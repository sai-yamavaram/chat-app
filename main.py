# import gridfs
import base64
import json
import mongo
import urllib.request
import io
from mongo import connection
import flask
# from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_cors import CORS
from flask import Flask,redirect, url_for, request,jsonify
from functools import wraps
import uuid

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '5tuAl3QNQhewhbApqeFC8cDuKbr1'
# JWTManager(app)
CORS(app)

class Mongo_CRUD:
    def __init__(self ,client):
        self.client =client
        self.db = self.client.business

    def fetch_users_data_all(self):
        print('hi')
       # access_token = create_access_token(identity=user_id)
        try:
            all_products_of_current_user = list(self.db.user_k.find({}))
            #print(all_products_of_current_user)
            #return jsonify(message="Fetched Users!", data=all_products_of_current_user), 201
            return {'data': all_products_of_current_user}
        except Exception as e:
            raise Exception("Unable to Fetch data")

    def insert_group_data(self,name,description,imageUrl,users):
        # users_group_data = eval(users_group_data)

        try:
            groupData = {
                "name":name,
                "description":description,
                "imageUrl":imageUrl,
                "users": users,
                "group_id": uuid.uuid1().hex 
            }
            print(groupData)
            self.db.groups_k.insert_one(groupData)
            #return jsonify(message=" Insert succesfully",),200
            return {'data':'succes'}
        except Exception as e:
            raise Exception(e)

    def insert_user_data(self,val):
        self.db.user_k.insert_many(val)

    def fetch_groups(self):
        try:
            k = self.db.groups_k.find({},{"_id" :0})
            return list(k)
        except Exception as e:
            raise Exception("Unable to Fetch Groups")
    
    def fetch_group_id(self,id):
        try:
            k = self.db.groups_k.find({"group_id":id},{"_id" :0})
            return list(k)
        except Exception as e:
            raise Exception("Unable to Fetch Groups")
            

    
    





#app=FastAPI()
password ='2AyZYEKDOLnozrg6'
database_user ='fahadev'
con = connection(password)
client = con.mongo_connect(database_user)
mongo_crud = Mongo_CRUD(client)
# user
@app.route('/add/user' , methods = ['POST', 'GET'])
def inser_nw_data():
    new =[{"1":['AVi','https://www.shutterstock.com/image-vector/check-back-soon-hand-lettering-inscription-1379832464']},{"2":['AVi','https://www.shutterstock.com/image-vector/check-back-soon-hand-lettering-inscription-1379832464']},{"3":['AV','https://www.shutterstock.com/image-vector/check-back-soon-hand-lettering-inscription-1379832464']},{'4':['sun','https://www.shutterstock.com/image-vector/check-back-soon-hand-lettering-inscription-1379832464']},{'5':['rwq','https://www.shutterstock.com/image-vector/check-back-soon-hand-lettering-inscription-1379832464']}]
    return mongo_crud.insert_user_data(new)


@app.route('/users' , methods = ['POST', 'GET'])
def fecth_all():
    
    p=mongo_crud.fetch_users_data_all()
    return p

@app.route('/add/group' , methods = ['POST'])
def insert_group_data():
    new_group_data = request.data
    new_group_data = eval(new_group_data)

    if request.method == 'POST':
        # name, description , image
        name = new_group_data.get('name')
        description = new_group_data.get('description')
        imageUrl = new_group_data.get('imageUrl')
        users = new_group_data.get('users')

        if name and description and imageUrl and users :
            # print("request",request,"body",new_group_data['sedfsdfs'])
            mongo_crud.insert_group_data(name,description,imageUrl,users)
            return {"success" : True} ,200
        else:
            return {"success",False}, 400

@app.route('/groups',methods=['GET'])
def get_groups():
    try:
        groups = mongo_crud.fetch_groups()
        return {"success":True,"groups":groups} 
    except Exception as e:
        return {"success":False}

@app.route('/search',methods=['GET'])
def get_groups_from_id():
    try:
        args = request.args
        id = args.get('id')
        groups = mongo_crud.fetch_group_id(id)
        # print("groups",groups)
        return {"success":True,"data":groups} 
    except Exception as e:
        return {"success":False}


if __name__ == '__main__':
    app.run()
    