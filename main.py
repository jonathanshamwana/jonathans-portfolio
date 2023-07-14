from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project-photos/<file_paths>")
def see_photos(file_paths):
    paths = file_paths.split(',')
    paths = [path.strip("'") for path in paths]
    return render_template("photos.html", paths=paths)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
