# Onto2Taxo - Ontology to Taxonomy

## A simple python CLI tool to translate an OWL ontology into a JSON taxonomy file

This program has been developed to extract and translate the class hierarcies present in OWL ontologies and represent them in a JSON taxonomy, in line with the requirements for [ICON](https://github.com/jingcshi/ICON)

## Quickstart

To run Onto2Taxo, make sure you have python version `3.12.4` installed and run the following command to install the correct dependencies:

`pip install requirements.txt`

Now to run Onto2Taxo run the following command:

`python main.py -input <input_ontology_path> -output <output_location>`

*Note: to make the above command cleaner, move the input ontology into the Onto2Taxo directory. This allows you to specify the file name of the input and then the output JSON will be placed in the Onto2Taxo directory*

In some cases, depending on how the input ontology has been constructed, the SPARQL queries used may require some modification to allow the program to function correctly. These queries can be found in `main.py` in the `classes_query(onto)` and `subClasses_query(onto)` functions respectively.
