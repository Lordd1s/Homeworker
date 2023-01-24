from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__, template_folder="templates", static_url_path='/static', static_folder='static')


# 127.0.0.1:8000
# flask --app main --debug run --host=0.0.0.0 --port=8000

@app.route('/')
def home():
    return render_template("tweet.html")


@app.route('/posts/')
def posts():
    with open("templates/db.json", "r") as r_file:
        data_dict = json.load(r_file)
    return render_template("posts.html", data_dict= data_dict)


@app.route('/addpost/', methods=['GET', 'POST'])
def post_create():
    if request.method == "GET":
        return render_template("addpost.html")
    elif request.method == "POST":
        title = str(request.form.get("title"))
        desc = str(request.form.get("desc"))
        with open("templates/db.json", "r") as file:
            data_dict = list(json.load(file))
            dict1 = {"title": title.capitalize(), "description": desc.capitalize()}
            data_dict.append(dict1)
        with open("templates/db.json", "w") as file:
            json.dump(data_dict, file, indent=4)
        return redirect(url_for("posts"))
