import pymongo
from flask import Flask
from app import routes

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["kenzie"]
collection = db["posts"]

def create_app():

    app = Flask(__name__)
    routes.init_app(app)

    return app