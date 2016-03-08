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
from tullymodel import db, connect_to_db, Pose, User, Category, Image, Sequence

from twilio.rest import TwilioRestClient
import os

app = Flask(__name__)

app.secret_key = 'tully-is-the-cutest'

app.jinja_env.undefined = jinja2.StrictUndefined

# AWESOMENESS = [
#     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
#     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

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
    
    return render_template("welcome.html", images=IMAGES)


# @app.route("/homepage")
# def homepage():
#     """Return homepage."""

#     return render_template("tullyhomepage.html")


@app.route('/about', methods=['GET'])
def about_page():
    """Site introduction."""

    # rand = random.randrange(0, session.query(Table).count()) 
    # row = session.query(Table)[rand]

    return render_template("about.html")


@app.route("/listposes")
def list_poses():
    """Return page showing all the poses for the sequence generator """

    pose_list = poses.get_all()

    return render_template("tullyall_poses.html",
                           pose_list=pose_list)


@app.route('/asanas')
def asana_list():
    """Homepage of all pose choices and pics"""

    poses = Pose.query.all()
    return render_template("homepage.html", poses=poses)


@app.route("/sanskrittranslations")
def sanskrit_list():
    """Show list of all poses with sanskrit."""

    # pose_info = Pose.query.get(pose_id)
    pose_info = Pose.query.all()

    return render_template("sanskrit_list.html", pose_info=pose_info)



@app.route("/fulllistofasanas")
def full_asana_list():
    """Show list of all poses."""

    # pose_info = Pose.query.get(pose_id)
    all_poses = Pose.query.all()
    # print pose_info

    return render_template("full_list_of_asanas.html", all_poses=all_poses)


# @app.route("/contraindications")
# def pregnancy_safe_list():
#     """Show list of all poses safe during pregnancy."""

#     # pose_info = Pose.query.get(pose_id)
#     baby_poses = Pose.query.all()
#     # print pose_info

#     return render_template("contraindications.html", baby_poses=baby_poses)


@app.route('/sanskrit/<int:pose_id>')
def sanskrit(pose_id):
    """Sanskrit translations"""

    pose_info = Pose.query.get(pose_id)

    print "checking pose_info...", pose_info.common_name, pose_info.category

    return render_template("sanskrit.html", pose_info=pose_info)


@app.route('/posedetails/<int:pose_id>')
def pose_details(pose_id):
    """Shows pose details for each asana"""

    pose_info = Pose.query.get(pose_id)

    print "checking pose_info...", pose_info.common_name, pose_info.category

    return render_template("detail_pose.html", pose=pose_info)


@app.route('/pregnancy/<int:pose_id>')
def pregnancy_safe(pose_id):
    """Shows pregnancy details for each asana"""

    pregnancy_info = Pose.query.get(pose_id)

    # print pregnancy_info, pose_id

    print "checking pose_info...", pregnancy_info.pregnancy

    return render_template("baby.html", pose=pregnancy_info)


@app.route("/sequence")
def returns_sequence():
    """Return homepage."""

    # sequence = save_sequence(request.arg.getlist("poses"))
    pose_id_list = request.args.getlist("poses")
    pose_id_str = ",".join(pose_id_list)
    pose_id_list = map(int, pose_id_list)
    poses = Pose.query.filter(Pose.pose_id.in_(pose_id_list)).all()
    print pose_id_str
    return render_template("sequence.html",poses=poses, pose_id_str=pose_id_str)
    # return render_template("sequence.html", sequence=sequence)


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


# @app.route("/add-to-favorites", methods=["POST"])
# def add_to_favorites():

#     photo_id = request.form.get("id")

#     # put this in a "favorites" table?

#     return jsonify(status="success", id=photo_id)

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

    print user.password, password
    print user.password == password
    print type(user.password), type(password)
    print len(user.password), len(password)

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


@app.route("/users/<int:user_id>", methods=['GET', 'POST'])
def user_detail(user_id):
    """Show info about user."""

    if request.method == 'POST':
        poses = request.form["poses"]
        print poses, type(poses)
        seq_name = request.form["seq_name"]
        pose_id_list = map(int, poses.split(","))
        print pose_id_list
        new_sequence = Sequence(user_id=user_id, seq_name=seq_name, full_seq=pose_id_list)
        db.session.add(new_sequence)
        db.session.commit()
    user = User.query.get(user_id)
    sequences_for_user = Sequence.query.filter_by(user_id=user_id).all()
    sequences_dict = {}
    for sequence in sequences_for_user:
        poses = Pose.query.filter(Pose.pose_id.in_(sequence.full_seq)).all()
        sequences_dict[sequence.seq_name] = [pose.common_name for pose in poses]
    print sequences_dict
    return render_template("user.html", user=user, sequences_dict=sequences_dict)


@app.route("/send_message")
def send_message():
    """Send message"""

    send_sms()

    return "Success"
                    

def send_sms():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to="+19256428623", from_="+16502821253", body="POSE OF THE DAY!", media_url="http://www.pocketyoga.com/images/poses/child_traditional.png")

# send_sms()

if __name__ == "__main__":


    connect_to_db(app)

    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(debug=True)