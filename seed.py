# """Utility file to seed database from Yoga JSON file data in seed_data/"""

import json 

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
from tullymodel import (User, Category, Pose, Image)
from tullymodel import connect_to_db, db
from server import app


# data_dict = json.loads("yoga_asanas.json")

# class Category(db.Model):
#     """Categories of segments of poses in the sequence."""

#     __tablename__ = "categories"

#     category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     category_name = db.Column(db.String(100), nullable=False )Ca


def load_users():
    """
    load existing users from user.csv into database
    """

    print "Users"

    #yoga_users is a csv file
    users_file = open("seed_data/yoga_users")

    for line in users_file:
        line = line.rstrip()
        line = line.split(",")
        a_user = User(email=line[0],
                      password=line[1])
        db.session.add(a_user)

    # user = User(user_id=user_id, email=email)

    db.session.commit()


def load_categories(data_dict):
    """Loads categories from yoga_asanas.json file"""

    # import pdb; pdb.set_trace()
    # data = open("yoga_asanas.json")
    # data_dict = json.load(data)
    # print data_dict

    print "Categories"
    
    for category in data_dict:
        new_category = Category(category_name=category)
        print new_category
        db.session.add(new_category)

    db.session.commit()


def load_poses():
    """
    load existing users from user.csv into database
    """

    print "Poses"

    #yoga_users is a csv file 
    users_file = open("seed_data/poses.csv")

    for line in users_file:
        line = line.rstrip()
        line = line.split("|")
        pose = Pose(category= line[1], common_name=line[2],
                      sanskrit_name=line[3], breathe=line[4],
                      image_url=line[5], time=line[6], pregnancy=line[7])
        db.session.add(pose)

    # user = User(user_id=user_id, email=email)

    db.session.commit()


def load_images(images):
    """Loads images from asana_images.json file"""

    # import pdb; pdb.set_trace()
    # data = open("yoga_asanas.json")
    # data_dict = json.load(data)
    # print data_dict

    print "Images"
    
    for image in images:
        new_image = Image(image_common_name=image)
        print new_image
        db.session.add(new_image)

    db.session.commit()

# def load_poses(data_dict):
#     """Load poses from yoga_asanas.json file"""

#     for category, value in data_dict:
#         category_id = Category.query.filter_by(category_name=category)
#         for pose, details in value:
#             # pose_name = pose
#             pose_list_time = details[2]
#             new_pose = Pose(pose_name=pose, pose_list_time=pose_list_time, category_id=category_id)
#             db.session.add(new_pose)

#     db.session.commit()


#     for category in data_dict:
#     ...     for poses in data_dict[category]:
#     ...             for steps in data_dict[poses]:
#     ...                     print steps


# >>> for category in data_dict:
# ...             print data_dict[poses]

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    users_file = open("./seed_data/users.csv.odt")
    data = open("yoga_asanas.json")
    print data
    images = open("asana_test.json")
    data_dict = json.load(data)
    images = json.load(images)
    connect_to_db(app)
    db.create_all()
    load_categories(data_dict)
    load_poses()
    load_users()
    load_images(images)
    print "Connected to DB."


