from flask import Flask, jsonify, request
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
from term_dashboard_backend import db
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
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        #Check existing user
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "The email address already exists"}), 400
        #Insert users
        if db.users.insert(user):
            return jsonify(user), 200
        
        return jsonify({"error": "Signup Failed"}), 400
        

