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
    return render_template("posts.html", data_dict=data_dict)


@app.route('/addpost/', methods=['GET', 'POST'])
def post_create():
    if request.method == "GET":
        return render_template("addpost.html")
    elif request.method == "POST":
        title = str(request.form.get("title"))
        desc = str(request.form.get("desc"))
        with open("templates/db.json", "r") as file:
            data_list = list(json.load(file))
            if data_list and "pk" in data_list[-1]:
                ids = data_list[-1]["pk"] + 1
            else:
                ids = 1
            dict1 = {"pk": ids, "title": title.capitalize(), "description": desc.capitalize()}
            if dict1["title"] and dict1["description"] == "":
                dict1["title"] = "Empty"
                dict1["description"] = "Empty"
            else:
                data_list.append(dict1)
        with open("templates/db.json", "w") as file:
            json.dump(data_list, file, indent=4)
        return redirect(url_for("posts"))

@app.route('/posts/<int:post_id>/delete/')
def posts_delete(post_id):
    with open("templates/db.json", "r") as file:
        data_dict = list(json.load(file))
        _ = data_dict.pop(post_id - 1)
    with open("templates/db.json", "w") as file:
        json.dump(data_dict, file)
    return redirect(url_for("posts"))


@app.route('/updatepost/<int:pk>/', methods=['GET', 'POST'])
def post_update(pk):
    if request.method == "GET":
        with open("templates/db.json", "r") as file:
            data_list = json.load(file)
            post = next((item for item in data_list if item["pk"] == pk), None)
            if post:
                return render_template("updatepost.html", post=post)
            else:
                return render_template("notfound.html")
    elif request.method == "POST":
        title = str(request.form.get("title"))
        desc = str(request.form.get("desc"))
        with open("templates/db.json", "r") as file:
            data_list = json.load(file)
            for post in data_list:
                if post["pk"] == pk:
                    post["title"] = title.capitalize()
                    post["description"] = desc.capitalize()
                    break
        with open("templates/db.json", "w") as file:
            json.dump(data_list, file, indent=4)
        return redirect(url_for("posts"))



