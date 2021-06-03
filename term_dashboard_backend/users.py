from flask import Flask, jsonify, request
from passlib.hash import pbkd
import uuid

class User:
    def signup(self):
        #  Check if user already exists, return 400 if it does.
        user = {
            "_id": uuid.uuid4().hex,
            "username": request.form.get('username'),
            "email": request.form.get('username'),
            "password":request.form.get('password'),
            "deadlines": []
        }

        #Encrypt the password

        return jsonify(user), 200

    def login(self):
        #authenticate user
    

