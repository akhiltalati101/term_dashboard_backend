from flask import Flask
from pymongo import MongoClient
import json

app = Flask(__name__)

from term_dashboard_backend import routes

mongoClient = MongoClient('mongodb://127.0.0.1:27017')
db = mongoClient.get_database('cd_backend_db')
# $ mongo
# $ use fremp_test_app1_db
# $ db.fremp_test_app1_col.insertOne({'data': 'Hello World from MongoDB'})

# @app.route('/api/get/')
# def getdata():
#     data = ''
#     if col.find({}):
#         for data in col.find({}):
#             user = data['user']
#             password = data['password']
#     return {'user': user, 'password': password}

if __name__ == "__main__":
    app.run()