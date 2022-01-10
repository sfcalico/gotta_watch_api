from flask import Flask, request
app = Flask(__name__)
import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)

# def root():
#     return 'ok'
# app.route('/', methods=["GET"])(root)

# signup user
def signup():
    user = models.User(
        email=request.json["email"],
        password=request.json["password"]
    )
    models.db.session.add(user)
    models.db.commit()
    return {
        "user": user.to_json()
    }
app.route('/', methods=["POST"])(signup)

# login user
def login():
    return 'ok'
app.route('/', methods=["POST"])(login)

# verify user
def verify():
    return 'ok'
app.route('/', methods=["POST"])(verify)

# update user's bio
def update():
    return 'ok'
app.route('/', methods=["PUT"])(update)

# search shows and series
def search():
    return 'ok'
app.route('/', methods=["GET"])(search)

#save listing to profile
def save():
    return 'ok'
app.route('/', methods=["POST"])(save)

# move listing to history page
def watch():
    return 'ok'
app.route('/', methods=["POST"])(watch)

# remove listing from profile
def remove():
    return 'ok'
app.route('/', methods=["DELETE"])(remove)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)