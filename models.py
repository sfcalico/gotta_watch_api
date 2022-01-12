from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)
    bio = db.Column(db.String)
    listings = db.relationship('Listing', secondary="user_listings")
    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "bio": self.bio
        }

class Listing(db.Model):

    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    year = db.Column(db.String)
    type = db.Column(db.String)
    user_id = db.Column(db.Integer)
    poster = db.Column(db.String)
    users = db.relationship('User', secondary="user_listings")
    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "type": self.type,
            "poster": self.poster,
            "user_id": self.user_id
        }

class User_Listings(db.Model):
    
    __tablename__ = 'user_listings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('users.id'))