import argparse
import json
import rdflib
from pathlib import Path


# Query the ontology and return the classes as a list
def classes_query(onto):

    # This query will need to be changed slightly from different ontologies
    query_1 = '''
    SELECT ?className WHERE {
        ?class rdf:type owl:Class .
        BIND(STRAFTER(STR(?class), "#") AS ?className)
    }
    '''

    results = []
    raw_result = onto.query(query_1)
    for row in raw_result:
        results.append(str(row.className))

    return results


# Query the ontology and return the subClassOf relations as a list
def subClasses_query(onto):
    
    # This query will need to be changed slightly from different ontologies
    query_2 = '''
    SELECT ?parent ?child WHERE {
        ?p rdf:type owl:Class .
        ?c rdf:type owl:Class .
        ?c rdfs:subClassOf ?p .
        BIND(STRAFTER(STR(?p), "#") AS ?parent)
        BIND(STRAFTER(STR(?c), "#") AS ?child)
    }
    '''

    results = []
    raw_result = onto.query(query_2)
    for row in raw_result:
        relation = [str(row.parent), str(row.child)]
        results.append(relation)

    return results


# Create a list of each node with its associated id
def populate_nodes(class_list, starting_id=1):
    nodes_list = []
    current_id = starting_id
    for c in class_list:
        class_dict = {"id": current_id,
                      "label": c}
        nodes_list.append(class_dict)
        current_id += 1

    return nodes_list


# Create a list of each subClassOf relation
def populate_edges(relations_list, node_list):
    edges_list = []
    for r in relations_list:
        parent_target = r[0]
        child_target = r[1]
        tgt = ""
        src = ""

        # Identify parent
        for n in node_list:
            if n["label"] == parent_target:
                tgt = n["id"]

        # Identify child
        for n in node_list:
            if n["label"] == child_target:
                src = n["id"]

        edge = {"src": src,
                "tgt": tgt,
                "label": "original"}

        edges_list.append(edge)

    return edges_list


# Generate the taxonomy
def run(args):

    onto = args.onto
    taxo = args.taxo

    g = rdflib.Graph()
    g.parse(onto)

    # TODO: Query ontology for all classes
    all_classes = classes_query(g)

    # TODO: Query ontology for all rdfs:subClassOf relationships
    all_relations = subClasses_query(g)

    # TODO: Populate nodes list
    nodes_list = populate_nodes(all_classes)

    # TODO: Populate edges list
    edges_list = populate_edges(all_relations, nodes_list)

    # TODO: Combine nodes and edges lists into a dictionary
    taxo_dict = {
        "nodes":nodes_list,
        "edges":edges_list
    }

    # TODO: Write dictionary to JSON
    taxo_json = json.dumps(taxo_dict, indent=4)

    onto_path = Path(onto)
    taxo_name = onto_path.stem

    with open(f"{taxo}{taxo_name}.json", "w") as output:
        output.write(taxo_json)


# Handle and bind arguments
def main():
    parser = argparse.ArgumentParser(
        prog="Onto2Taxo",
        description="A CLI tool for translating OWL class-hierarchies into JSON taxonomies"
    )
    parser.add_argument(
        "--I",
        "-input",
        type=str,
        help="The file path of the input ontology",
        dest="onto",
        required=True
    )
    parser.add_argument(
        "--O",
        "-output",
        type=str,
        help="The location of the output taxonomy",
        dest="taxo",
        required=False,
        default=""
    )

    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
