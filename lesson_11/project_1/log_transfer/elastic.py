from elasticsearch import Elasticsearch
import logging


logger = logging.getLogger(__name__)

client = Elasticsearch("http://localhost:9200", basic_auth=("elastic", "changeme"))


def get_new_docs(timestamp: str) -> list:
    query = {"range": {"@timestamp": {"gt": timestamp}}}
    resp = client.search(index="flask-logs-8.15.3", query=query, size=10000)
    logger.info(f"Got {resp['hits']['total']['value']} new docs")
    output = []
    for hit in resp["hits"]["hits"]:
        output.append(hit["_source"])
    return output
