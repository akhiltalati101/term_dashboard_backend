from datetime import datetime
from datetime import timedelta
from datetime import timezone

from flask import jsonify, request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

from passlib.hash import pbkdf2_sha256

from term_dashboard_backend import db
import uuid


class User:
    def signup(self):
        user = {
            "_id": uuid.uuid4().hex,
            "username": request.form.get('username'),
            "email": request.form.get('username'),
            "password": request.form.get('password'),
            "deadlines": []
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check existing user
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "The email address already exists"}), 400
        # Insert users
        if db.users.insert(user):
            response = jsonify({"msg": "login successful"})
            access_token = create_access_token(identity=user['email'])
            set_access_cookies(response, access_token)
            return response

        return jsonify({"error": "Signup Failed"}), 400

    def login(self):
        user = db.users.find_one({"email": request.form.get('username')})

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):            
            response = jsonify({"msg": "login successful"})
            access_token = create_access_token(identity=user['email'])
            set_access_cookies(response, access_token)
            return response

        return jsonify({"error": "Invalid login credentials"}), 401

    def logout(self):
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response

    def deadlines(self):
        current_user_email = get_jwt_identity()
        print(current_user_email)
        user = db.users.find_one({"email": current_user_email})
        if user:
            deadlines = user['deadlines']
            return jsonify(deadlines=deadlines)

        return jsonify({"error": "Invalid token, user does not exist in database"}), 401

    def refresh_token(self):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original respone
            return response

