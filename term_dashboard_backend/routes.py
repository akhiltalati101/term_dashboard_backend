from flask import Flask, request, jsonify
from term_dashboard_backend import app
from term_dashboard_backend.users import User




@app.route('/token', methods=['POST'])
def create_token():
    return User().create_token()

@app.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/login/', methods=['POST'])
def login():
    return User().login()
