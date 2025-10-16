import os
import sys
import pymongo
import certifi

from heart_failure.constants import database_name, mongo_db_url
from heart_failure.logger import logging
from heart_failure.exception import HeartFailureException

ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name = database_name) -> None:
        try:
            if MongoDBClient.client is None:
                mongodb_url = os.getenv(mongo_db_url)
                if mongodb_url is None:
                    raise Exception(f"Environment Key: {mongo_db_url} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAfile=ca)
                self.client = MongoDBClient.client
                self.database = self.client[database_name]
                self.database_name = database_name
                logging.info(f"MongoDB connected.")
            
        except Exception as e:
            raise HeartFailureException(e, sys)