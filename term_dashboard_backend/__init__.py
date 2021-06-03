from flask import Flask
from pymongo import MongoClient
import json

app = Flask(__name__)

# Database
mongoClient = MongoClient('mongodb://127.0.0.1:27017')
db = mongoClient.get_database('cd_backend_db')

# Routes
from term_dashboard_backend import routes

if __name__ == "__main__":
    app.run()