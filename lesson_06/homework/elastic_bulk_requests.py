from csv_to_json import csv_to_json
import requests

csv_file_path = r"imdb_top_1000.csv"
json_file_path = r"data.json"

csv_to_json(csv_file_path, json_file_path)
with open(json_file_path, "r") as file:
    data = file.read()
url = "http://localhost:9200/movies/_bulk"
requests.post(
    url,
    auth=("elastic", "changeme"),
    headers={"content-type": "application/json", "charset": "UTF-8"},
    data=str(data),
)
