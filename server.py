"""Tully and Tsegi's Asana Generator"""


# from javascript3demo
from flask import Flask, request, render_template, jsonify
import jinja2
# from ratings
# from flask import Flask, render_template, request, flash, redirect, session
# from flask_debugtoolbar import DebugToolbarExtension
# from model import connect_to_db, db, User, Movie, Rating


app = Flask(__name__)

IMAGES = [
    { "id": 1, "url": "http://www.pocketyoga.com/images/poses/child_traditional.png"},
    { "id": 2, "url": "http://www.pocketyoga.com/images/poses/downward_dog.png"},
    { "id": 3, "url": "http://www.pocketyoga.com/images/poses/forward_bend.png"},
    { "id": 4, "url": "http://www.pocketyoga.com/images/poses/chair_prayer.png"},
    { "id": 1, "url": "http://www.pocketyoga.com/images/poses/child_traditional.png"},
    { "id": 2, "url": "http://www.pocketyoga.com/images/poses/downward_dog.png"},
    { "id": 3, "url": "http://www.pocketyoga.com/images/poses/forward_bend.png"},
    { "id": 4, "url": "http://www.pocketyoga.com/images/poses/chair_prayer.png"},
    { "id": 5, "url": "http://unsplash.it/380/200"},
    { "id": 6, "url": "http://unsplash.it/360/200"},
    { "id": 7, "url": "http://unsplash.it/380/200"},
    { "id": 8, "url": "http://unsplash.it/320/200"},
    { "id": 9, "url": "http://unsplash.it/300/200"},
    { "id": 10, "url": "http://unsplash.it/290/200"},
    { "id": 11, "url": "http://unsplash.it/350/200"},
    { "id": 12, "url": "http://www.pocketyoga.com/images/thumbnailsbig/box_neutral-tnbig.png"},
    { "id": 1, "url": "http://unsplash.it/320/200"},
    { "id": 2, "url": "http://unsplash.it/300/200"},
    { "id": 3, "url": "http://unsplash.it/290/200"},
    { "id": 4, "url": "http://unsplash.it/350/200"},
    { "id": 5, "url": "http://unsplash.it/380/200"},
    { "id": 6, "url": "http://unsplash.it/360/200"},
    { "id": 7, "url": "http://unsplash.it/380/200"},
    { "id": 8, "url": "http://unsplash.it/320/200"},
    { "id": 9, "url": "http://unsplash.it/300/200"},
    { "id": 10, "url": "http://unsplash.it/290/200"},
    { "id": 11, "url": "http://unsplash.it/350/200"},
    { "id": 1, "url": "http://unsplash.it/320/200"},
    { "id": 2, "url": "http://unsplash.it/300/200"},
    { "id": 3, "url": "http://unsplash.it/290/200"},
    { "id": 4, "url": "http://unsplash.it/350/200"},
    { "id": 5, "url": "http://unsplash.it/380/200"},
    { "id": 6, "url": "http://unsplash.it/360/200"},
    { "id": 7, "url": "http://unsplash.it/380/200"},
    { "id": 8, "url": "http://unsplash.it/320/200"},
    { "id": 9, "url": "http://unsplash.it/300/200"},
    { "id": 10, "url": "http://unsplash.it/290/200"},
    { "id": 11, "url": "http://unsplash.it/350/200"},
    { "id": 1, "url": "http://unsplash.it/320/200"},
    { "id": 2, "url": "http://unsplash.it/300/200"},
    { "id": 3, "url": "http://unsplash.it/290/200"},
    { "id": 4, "url": "http://unsplash.it/350/200"},
    { "id": 5, "url": "http://unsplash.it/380/200"},
    { "id": 6, "url": "http://unsplash.it/360/200"},
    { "id": 7, "url": "http://unsplash.it/380/200"},
    { "id": 8, "url": "http://unsplash.it/320/200"},
    { "id": 9, "url": "http://unsplash.it/300/200"},
    { "id": 10, "url": "http://unsplash.it/290/200"},
    { "id": 11, "url": "http://unsplash.it/350/200"},
    { "id": 1, "url": "http://unsplash.it/320/200"},
    { "id": 2, "url": "http://unsplash.it/300/200"},
    { "id": 3, "url": "http://unsplash.it/290/200"},
    { "id": 4, "url": "http://unsplash.it/350/200"},
    { "id": 5, "url": "http://unsplash.it/380/200"},
    { "id": 6, "url": "http://unsplash.it/360/200"},
    { "id": 7, "url": "http://unsplash.it/380/200"},
    { "id": 8, "url": "http://unsplash.it/320/200"},
    { "id": 9, "url": "http://unsplash.it/300/200"},
    { "id": 10, "url": "http://unsplash.it/290/200"},
    { "id": 11, "url": "http://unsplash.it/350/200"}
]

@app.route("/")
def index():
    """Welcome page."""
    
    # movies = Movie.query.order_by('title').all()
    return render_template("welcome.html", images=IMAGES)

@app.route("/asanas")
def image_list():
    """Return homepage."""
    
    return render_template("homepage.html", images=IMAGES)

# @app.route("/movies")
#     def movie_list():
#         """Show list of movies."""

#         movies = Movie.query.order_by('title').all()
#         return render_template("movie_list.html", movies=movies)

@app.route("/add-to-favorites", methods=["POST"])
def add_to_favorites():

    photo_id = request.form.get("id")

    # put this in a "favorites" table?

    return jsonify(status="success", id=photo_id)


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")


# @app.route('/register', methods=['POST'])
# def register_process():
#     """Process registration."""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]
#     age = int(request.form["age"])
#     zipcode = request.form["zipcode"]

#     new_user = User(email=email, password=password, age=age, zipcode=zipcode)

#     db.session.add(new_user)
#     db.session.commit()

#     flash("User %s added." % email)
#     return redirect("/users/%s" % new_user.user_id)


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


# @app.route('/login', methods=['POST'])
# def login_process():
#     """Process login."""

#     # Get form variables
#     email = request.form["email"]
#     password = request.form["password"]

#     user = User.query.filter_by(email=email).first()

#     if not user:
#         flash("No such user")
#         return redirect("/login")

#     if user.password != password:
#         flash("Incorrect password")
#         return redirect("/login")

#     session["user_id"] = user.user_id

#     flash("Logged in")
#     return redirect("/users/%s" % user.user_id)


# @app.route('/logout')
# def logout():
#     """Log out."""

#     del session["user_id"]
#     flash("Logged Out.")
#     return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)

    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()