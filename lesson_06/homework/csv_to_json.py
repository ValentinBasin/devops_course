import csv
import json
import random
from typing import Any, Dict, List


# conver data types from strings to correct types
def convert_row(row: Dict[str, Any]) -> None:
    # convert release date to int
    try:
        row["datereleased"] = int(row["datereleased"])
    except ValueError:
        del row["datereleased"]

    # convert rating to int
    try:
        row["rating"] = int(row["rating"])
    except ValueError:
        del row["rating"]

    # teke only one genere from list
    row_generes = row["genere"].split(", ")
    row["genere"] = random.choice(row_generes)


def csv_to_dict(csv_file_path: str) -> List[Dict[str, Any]]:
    data = []
    with open(csv_file_path, encoding="utf-8") as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            convert_row(row)
            row["_index"] = "movies"
            data.append(row)
    return data


def csv_to_json(csv_file_path, json_file_path):
    json_array = []

    # read csv file
    with open(csv_file_path, encoding="utf-8") as csvf:
        # load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csv_reader:
            # add this python dict to json array
            json_array.append({"index": {}})
            convert_row(row)
            json_array.append(row)

    # convert python json_array to JSON String and write to file
    with open(json_file_path, "w", encoding="utf-8") as jsonf:
        for row in json_array:
            json_string = json.dumps(row)
            jsonf.write(json_string + "\n")
