from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)

# CONNECT TO DB
# SQLite database for development
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
# Switch to PostgreSQL for deployment - this will use sqlite database if run locally
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///blog.db")


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(600), nullable=False)
    img_url = db.Column(db.String(600), nullable=False)
    link = db.Column(db.String(600), nullable=False)

# db.create_all()


# pass current year to all routes for footer
current_year = datetime.now().year


@app.route('/')
def home():
    return render_template("index.html", current_year=current_year)


@app.route('/portfolio')
def portfolio():
    projects = Project.query.all()
    return render_template("portfolio.html", current_year=current_year, all_projects=projects)


if __name__ == "__main__":
    app.run(debug=True)

