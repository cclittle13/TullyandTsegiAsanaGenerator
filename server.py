"""Tully and Tsegi's Asana Generator"""


# from javascript3demo
from flask import (Flask, render_template, redirect,
                   request, flash, session, jsonify)
import jinja2
# from jinja2 import StrictUndefined
# from ratings
# from flask import Flask, render_template, request, flash, redirect, session
# from flask_debugtoolbar import DebugToolbarExtension
# from model import connect_to_db, db, User, Movie, Rating


app = Flask(__name__)

app.secret_key = 'tully-is-the-cutest'

app.jinja_env.undefined = jinja2.StrictUndefined

IMAGES = [
    { "id": 1, "name": "Child's Pose", "url": "http://www.pocketyoga.com/images/poses/child_traditional.png"},
    { "id": 2, "name": "Downward Facing Dog", "url": "http://www.pocketyoga.com/images/poses/downward_dog.png"},
    { "id": 3, "name": "Ragdoll", "url": "http://www.pocketyoga.com/images/poses/forward_bend.png"},
    { "id": 4, "name": "Samasthiti", "url": "http://www.pocketyoga.com/images/poses/chair_prayer.png"},
    { "id": 5, "name": "Mountain Pose", "url": "http://www.pocketyoga.com/images/poses/mountain.png"},
    { "id": 6, "name": "Standing Forward Fold", "url": "http://www.pocketyoga.com/images/poses/forward_bend.png"},
    { "id": 7, "name": "Halfway Lift", "url": "http://www.pocketyoga.com/images/poses/forward_bend_half_way.png"},
    { "id": 8, "name": "Chaturanga Dandasana", "url": "http://www.pocketyoga.com/images/poses/chair_prayer.png"},
    { "id": 9, "name": "Upward Facing Dog", "url": "http://www.pocketyoga.com/images/poses/upward_dog.png"},
    { "id": 10, "name": "Table Top Pose", "url": "http://www.pocketyoga.com/images/poses/box_neutral.png"},
    { "id": 11, "name": "Chair Pose", "url": "http://www.pocketyoga.com/images/poses/chair.png"},
    { "id": 12, "name": "Warrior 2", "url": "http://www.pocketyoga.com/images/poses/warrior_II_R.png"},
    { "id": 13, "name": "Extended Side Angle", "url": "http://www.pocketyoga.com/images/poses/warrior_II_forward_arm_forward_R.png"},
    { "id": 14, "name": "Reverse Warrior", "url": "http://www.pocketyoga.com/images/poses/warrior_II_reverse_R.png"},
    { "id": 15, "name": "Reclined Bound Angle Sit-Ups", "url": "http://www.pocketyoga.com/images/poses/supine_bound_angle.png"},
    { "id": 16, "name": "Bicycle Sit-Ups", "url": "http://www.pocketyoga.com/images/poses/wind_removing_R.png"},
    { "id": 17, "name": "Boat Pose", "url": "http://www.pocketyoga.com/images/poses/boat_full.png"},
    { "id": 18, "name": "Cresent Lunge", "url": "http://www.pocketyoga.com/images/poses/lunge_crescent_R.png"},
    { "id": 19, "name": "Revolved Cresent Lunge", "url": "http://www.pocketyoga.com/images/poses/lunge_kneeling_twist_R.png"},
    { "id": 20, "name": "Runner's Lunge", "url": "http://www.pocketyoga.com/images/poses/lunge_R.png"},
    { "id": 21, "name": "Side Plank", "url": "http://www.pocketyoga.com/images/poses/plank_side_L.png"},
    { "id": 22, "name": "Prayer Twist", "url": "http://www.pocketyoga.com/images/poses/chair_twist_R.png"},
    { "id": 23, "name": "Frog Pose", "url": "http://www.pocketyoga.com/images/poses/seated_on_heels_hands_on_mat_opened_knees.png"},
    { "id": 24, "name": "Crow Pose", "url": "http://www.pocketyoga.com/images/poses/crow.png"},
    { "id": 25, "name": "Eagle Pose", "url": "http://www.pocketyoga.com/images/poses/eagle_L.png"},
    { "id": 26, "name": "Dancer's Pose", "url": "http://www.pocketyoga.com/images/poses/lord_of_the_dance_R.png"},
    { "id": 27, "name": "Tree Pose", "url": "http://www.pocketyoga.com/images/poses/tree_L.png"},
    { "id": 28, "name": "Warrior 1", "url": "http://www.pocketyoga.com/images/poses/warrior_I_R.png"},
    { "id": 29, "name": "Triangle Pose", "url": "http://www.pocketyoga.com/images/poses/triangle_forward_R.png"},
    { "id": 30, "name": "Prasarita Pose", "url": "http://www.pocketyoga.com/images/poses/forward_bend_deep.png"},
    { "id": 31, "name": "Half Pigeon", "url": "http://www.pocketyoga.com/images/poses/pigeon_half_R.png"},
    { "id": 32, "name": "Cobra Pose", "url": "http://www.pocketyoga.com/images/poses/cobra.png"},
    { "id": 33, "name": "Floor Bow", "url": "http://www.pocketyoga.com/images/poses/bow.png"},
    { "id": 34, "name": "Camel Pose", "url": "http://www.pocketyoga.com/images/poses/camel.png"},
    { "id": 34, "name": "Bridge Pose", "url": "http://www.pocketyoga.com/images/poses/bridge.png"},
    { "id": 35, "name": "Reclined Bound Angle Pose", "url": "http://www.pocketyoga.com/images/poses/supine_bound_angle.png"},
    { "id": 36, "name": "Seated Forward Fold", "url": "http://www.pocketyoga.com/images/poses/seated_forward_bend.png"},
    { "id": 37, "name": "Happy Baby Pose", "url": "http://www.pocketyoga.com/images/poses/blissful_baby.png"},
    { "id": 38, "name": "Supine Twist", "url": "http://www.pocketyoga.com/images/poses/supine_spinal_twist_R.png"},
    { "id": 39, "name": "Savasana","name": "Supine Twist","url": "http://www.pocketyoga.com/images/poses/corpse.png"},
    { "id": 40, "name": "Namaste","url": "http://www.pocketyoga.com/images/poses/easy.png"},
]

