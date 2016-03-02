# """Utility file to seed ratings database from Yoga JSON file data in seed_data/"""

import json 

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
from model import (User, Category, Pose, Image)
from model import connect_to_db, db
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


# def load_users():
#     """Load users from u.user into database."""

#     print "Users"

#     for i, row in enumerate(open("seed_data/u.user")):
#         row = row.rstrip()
#         user_id, age, gender, occupation, zipcode = row.split("|")

#         user = User(user_id=user_id,
#                     age=age,
#                     zipcode=zipcode)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(user)

#         # provide some sense of progress
#         if i % 100 == 0:
#             print i

#     # Once we're done, we should commit our work
#     db.session.commit()


# def load_movies():
#     """Load movies from u.item into database."""

#     print "Movies"

#     for i, row in enumerate(open("seed_data/u.item")):
#         row = row.rstrip()

#         # clever -- we can unpack part of the row!
#         movie_id, title, released_str, junk, imdb_url = row.split("|")[:5]

#         # The date is in the file as daynum-month_abbreviation-year;
#         # we need to convert it to an actual datetime object.

#         if released_str:
#             released_at = datetime.datetime.strptime(released_str, "%d-%b-%Y")
#         else:
#             released_at = None

#         # Remove the (YEAR) from the end of the title.

#         title = title[:-7]   # " (YEAR)" == 7

#         movie = Movie(movie_id=movie_id,
#                       title=title,
#                       released_at=released_at,
#                       imdb_url=imdb_url)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(movie)

#         # provide some sense of progress
#         if i % 100 == 0:
#             print i

#     # Once we're done, we should commit our work
#     db.session.commit()


# def load_ratings():
#     """Load ratings from u.data into database."""

#     print "Ratings"

#     for i, row in enumerate(open("seed_data/u.data")):
#         row = row.rstrip()

#         user_id, movie_id, score, timestamp = row.split("\t")

#         user_id = int(user_id)
#         movie_id = int(movie_id)
#         score = int(score)

#         # We don't care about the timestamp, so we'll ignore this

#         rating = Rating(user_id=user_id,
#                         movie_id=movie_id,
#                         score=score)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(rating)

#         # provide some sense of progress
#         if i % 1000 == 0:
#             print i

#             # An optimization: if we commit after every add, the database
#             # will do a lot of work committing each record. However, if we
#             # wait until the end, on computers with smaller amounts of
#             # memory, it might thrash around. By committing every 1,000th
#             # add, we'll strike a good balance.

#             db.session.commit()

#     # Once we're done, we should commit our work
#     db.session.commit()


# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()


# if __name__ == "__main__":
#     connect_to_db(app)
#     db.create_all()

#     load_users()
#     load_movies()
#     load_ratings()
#     set_val_user_id()

#     # Mimic what we did in the interpreter, and add the Eye and some ratings
#     eye = User(email="the-eye@of-judgment.com", password="evil")
#     db.session.add(eye)
#     db.session.commit()

#     # Toy Story
#     r = Rating(user_id=eye.user_id, movie_id=1, score=1)
#     db.session.add(r)

#     # Robocop 3
#     r = Rating(user_id=eye.user_id, movie_id=1274, score=5)
#     db.session.add(r)

#     # Judge Dredd
#     r = Rating(user_id=eye.user_id, movie_id=373, score=5)
#     db.session.add(r)

#     # 3 Ninjas
#     r = Rating(user_id=eye.user_id, movie_id=314, score=5)
#     db.session.add(r)

#     # Aladdin
#     r = Rating(user_id=eye.user_id, movie_id=95, score=1)
#     db.session.add(r)

#     # The Lion King
#     r = Rating(user_id=eye.user_id, movie_id=71, score=1)
#     db.session.add(r)

#     db.session.commit()
    
#     # Add our user
#     jessica = User(email="jessica@gmail.com",
#                    password="love",
#                    age=42,
#                    zipcode="94114")
#     db.session.add(jessica)
#     db.session.commit()

#     # Toy Story
#     r = Rating(user_id=jessica.user_id, movie_id=1, score=5)
#     db.session.add(r)

#     # Robocop 3
#     r = Rating(user_id=jessica.user_id, movie_id=1274, score=1)
#     db.session.add(r)

#     # Judge Dredd
#     r = Rating(user_id=jessica.user_id, movie_id=373, score=1)
#     db.session.add(r)

#     # 3 Ninjas
#     r = Rating(user_id=jessica.user_id, movie_id=314, score=1)
#     db.session.add(r)

#     # Aladdin
#     r = Rating(user_id=jessica.user_id, movie_id=95, score=5)
#     db.session.add(r)

#     # The Lion King
#     r = Rating(user_id=jessica.user_id, movie_id=71, score=5)
#     db.session.add(r)

#     db.session.commit()
