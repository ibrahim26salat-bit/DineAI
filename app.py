from flask import Flask, render_template

app = Flask(__name__)

restaurants = [
    {"name": "Spice Villa", "cuisine": "Indian", "rating": 4.5, "price": "₹500"},
    {"name": "Pizza Hub", "cuisine": "Italian", "rating": 4.2, "price": "₹700"},
    {"name": "Dragon Bowl", "cuisine": "Chinese", "rating": 4.4, "price": "₹600"},
    {"name": "Royal Biryani", "cuisine": "Mughlai", "rating": 4.8, "price": "₹650"},
    {"name": "Green Leaf", "cuisine": "Vegetarian", "rating": 4.6, "price": "₹450"},
    {"name": "Burger Point", "cuisine": "Fast Food", "rating": 4.1, "price": "₹350"}
]

@app.route("/")
def home():
    return render_template("index.html", restaurants=restaurants)

if __name__ == "__main__":
    app.run(debug=True)
