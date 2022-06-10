# -*- coding: utf-8 -*-
"""
csv to yaml converter
"""
import sys
import logging  # missing-module-docstring
import argparse
import csv
import yaml

logging.basicConfig(level=logging.INFO)


def main():
    """main function"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input csv file")
    parser.add_argument("-o", "--output", help="output yaml file")

    args = parser.parse_args()
    if not args.input or not args.output:
        parser.print_help()
        logging.error("you need to specify input and output files with -i and -o flags")
        sys.exit(0)
    csv_to_yaml(args.input, args.output)


def names_schema(csv_obj):
    """return a dictionary with the schema for Invenio names"""
    return [
        {
            "affiliations": {
                "name": csv_obj["affiliations/0/name"],
            },
            "family_name": csv_obj["family_name"],
            "given_name": csv_obj["given_name"],
            "identifier": {
                "identifier": csv_obj["identifiers/0/identifier"],
                "scheme": csv_obj["identifiers/0/scheme"],
            },
        }
    ]


def csv_to_yaml(csv_file, yaml_file, schema=names_schema):
    """convert a csv file to a yaml file"""
    # read csv file
    to_yaml = []
    with open(csv_file, encoding="utf-8") as csv_f:
        reader = csv.DictReader(csv_f)
        for row in reader:
            logging.info(row)
            to_yaml.append(schema(row))
    # write yaml file
    with open(yaml_file, "w", encoding="utf-8") as yaml_f:
        for row in to_yaml:
            yaml.dump(row, yaml_f)


if __name__ == "__main__":
    main()
