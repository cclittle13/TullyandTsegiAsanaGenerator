"""Tully and Tsegi's Asana Generator"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db, db, User, Movie, Rating


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

# This is the constant k for our kNN algorithm
k_forKNN = 5


WELCOME = [ 
    { "id": 1, "url": "http://unsplash.it/320/200"},
]

#rename, add links to new images, add button for links to seperate pages, 
IMAGES = [
    { "id": 1, "url": "http://unsplash.it/320/200"},
    { "id": 2, "url": "http://unsplash.it/300/200"},
    { "id": 3, "url": "http://unsplash.it/320/200"},
    { "id": 4, "url": "http://unsplash.it/300/200"},
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
    { "id": 12, "url": "http://unsplash.it/360/200"}
]

# @app.route("/")
# def index():
#     """Return homepage."""

#     return render_template("homepage.html", images=IMAGES)

# @app.route("/add-to-favorites", methods=["POST"])
# def add_to_favorites():

#     photo_id = request.form.get("id")

#     # put this in a "favorites" table?

#     return jsonify(status="success", id=photo_id)



@app.route('/')
def index():
    """Return welcome page."""

    return render_template("welcome.html", welcome=WELCOME)

@app.route('/asanas')
def asana_list():
    """Homepage of all pose choices and pics"""

    return render_template("homepage.html", images=IMAGES)

@app.route('/about', methods=['GET'])
def about_page():
    """Site introduction."""

    return render_template("about.html")


@app.route('/add-to-sequence', methods=['POST'])
def add_to_sequence():
    """Adds favored poses to db table and highlighted heart red"""

    photo_id = request.form.get("id")

    # put this in a "favorites" table?

    return jsonify(status="success", id=photo_id)


@app.route('/asanas')
def asana_list():
    """Show list of asanas."""

    Asana = Asana.query.order_by('pose').all()
    return render_template("asana_list.html", poses=poses)


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]
    age = int(request.form["age"])
    zipcode = request.form["zipcode"]

    new_user = User(email=email, password=password, age=age, zipcode=zipcode)

    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % email)
    return redirect("/users/%s" % new_user.user_id)


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect("/users/%s" % user.user_id)


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


# @app.route("/users/<int:user_id>")
# def user_detail(user_id):
#     """Show info about user."""

#     user = User.query.get(user_id)
#     return render_template("user.html", user=user)

@app.route("/asanas")
def asana_list():
    """Show list of asanas."""

    Asana = Asana.query.order_by('pose').all()
    return render_template("asana_list.html", poses=poses)

# @app.route("/movies")
# def movie_list():
#     """Show list of movies."""

#     movies = Movie.query.order_by('title').all()
#     return render_template("movie_list.html", movies=movies)


# @app.route("/movies/<int:movie_id>", methods=['GET'])
# def movie_detail(movie_id):
#     """Show info about movie.

#     If a user is logged in, let them add/edit a rating.
#     """
#     print "made it here"

#     movie = Movie.query.get(movie_id)

#     user_id = session.get("user_id")

#     if user_id:
#         user_rating = Rating.query.filter_by(
#             movie_id=movie_id, user_id=user_id).first()

#     else:
#         user_rating = None


    if __name__ == "__main__":
        app.run(debug=True)