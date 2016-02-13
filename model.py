"""Models and database functions for Asana Generator project."""

from flask_sqlalchemy import SQLAlchemy
import json 
# data_dict = json.load("yoga_asanas.json")

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of asana sequence website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

# CREATE TABLE poses (
#     pose_id SERIAL PRIMARY KEY, 
#     pose_name VARCHAR(100) NOT NULL,
#     pose_list VARCHAR(500),
#     category_id INTEGER REFERENCES Category, 
#     pose_list_time INTEGER,
#     image_file_name VARCHAR(100));

    # def __repr__(self):
    #     """Provide helpful representation when printed."""

    #     return "<User user_id=%s email=%s>" % (self.user_id, self.email)


class Pose(db.Model):
    """Asanas for sequence."""

    __tablename__ = "poses"

    pose_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pose_name = db.Column(db.String(100), nullable=False )
    # pose_name = db.Column(db.String(100),nullable=False )
    pose_list = db.Column(db.String(500), nullable=False )
    category_id = db.Column(db.Integer, nullable=False )
    pose_list_time = db.Column(db.Integer, nullable=False )
    image_file_name = db.Column(db.String(100), nullable=False )

    # def __repr__(self):
    #     """Provide helpful representation when printed."""

    #     return "<Movie movie_id=%s title=%s>" % (self.movie_id, self.title)


# CREATE TABLE poses (
#         pose_id SERIAL PRIMARY KEY, 
#         pose_name VARCHAR(100) NOT NULL,
#         pose_list VARCHAR(500),
#         category_id INTEGER REFERENCES Category, 
#         pose_list_time INTEGER,
#         image_file_name VARCHAR(100));


class Category(db.Model):
    """Categories of segments of poses in the sequence."""

    __tablename__ = "categories"

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False )
    


# CREATE TABLE categories (
#         category_id SERIAL PRIMARY KEY, 
#         category_name VARCHAR(100) NOT NULL,
#         pose_id INTEGER REFERENCES Pose, 
#         );

    # def __repr__(self):
    #     """Provide helpful representation when printed."""

    #     return "<Rating rating_id=%s movie_id=%s user_id=%s score=%s>" % (
    #         self.rating_id, self.movie_id, self.user_id, self.score)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///chelsea'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    # db.create_all()
    print "Connected to DB."