from flask import Flask
from term_dashboard_backend import app
from term_dashboard_backend.users import User

@app.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()
