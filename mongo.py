import pymongo
#client = pymongo.MongoClient("mongodb://localhost:27017/")
from pymongo import MongoClient
from pymongo import database
from pymongo.errors import ConnectionFailure
password ='2AyZYEKDOLnozrg6'
database_user ='fahadev'
# = MongoClient(f"mongodb+srv://faha_nonprod:{password}@fahadev.tj25u.mongodb.net/{myFirstDatabase}?retryWrites=true&w=majority")
class connection:
    def __init__(self , password):
        self.val=password
    def mongo_connect(self , database_user):
        k = "mongodb+srv://faha_nonprod:{}@fahadev.tj25u.mongodb.net/{}?retryWrites=true&w=majority".format(self.val,database_user)
        client = MongoClient(k)
        try:
            client.admin.command('ismaster')
            print("Connection Succesfull")
            return client
        except ConnectionFailure as e:
            print("Server not available")

            raise Exception("Server not available error {}".format(e))
        
        