@app.route("/")
def index():
    """Welcome page."""
    
    # movies = Movie.query.order_by('title').all()
    return render_template("welcome.html", images=IMAGES)

@app.route("/homepage")
def homepage():
    """Return homepage."""

    return render_template("tullyhomepage.html")


@app.route("/listposes")
def list_poses():
    """Return page showing all the poses for the sequence generator """

    pose_list = poses.get_all()
    return render_template("tullyall_poses.html",
                           pose_list=pose_list)
# @app.route("/poses")
# def list_poses():
#     """Return page showing all the poses"""

#     melon_list = melons.get_all()
#     return render_template("all_poses.html",
#                            melon_list=melon_list)

@app.route('/asanas')
def asana_list():
    """Homepage of all pose choices and pics"""

    return render_template("homepage.html", images=IMAGES)


    

@app.route('/about', methods=['GET'])
def about_page():
    """Site introduction."""

    return render_template("about.html")

# @app.route("/about")
# def website_info():
#     """Return website info page."""
    
#     return render_template("about.html")

@app.route('/add-to-sequence', methods=['POST'])
def add_to_sequence():
    """Adds favored poses to db table and highlighted heart red"""

    photo_id = request.form.get("id")

    # put this in a "favorites" table?

    return jsonify(status="success", id=photo_id)


# @app.route("/process_login")
# def process_login():

#     username = request.args.get("username")

#     existing_user = User.query.filter(User.username == username).first()
#     if existing_user is None:
#         flash("Username incorrect. Please re-enter")
#         return redirect("/")
#     else:
#         session["user_id"] = existing_user.user_id
#         return redirect("/home")

# @app.route("/home")
# def show_homepage():
#     """Show homepage of logged in user"""

#     user = User.query.get(session["user_id"])


#     return render_template("homepage.html", user=user)

# @app.route("/asanas")
# def image_list():
#     """Return homepage."""
    
#     return render_template("homepage.html", images=IMAGES)


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



@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")


# @app.route("/register", methods=["GET", "POST"])
# def registration_form():
#     """
#     GET - Displays a form for new users to enter login info & connect to Mint
#     POST - adds registration data to DB --> redirect to transaction analysis
#     (or choose to browse challenges --> redirect to challenge browser tool)
#     """

#     if request.method == "POST":

#         # firstname = request.form["firstname"]
#         # lastname = request.form["lastname"]
#         email = request.form["email"]
#         password = request.form["password"]
#         # age = request.form["age"]
#         # zipcode = request.form["zipcode"]

#         if User.query.filter(User.email == email).first():
#             flash("""Hmm...we already have your email account on file.
#                   Please log in.""")
#             return redirect("/login")
#         else:
#             new_user = User(email=email, password=password)
#             db.session.add(new_user)
#             db.session.commit()

#             session["login"] = email
#             # keyring.set_password("system", mint_username, mint_password)

#             flash("Thanks for creating an account!")
#             return redirect("/")

#     return render_template("register_form.html")





if __name__ == "__main__":
    app.run(debug=True)

    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()