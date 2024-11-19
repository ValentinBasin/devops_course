import logging
from pymongo import MongoClient

logger = logging.getLogger(__name__)

CONNECTION_STRING = "mongodb://localhost:27017/"
DATABASE_NAME = "flask_logs"
COLLECTION_NAME = "logs"


def get_database(mongo_instanse: str, database_name: str):
    mongo_client = MongoClient(mongo_instanse)
    logger.info(mongo_client)
    return mongo_client[database_name]


database = get_database(CONNECTION_STRING, DATABASE_NAME)
collection = database[COLLECTION_NAME]


def put_docs(data: list):
    resp = collection.insert_many(data)
    if resp.acknowledged:
        logger.info(f"{len(resp.inserted_ids)} new docs added to database")


def get_last_doc():
    try:
        last_doc = collection.find().limit(1).sort({"@timestamp": -1})[0]
        logger.info(f"Timestamp of latest doc in Database is {last_doc["@timestamp"]}")
        return last_doc
    except IndexError:
        logger.info("Database collection is empty")
        return {"@timestamp": "1970-11-19T08:30:36.650Z"}
