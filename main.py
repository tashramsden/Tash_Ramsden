from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import datetime
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)

# pass current year to all routes for footer
current_year = datetime.now().year


@app.route('/')
def home():
    return render_template("index.html", current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
