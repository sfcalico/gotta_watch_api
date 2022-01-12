from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
import os
from dotenv import load_dotenv
load_dotenv()

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
import models
models.db.init_app(app)

# def root():
#     return 'ok'
# app.route('/', methods=["GET"])(root)

# signup user
@cross_origin()
def signup():
    user = models.User(
        email=request.json["email"],
        password=request.json["password"]
    )
    models.db.session.add(user)
    models.db.session.commit()
    return {
        "user": user.to_json()
    }
app.route('/users/signup', methods=["POST"])(signup)

# login user
def login():
    user = models.User.query.filter_by(email=request.json["email"]).first()
    if not user:
        return {
            "message": "User not found"
        }, 404
    return { 
        "user": user.to_json() }
app.route('/users/login', methods=["POST"])(login)

# verify user
def verify():
    user = models.User.query.filter_by(id=request.headers["Authorization"]).first()
    if not user:
        return {
            "message": "user not found"
        }, 404
    if user:
        return { "user": user.to_json() }
app.route('/users/verify', methods=["GET"])(verify)

# update user's bio
def update(id):
    user = models.User.query.filter_by(id=id).first()
    bio = request.json["bio"]
    user.bio = bio
    models.db.session.add(user)
    models.db.session.commit()
    return { "user": user.to_json() }
app.route('/users/<int:id>', methods=["PUT"])(update)

#save listing to profile
def save(id):
    user = models.User.query.filter_by(id=id).first()
    listing = models.Listing(
        title=request.json["title"],
        year=request.json["year"],
        type=request.json["type"],
        user_id=request.json["user_id"]
    )
    user.listings.append(listing)
    models.db.session.add(user)
    models.db.session.add(listing)
    models.db.session.add(user)
    models.db.session.commit()
    return {
        "user": user.to_json(),
        "listing": listing.to_json()
    }
app.route('/listings/save/<int:id>', methods=["POST"])(save)

# remove listing from profile
def remove(id):
    listing = models.Listing.query.filter_by(id=id).first()
    models.db.session.delete(listing)
    models.db.session.commit()
    return {
        "listing": listing.to_json()
    }
app.route('/listings/remove/<int:id>', methods=["DELETE"])(remove)

def see_shows(id):
    listings = models.Listing.query.filter_by(user_id=id).filter_by(type="series").all()
    return {
        "listings": [l.to_json() for l in listings]
    }
app.route('/listings/users/<int:id>/series', methods=["GET"])(see_shows)

def see_movies(id):
    listings = models.Listing.query.filter_by(user_id=id).filter_by(type="movie").all()
    return {
        "listings": [l.to_json() for l in listings]
    }
app.route('/listings/users/<int:id>/movies', methods=["GET"])(see_movies)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)