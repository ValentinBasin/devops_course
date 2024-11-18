from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200", basic_auth=("elastic", "changeme"))

test = es.search(index="flask-logs-8.15.3", query={"match_all": {}})["hits"]["hits"]

print(test)
