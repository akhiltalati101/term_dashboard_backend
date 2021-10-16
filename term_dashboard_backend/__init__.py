import os
from flask import Flask
from pymongo import MongoClient
import json
from flask_jwt_extended import JWTManager


app = Flask(__name__)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
jwt = JWTManager(app)

# Database
mongoClient = MongoClient('mongodb://127.0.0.1:27017')
db = mongoClient.get_database('cd_backend_db')

# Routes
from term_dashboard_backend import routes

if __name__ == "__main__":
    app.run()