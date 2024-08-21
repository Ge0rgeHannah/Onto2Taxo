import argparse
import json
import rdflib


# Query the ontology and return the results as a list
def sparql_query(onto, query):
    pass


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

    # TODO: Query ontology for all classes

    # TODO: Query ontology for all rdfs:subClassOf relationships

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
