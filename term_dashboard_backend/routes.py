from flask import Flask, request, jsonify
from term_dashboard_backend import app
from term_dashboard_backend.users import User
from flask_jwt_extended import jwt_required




@app.after_request
def refresh_token():
    return User().refresh_token()

@app.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/login/', methods=['POST'])
def login():
    return User().login()

@app.route('/user/deadlines/', methods=['GET'])
@jwt_required()
def deadlines():
    return User().deadlines()
