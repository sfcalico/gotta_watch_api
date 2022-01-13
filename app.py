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

## Signup user
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

## Login user
def login():
    user = models.User.query.filter_by(email=request.json["email"]).first()
    if not user:
        return {
            "message": "User not found"
        }, 404
    return { 
        "user": user.to_json() }
app.route('/users/login', methods=["POST"])(login)

## Verify user
def verify():
    user = models.User.query.filter_by(id=request.headers["Authorization"]).first()
    if not user:
        return {
            "message": "user not found"
        }, 404
    if user:
        return { "user": user.to_json() }
app.route('/users/verify', methods=["GET"])(verify)

## Update user's bio ## maybe use for stretch goals
# def update(id):
#     user = models.User.query.filter_by(id=id).first()
#     bio = request.json["bio"]
#     user.bio = bio
#     models.db.session.add(user)
#     models.db.session.commit()
#     return { "user": user.to_json() }
# app.route('/users/<int:id>', methods=["PUT"])(update)

## Save listing to profile
def save(id):
    user = models.User.query.filter_by(id=id).first()
    listing = models.Listing(
        title=request.json["title"],
        year=request.json["year"],
        type=request.json["type"],
        poster=request.json["poster"],
        user_id=request.json["user_id"],
        watched=False
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

## remove listing from profile
def remove(id, user_id):
    listing = models.Listing.query.filter_by(id=id).filter_by(user_id=user_id).first()
    models.db.session.delete(listing)
    models.db.session.commit()
    return {
        "listing": listing.to_json()
    }
app.route('/listings/remove/<int:id>/<int:user_id>', methods=["DELETE"])(remove)

## Series to watch page
def see_shows(id):
    listings = models.Listing.query.filter_by(user_id=id).filter_by(type="series").filter_by(watched=False).all()
    return {
        "listings": [l.to_json() for l in listings]
    }
app.route('/listings/users/<int:id>/series', methods=["GET"])(see_shows)

## Movies to watch page
def see_movies(id):
    listings = models.Listing.query.filter_by(user_id=id).filter_by(type="movie").filter_by(watched=False).all()
    return {
        "listings": [l.to_json() for l in listings]
    }
app.route('/listings/users/<int:id>/movies', methods=["GET"])(see_movies)

## Push title to Watched page
def have_seen(id):
    seen = models.Listing.query.filter_by(id=id).first()
    seen.watched = True
    models.db.session.add(seen)
    models.db.session.commit()
    return {
        "listing": seen.to_json()
    }
app.route('/listings/users/<int:id>/seen', methods=["PUT"])(have_seen)

## Watched page, series
def series_history(id):
    series = models.Listing.query.filter_by(user_id=id).filter_by(type="series").filter_by(watched=True).all()
    return {
        "series": [s.to_json() for s in series]
    }
app.route('/listings/users/history/<int:id>/series')(series_history)

## Watched page, movies
def movies_history(id):
    movies = models.Listing.query.filter_by(user_id=id).filter_by(type="movie").filter_by(watched=True).all()
    return {
        "movies": [m.to_json() for m in movies]
    }
app.route('/listings/users/history/<int:id>/movies')(movies_history)

## Push title back to saved pages
def not_seen(id):
    seen = models.Listing.query.filter_by(id=id).first()
    seen.watched = False
    models.db.session.add(seen)
    models.db.session.commit()
    return {
        "listing": seen.to_json()
    }
app.route('/listings/users/<int:id>/notyet', methods=["PUT"])(not_seen)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)