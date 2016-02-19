"""Tully and Tsegi's Asana Generator"""


# from javascript3demo
from flask import (Flask, render_template, redirect,
                   request, flash, session, jsonify)
import jinja2
# from ratings
# from flask import Flask, render_template, request, flash, redirect, session
# from flask_debugtoolbar import DebugToolbarExtension
# from model import connect_to_db, db, User, Movie, Rating


app = Flask(__name__)

IMAGES = [
    { "id": 1, "name": "Child's Pose", "url": "http://www.pocketyoga.com/images/poses/child_traditional.png"},
    { "id": 2, "name": "Downward Dog", "url": "http://www.pocketyoga.com/images/poses/downward_dog.png"},
    { "id": 3, "name": "Ragdoll", "url": "http://www.pocketyoga.com/images/poses/forward_bend.png"},
    { "id": 4, "name": "Samasthiti", "url": "http://www.pocketyoga.com/images/poses/chair_prayer.png"},
    { "id": 5, "name": "Mountain Pose", "url": "http://www.pocketyoga.com/images/poses/child_traditional.png"},
    { "id": 6, "name": "Standing Forward Fold", "url": "http://www.pocketyoga.com/images/poses/downward_dog.png"},
    { "id": 7, "name": "Halfway Lift", "url": "http://www.pocketyoga.com/images/poses/forward_bend.png"},
    { "id": 8, "name": "Chaturanga Dandasana", "url": "http://www.pocketyoga.com/images/poses/chair_prayer.png"},
    { "id": 9, "name": "Upward Dog", "url": "http://unsplash.it/380/200"},
    { "id": 10, "name": "Downward Dog", "url": "http://unsplash.it/360/200"},
    { "id": 11, "name": "Chair Pose", "url": "http://unsplash.it/380/200"},
    { "id": 12, "name": "Warrior 2", "url": "http://unsplash.it/320/200"},
    { "id": 13, "name": "Extended Side Angle", "url": "http://unsplash.it/300/200"},
    { "id": 14, "name": "Reverse Warrior", "url": "http://unsplash.it/290/200"},
    { "id": 15, "name": "Reclined Bound Angle Sit-Ups", "url": "http://unsplash.it/350/200"},
    { "id": 16, "name": "Bicycle Sit-Ups", "url": "http://www.pocketyoga.com/images/thumbnailsbig/box_neutral-tnbig.png"},
    { "id": 17, "name": "Boat Pose", "url": "http://unsplash.it/320/200"},
    { "id": 18, "name": "Cresent Lunge", "url": "http://unsplash.it/300/200"},
    { "id": 19, "name": "Revolved Cresent Lunge", "url": "http://unsplash.it/290/200"},
    { "id": 20, "name": "Runner's Lunge", "url": "http://unsplash.it/350/200"},
    { "id": 21, "name": "Side Plank", "url": "http://unsplash.it/380/200"},
    { "id": 22, "name": "Prayer Twist", "url": "http://unsplash.it/360/200"},
    { "id": 23, "name": "Frog Pose", "url": "http://unsplash.it/380/200"},
    { "id": 24, "name": "Crow Pose", "url": "http://unsplash.it/320/200"},
    { "id": 25, "name": "Eagle Pose", "url": "http://unsplash.it/300/200"},
    { "id": 26, "name": "Dancer's Pose", "url": "http://unsplash.it/290/200"},
    { "id": 27, "name": "Tree Pose", "url": "http://unsplash.it/350/200"},
    { "id": 28, "name": "Warrior 1", "url": "http://unsplash.it/320/200"},
    { "id": 29, "name": "Triangle Pose", "url": "http://unsplash.it/300/200"},
    { "id": 30, "name": "Prasarita Pose", "url": "http://unsplash.it/290/200"},
    { "id": 31, "name": "Half Pigeon", "url": "http://unsplash.it/350/200"},
    { "id": 32, "name": "Cobra", "url": "http://unsplash.it/380/200"},
    { "id": 33, "name": "Floor Bow", "url": "http://unsplash.it/360/200"},
    { "id": 34, "name": "Camel Pose", "url": "http://unsplash.it/380/200"},
    { "id": 35, "name": "Reclined Boung Angle Pose", "url": "http://unsplash.it/320/200"},
    { "id": 36, "name": "Seated Forward Fold", "url": "http://unsplash.it/300/200"},
    { "id": 37, "name": "Happy Baby Pose", "url": "http://unsplash.it/290/200"},
    { "id": 38, "name": "Supine Twist", "url": "http://unsplash.it/350/200"},
    { "id": 39, "name": "Savasana","name": "Supine Twist","url": "http://unsplash.it/320/200"},
    { "id": 40, "name": "Namaste","url": "http://unsplash.it/300/200"},
    # { "id": 3, "url": "http://unsplash.it/290/200"},
    # { "id": 4, "url": "http://unsplash.it/350/200"},
    # { "id": 5, "url": "http://unsplash.it/380/200"},
    # { "id": 6, "url": "http://unsplash.it/360/200"},
    # { "id": 7, "url": "http://unsplash.it/380/200"},
    # { "id": 8, "url": "http://unsplash.it/320/200"},
    # { "id": 9, "url": "http://unsplash.it/300/200"},
    # { "id": 10, "url": "http://unsplash.it/290/200"},
    # { "id": 11, "url": "http://unsplash.it/350/200"},
    # { "id": 1, "url": "http://unsplash.it/320/200"},
    # { "id": 2, "url": "http://unsplash.it/300/200"},
    # { "id": 3, "url": "http://unsplash.it/290/200"},
    # { "id": 4, "url": "http://unsplash.it/350/200"},
    # { "id": 5, "url": "http://unsplash.it/380/200"},
    # { "id": 6, "url": "http://unsplash.it/360/200"},
    # { "id": 7, "url": "http://unsplash.it/380/200"},
    # { "id": 8, "url": "http://unsplash.it/320/200"},
    # { "id": 9, "url": "http://unsplash.it/300/200"},
    # { "id": 10, "url": "http://unsplash.it/290/200"},
    # { "id": 11, "url": "http://unsplash.it/350/200"}
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


@app.route("/about")
def website_info():
    """Return website info page."""
    
    return render_template("about.html")


@app.route("/sequence")
def returns_sequence():
    """Return homepage."""
    
    return render_template("sequence.html", images=IMAGES)

@app.route("/poses")
def shows_full_pose_list():
    """Return list of all poses."""
    
    return render_template("pose.html", images=IMAGES)


@app.route("/add-to-favorites", methods=["POST"])
def add_to_favorites():

    photo_id = request.form.get("id")

    # put this in a "favorites" table?

    return jsonify(status="success", id=photo_id)

# @app.route("/add-to-favorites", methods=["POST"])
# def add_to_favorites():

#     photo_id = request.form.get("id")

#     # put this in a "favorites" table?

#     return jsonify(status="success", id=photo_id)

# @app.route('/login', methods=['GET'])
# def login_form():
#     """Show login form."""

#     return render_template("login_form.html")



@app.route("/login", methods=["POST", "GET"])
def login_form():
    """
    GET - displays a form that asks for email and password
    POST - collects that data and authenticates --> redirect to user profile
    """

    if request.method == "POST":
        email = request.form["username_input"]
        password = request.form["password_input"]
        user_object = User.query.filter(User.email == email).first()

        if user_object:
            if user_object.password == password:
                session["login"] = email
                flash("You logged in successfully")
                return redirect("/profile")
            else:
                flash("Incorrect password. Try again.")
                return redirect("/login")
        else:
            flash("""We do not have this email on file.
                Click Register if you would like to create an account.""")
            return redirect("/register")

    return render_template("login_form.html")


@app.route("/logout")
def logout():
    """
    Logout - link removes User from session and redirects to homepage.
    Flashes message confirming that User has logged out.
    """

    session.pop("login")
    flash("You've successfully logged out. Goodbye.")
    return redirect("/")



# @app.route('/register', methods=['GET'])
# def register_form():
#     """Show form for user signup."""

#     return render_template("register_form.html")


@app.route("/register", methods=["GET", "POST"])
def registration_form():
    """
    GET - Displays a form for new users to enter login info & connect to Mint
    POST - adds registration data to DB --> redirect to transaction analysis
    (or choose to browse challenges --> redirect to challenge browser tool)
    """

    if request.method == "POST":

        # firstname = request.form["firstname"]
        # lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        # age = request.form["age"]
        # zipcode = request.form["zipcode"]

        if User.query.filter(User.email == email).first():
            flash("""Hmm...we already have your email account on file.
                  Please log in.""")
            return redirect("/login")
        else:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            session["login"] = email
            # keyring.set_password("system", mint_username, mint_password)

            flash("Thanks for creating an account!")
            return redirect("/")

    return render_template("register_form.html")


# @app.route('/login', methods=['GET'])
# def login_form():
#     """Show login form."""

# @app.route('/login-process', methods=['POST'])
# def process_login():
#     """Handle form submission for login process."""

#     attempted_username = request.form.get('username').strip().lower()
#     attempted_password = request.form.get('password')

#     user = User.query.filter(User.username == attempted_username).first()

#     if (user is None) or not attempted_username:
#         flash("Nonexistent user. Please retry log in.")
#         return redirect('/login')

#     elif attempted_password == user.password:
#         session['user_id'] = user.user_id
#         session['username'] = user.username

#         flash("Successful log in! Welcome {}.".format(user.username))
#         return redirect('/navigation')

#     else:
#         flash("Invalid password.")
#         return redirect('/login')


# @app.route('/signup-process', methods=['POST'])
# def process_signup():
#     """Handle form submission for signup process."""

#     attempted_username = request.form.get('username').strip().lower()
#     attempted_email = request.form.get('email')
#     attempted_password = request.form.get('password')

#     user = User.query.filter(User.username == attempted_username).first()

#     if (user is None) and attempted_username:
#         # User not already existing, and a username was entered
#         user = User(username=attempted_username,
#                     email=attempted_email,
#                     password=attempted_password)
#         db.session.add(user)
#         db.session.commit()

#         flash("Sign up successful! Now log in.")
#         return redirect('/login')

#     else:
#         flash("Invalid sign up attempt.")
#         return redirect('/login')


# @app.route('/logout-process')
# def process_logout():
#     """Handle form submission for logout process."""

#     session.pop('user_id', None)

#     # flash message: logout successs
#     flash("Successful log out. Goodbye!")
#     return redirect('/')


# @app.route('/register', methods=['GET'])
# def register_form():
#     """Show form for user signup."""

#     return render_template("register_form.html")


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