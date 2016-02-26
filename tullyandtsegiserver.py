"""Tully and Tsegi's Asana Generator"""

import random
from random import sample
from random import choice 
from random import shuffle 
# from javascript3demo
from flask import (Flask, render_template, redirect,
                   request, flash, session, jsonify)
import jinja2
from jinja2 import StrictUndefined
# from ratings
# from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_to_db, Pose, User, Category, Image


app = Flask(__name__)

app.secret_key = 'tully-is-the-cutest'

app.jinja_env.undefined = jinja2.StrictUndefined

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

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
    { "id": 39, "name": "Savasana","url": "http://www.pocketyoga.com/images/poses/corpse.png"},
    { "id": 40, "name": "Namaste","url": "http://www.pocketyoga.com/images/poses/easy.png"},
]

@app.route("/")
def index():
    """Welcome page."""
    
    # movies = Movie.query.order_by('title').all()
    return render_template("welcome.html", images=IMAGES)
# from madlibs add hello to user 

@app.route("/hello")
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")
#______________________________________________________________________

@app.route("/posegame")
def pose_game():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("quotes.html")
                           # user=user,
                           # poses=poses)

@app.route('/game')
def show_game_form():
    

    player = request.args.get("person")
    answer = request.args.get("playgame")
    # yogi = request.args.get("yogi")
    # answer = request.args.get("pickposes")

    if answer == "No":
        return render_template("goodbye.html",
                                person=player)
    else:
        return render_template("game.html")

@app.route('/madlib', methods=["GET"])
def show_madlib():
    name = request.form.get("name")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    quantity = request.form.get("quantity")
    theme = request.form.get("theme")

    return render_template("madlib.html",
                            name=name,
                            color=color,
                            noun=noun,
                            adjective=adjective,
                            quantity=quantity,
                            theme=theme)

#__________________________________________________________________

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

@app.route('/posedetails/<int:pose_id>')
def pose_details(pose_id):
    """Shows pose details for each asana"""

    pose_info = Pose.query.get(pose_id)

    print "checking pose_info...", pose_info.common_name, pose_info.category

    return render_template("detail_pose.html", pose=pose_info)

#HTML 
#pose becomes jinja variable



@app.route('/about', methods=['GET'])
def about_page():
    """Site introduction."""

    # rand = random.randrange(0, session.query(Table).count()) 
    # row = session.query(Table)[rand]

    return render_template("about.html")


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

    poses_list = request.args.getlist("poses")
    print poses_list
    
    return render_template("sequence.html",poses_list=poses_list)



@app.route("/random")
def random_list():
    """Return random list."""

    all_poses = ["Child's_Pose", 
    "Downward_Facing_Dog",
    "Ragdoll",
    "Samasthiti",
    "Mountain_Pose",
    "Standing_Forward_Fold",
    "Halfway_Lift",
    "Chaturanga_Dandasana",
    "Upward_Facing_Dog",
    "Table_Pose",
    "Chair_Pose",
    "Warrior_2",
    "Extended_Side_Angle",
    "Reverse_Warrior",
    "Reclined_Bound_Angle_Sit-Ups",
    "Bicycle_Sit-Ups",
    "Boat_Pose", 
    "Cresent_Lunge",
    "Revolved_Cresent_Lunge",
    "Runner's_Lunge",
    "Side_Plank",
    "Prayer_Twist",
    "Frog_Pose",
    "Crow_Pose",
    "Eagle_Pose",
    "Dancer's_Pose",
    "Warrior_1",
    "Triangle_Pose",
    "Prasarita_Pose", 
    "Half_Pigeon",
    "Cobra_Pose",
    "Floor_Bow",
    "Camel_Pose",
    "Bridge_Pose",
    "Reclined_Bound_Angle_Pose", 
    "Seated_Forward_Fold",
    "Happy_Baby_Pose",
    "Supine_Twist",
    "Savasana",
    "Namaste"]


    random_poses = []

    for i in range(40):
        random_poses.append(random.choice(all_poses))

        #sqlalchemy query that returns list of my pose objects, iterate over list and then print


    print random_poses
    return render_template("random_poses.html", random_poses= random_poses)


# random_list(list_length, pose_range)

    # all_poses = ["Child's_Pose", 
    # "Downward_Facing_Dog",
    # "Ragdoll",
    # "Samasthiti",
    # "Mountain_Pose"]
    # Standing_Forward_Fold,
    # Halfway_Lift,
    # Chaturanga_Dandasana,
    # Upward_Facing_Dog,
    # Table_Pose,
    # Chair_Pose,
    # Warrior_2,
    # Extended_Side_Angle,]

    # random.shuffle(all_poses, random.random)

    # return all_poses

    # random.shuffle(x[, random])

    # def myshuffle(ls):
    #     random.shuffle(ls)
    #     return ls


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
#___________________________________________________________________________________
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
    
    new_user = User(email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    flash("User %s added." % email)
    return redirect("/users/%s" % new_user.user_id)


@app.route('/login', methods=['GET'])
def login_form():
    """Show form for user signup."""

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


@app.route("/users/<int:user_id>")
def user_detail(user_id):
    """Show info about user."""

    user = User.query.get(user_id)
    return render_template("user.html", user=user)





if __name__ == "__main__":


    connect_to_db(app)

    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(debug=True)