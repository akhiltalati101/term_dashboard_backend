from flask import Flask, json, jsonify, request
from pymongo import MongoClient
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from passlib.hash import pbkdf2_sha256
from term_dashboard_backend import db
import uuid

class User:
    def signup(self):
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
            access_token = create_access_token(identity=user['email'])
            return jsonify(access_token=access_token)

        return jsonify({"error": "Signup Failed"}), 400

    def login(self):
        user = db.users.find_one({"email": request.form.get('email')})

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            access_token = create_access_token(identity=user['email'])
            return jsonify(access_token=access_token)
        
        return jsonify({ "error": "Invalid login credentials" }), 401  
