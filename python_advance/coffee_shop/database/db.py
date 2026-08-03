from pymongo import MongoClient


class Db:
    def __init__(self, mongo_uri: str):
        self.mongo_uri = mongo_uri
        self.client = None
        self.database = None


    def connection(self):
        try:
            print("\nConnecting to db...\n")

            # Checking if already connected
            if self.client:
                return self.client

            # Creating MongoDB client
            self.client = MongoClient(self.mongo_uri)

            # Checking connection
            self.client.admin.command("ping")

            print("\nConnected successfully\n")

            return self.client

        except Exception as err:
            print(f"Database error: {err}")
            self.client = None
            return None


    def create_collection(self, collection_name):

        client = self.connection()

        if client is None:
            return None

        # Selecting database
        database = client["cozy_cup"]

        # Storing database reference
        self.database = database

        # Checking collection exists or not
        if collection_name not in database.list_collection_names():

            database.create_collection(collection_name)

            print(f"\n{collection_name} Collection created\n")

        else:

            print(f"\n{collection_name} Collection already exists\n")


    def __getitem__(self, collection_name):

        client = self.connection()

        if client is None:
            return None

        database = client["your_database_name"]

        return database[collection_name]