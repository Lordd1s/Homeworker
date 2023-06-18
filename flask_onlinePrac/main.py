import requests
import os
import json
from flask import render_template, request, redirect, url_for, Flask

app = Flask(__name__, template_folder="templates", static_url_path='/static', static_folder='static')

@app.route('/')
def home():
    return render_template(template_name_or_list="home.html")


@app.route('/get_json', methods=["GET"])
def get_json():
    if os.path.exists("temp/file.json"):
        with open("temp/file.json", mode="r") as f:
            exist_file_js = json.load(f) #return [ { } ]
            return render_template(template_name_or_list="list_of_json.html", datas=exist_file_js)

    response = requests.get(url="https://jsonplaceholder.typicode.com/posts").json()
    with open("temp/file.json", mode="w") as file:
        new_file_js = json.dump(response, file)  #return [ { } ]
        return render_template(template_name_or_list="list_of_json.html", datas=new_file_js)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)