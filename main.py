# import os
import csv
import yaml

# get csv_file as -i and yaml_file as -o


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input csv file")
    parser.add_argument("-o", "--output", help="output yaml file")

    args = parser.parse_args()
    if not args.input or not args.output:
        parser.print_help()
        print("you need to specify input and output files with -i and -o flags")
        exit(1)
    csv_to_yaml(args.input, args.output)


def names_schema(csv_obj):
    return  [
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
    # read csv file
    to_yaml = []
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            to_yaml.append(schema(row))
    with open(yaml_file, "w") as yaml_file:
        for row in to_yaml:
            yaml.dump(row, yaml_file)

if __name__ == "__main__":
    main()
