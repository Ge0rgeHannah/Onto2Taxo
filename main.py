import argparse
import json
import rdflib


# Query the ontology and return the classes as a list
def classes_query(onto):

    # This query will need to be changed slightly from different ontologies        BIND(STRAFTER(STR(?class), "#") AS ?className)
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
    
    # This query will need to be changed slightly from different ontologies        BIND(STRAFTER(STR(?class), "#") AS ?className)
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
    pass


# Create a list of each subClassOf relation
def populate_edges(relations_list, node_list):
    pass


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

    # TODO: Populate edges list

    # TODO: Combine nodes and edges lists into a dictionary

    # TODO: Write dictionary to JSON



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
