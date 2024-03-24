from logger import configure_logger
import pymongo
from pymongo.errors import ConnectionFailure
import os

# Configure logging
logger = configure_logger()


class MongoDBClient:
    def __init__(self):
        self.client = None
        self.db = None
        self.mongo_uri = os.getenv("MONGODB_URI")
        if not self.mongo_uri:
            raise ValueError("MONGO_URI environment variable is not set or is empty")

    def get_db(self):
        if self.client is None:
            try:
                self.client = pymongo.MongoClient(self.mongo_uri)
                self.db = self.client["chatbot"]
                logger.info("Successfully connected to MongoDB")
            except ConnectionFailure as e:
                logger.error(f"Failed to connect to MongoDB: {e}")
                self.db = None
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                self.db = None
        return self.db

    def close_db(self):
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed.")
            self.client = None
