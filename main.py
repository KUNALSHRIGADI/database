from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafes(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    cafe_name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    banner_img_url = db.Column(db.String(500), nullable=False)


db.create_all()


@app.route('/')
def home():
    post = Cafes.query.all()
    return render_template("index.html", all_posts=post)


if __name__ == "__main__":
    app.run(debug=True)
