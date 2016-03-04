"""Models and database functions for Asana Generator project."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
# import json 
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
   

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)
   

class Sequence(db.Model):
    """Full saved sequences for user of website."""

    __tablename__ = "sequences"

    seq_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    seq_name = db.Column(db.String(500), nullable=True)
    full_seq = db.Column("poses", postgresql.ARRAY(db.Integer))

   
    user = db.relationship("User",
                           backref=db.backref("sequences"))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User seq_id=%s seq_name=%s>" % (self.seq_id, self.seq_name)


class Pose(db.Model):
    """Asanas for sequence."""

    __tablename__ = "poses"

    pose_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category = db.Column(db.String(100), nullable=True)
    common_name = db.Column(db.String(100), nullable=False )
    sanskrit_name = db.Column(db.String(100),nullable=True )
    breathe = db.Column(db.String(500), nullable=True )
    image_url = db.Column(db.String(500), nullable=True)
    time = db.Column(db.Integer, nullable=True)
    pregnancy = db.Column(db.Integer, nullable=True )


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Pose pose_id=%s category=%s common_name=%s sanskrit_name=%s breathe=%s image_url pregnancy=%s>" % (self.pose_id, 
                                                    self.category, self.common_name, self.sanskrit_name, 
                                                    self.breathe, self.image_url, self.time, self.pregnancy)


class Image(db.Model):
    """Images of asanas for sequence website."""

    __tablename__ = "images"

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    image_common_name = db.Column(db.String(100), nullable=False )
    # image_url = db.Column(db.String, db.ForeignKey('movies.movie_id'))
    pose_id = db.Column(db.Integer, db.ForeignKey('poses.pose_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


    # # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("images"))

    # Define relationship to pose
    pose = db.relationship("Pose",
                            backref=db.backref("images"))
   

    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User image_id=%s image_common_name=%s>" % (self.image_id, self.image_common_name)



    # def __init__(self,
    #              id,
    #              common_name,
    #              sanskrit_name,
    #              breathe,
    #              image_url,
    #              category,
    #              random,
    #              ):
    #     self.id = id
    #     self.common_name = common_name
    #     self.sanskrit_name = sanskrit_name
    #     self.breathe = breathe
    #     self.image_url = image_url
    #     self.category = category
    #     self.random = random

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


def connect_to_db(app):
    """Connect the database to our Flask app."""

    #  Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hackbright@localhost/chelsea'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from tullyandtsegiserver import app
    connect_to_db(app)

    db.create_all()
    print "Connected to DB."

