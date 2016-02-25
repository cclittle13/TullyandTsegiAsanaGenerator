"""Yoga Asana Generator application Flask server.

Provides web interface for browsing asanas, seeing detail about individual asanas, and a way to
put asanas in a list (with an option for a random choice generator).

Author: Chelsea Little.
"""


from flask import Flask, render_template, redirect, flash, session
import jinja2
# from model import connect_to_db, db, User, Category, Poses

from poses import Pose
app = Flask(__name__)

# Need to use Flask sessioning features

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
    """Return homepage."""

    return render_template("homepage.html")

@app.route("/poses")
def list_poses():
    """Return page showing all the poses for the sequence generator """

    pose_list = Pose.query.all()
    print pose_list
    return render_template("all_poses.html",
                           pose_list=pose_list)


@app.route("/melon/<int:pose_id>")
def show_melon(melon_id):
    """Return page showing the details of a given melon.

    Show all info about a pose. Also, provide a button to pick that pose.
    """

    pose = poses.get_by_id(pose_id)
    print pose 
    return render_template("pose_details.html",
                           display_pose=pose)

# @app.route("/welcome")
# def index():
#     """Welcome page."""
    
#     # movies = Movie.query.order_by('title').all()
#     return render_template("welcome.html", images=IMAGES)

# @app.route("/asanas")
# def image_list():
#     """Return homepage."""
    
#     return render_template("homepage.html", images=IMAGES)


# @app.route("/about")
# def website_info():
#     """Return website info page."""
    
#     return render_template("about.html")


# @app.route("/sequence")
# def returns_sequence():
#     """Return homepage."""
    
#     return render_template("sequence.html", images=IMAGES)

# @app.route("/poses")
# def shows_full_pose_list():
#     """Return list of all poses."""
    
#     return render_template("all_poses.html", images=IMAGES)


# @app.route("/add-to-favorites", methods=["POST"])
# def add_to_favorites():

#     photo_id = request.form.get("id")

#     # put this in a "favorites" table?

#     return jsonify(status="success", id=photo_id)

# @app.route("/melons")
# def list_melons():
#     """Return page showing all the melons ubermelon has to offer"""

#     melon_list = melons.get_all()
#     return render_template("all_melons.html",
#                            melon_list=melon_list)

# @app.route("/melon/<int:melon_id>")
# def show_melon(melon_id):
#     """Return page showing the details of a given melon.

#     Show all info about a melon. Also, provide a button to buy that melon.
#     """

#     melon = melons.get_by_id(melon_id)
#     print melon
#     return render_template("melon_details.html",
#                            display_melon=melon)


# @app.route("/cart")
# def shopping_cart():
#     """Display content of shopping cart."""

#     order_total = 0

#     # Get the cart (or an empty list if there's no cart yet)
#     raw_cart_ids = session.get('cart', [])

#     # We'll use this dictionary to keep track of the melon types
#     # we have in the cart.
#     #
#     # Format: id -> {dictionary-of-melon-info}

#     cart = {}

#     # Loop over the melon IDs in the session cart to build up the
#     # `cart` dictionary

#     for melon_id in raw_cart_ids:

#         if melon_id in cart:
#             cart_info = cart[melon_id]

#         else:
#             melon_type = melons.get_by_id(melon_id)
#             cart_info = cart[melon_id] = {
#                 'common_name': melon_type.common_name,
#                 'unit_cost': melon_type.price,
#                 'qty': 0,
#                 'total_cost': 0,
#             }

#         # increase quantity, update melon-total cost by cost of this melon
#         cart_info['qty'] += 1
#         cart_info['total_cost'] += cart_info['unit_cost']

#         # increase order total by cost of this melon
#         order_total += cart_info['unit_cost']

#     # Get the melon-info dictionaries from our cart
#     cart = cart.values()

#     return render_template("cart.html", cart=cart, order_total=order_total)


# @app.route("/add_to_cart/<int:id>")
# def add_to_cart(id):
#     """Add a melon to cart and redirect to shopping cart page.

#     When a melon is added to the cart, redirect browser to the shopping cart
#     page and display a confirmation message: 'Successfully added to cart'.
#     """

#     # Check if we have a cart in the session dictionary and, if not, add one
#     if 'cart' in session:
#         cart = session['cart']

#     else:
#         cart = session['cart'] = []

#     # Add melon to cart
#     cart.append(id)

#     # Show user success message on next page load
#     flash("Successfully added to cart.")

#     # Redirect to shopping cart page
#     return redirect("/cart")


# @app.route("/login", methods=["GET"])
# def show_login():
#     """Show login form."""

#     return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def process_login():
#     """Log user into site.

#     Find the user's login credentials located in the 'request.form'
#     dictionary, look up the user, and store them in the session.
#     """

#     # TODO: Need to implement this!

#     return "Oops! This needs to be implemented"


# @app.route("/checkout")
# def checkout():
#     """Checkout customer, process payment, and ship melons."""

#     # For now, we'll just provide a warning. Completing this is beyond the
#     # scope of this exercise.

#     flash("Sorry! Checkout will be implemented in a future version.")
#     return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)

    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()