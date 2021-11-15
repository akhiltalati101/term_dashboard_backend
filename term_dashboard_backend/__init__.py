import os
from flask import Flask
from pymongo import MongoClient
from datetime import timedelta
import json
from flask_jwt_extended import JWTManager


app = Flask(__name__)

# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
app.config["JWT_COOKIE_SECURE"] = os.environ.get('JWT_COOKIE_SECURE')
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

# Database
mongoClient = MongoClient('mongodb://127.0.0.1:27017')
db = mongoClient.get_database('cd_backend_db')

# Routes
from term_dashboard_backend import routes

if __name__ == "__main__":
    app.run()