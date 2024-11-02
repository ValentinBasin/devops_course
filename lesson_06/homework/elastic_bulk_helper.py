from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from csv_to_json import csv_to_dict

client = Elasticsearch("http://localhost:9200", basic_auth=("elastic", "changeme"))

csv_file_path = r"imdb_top_1000.csv"

data = csv_to_dict(csv_file_path)
bulk(client, data)
