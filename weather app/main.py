# flask --app main --debug run --host=0.0.0.0 --port=8000
import json
import requests
from flask import Flask, render_template, request, redirect, url_for
import bs4

# ЛИБО САЙТ НЕ ДАЕТ ПРАВИЛЬНО ПАРСИТЬ ЛИБО МОЙ КОД ГАВНО!!! НО Я ЗАМЕТИЛ ИЗМЕНЕНИЕ ПОГОДЫ!!! КРЧ idk)

app = Flask(__name__, template_folder="templates", static_url_path='/static', static_folder='static')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


@app.route('/')
def home():
    data_dict = []
    file = requests.get("https://www.gismeteo.kz/weather-kyzylorda-5319/", headers=headers)
    soup = bs4.BeautifulSoup(file.content, "html.parser")
    temp = soup.find("span", class_="unit unit_temperature_c").text
    print(temp)
    dict_1 = {"temp": temp}
    data_dict.append(dict_1)
    with open("templates/db.json", "w") as w_file:
        json.dump(data_dict, w_file)
    with open("templates/db.json", "r") as r_file:
        data_dict = json.load(r_file)
    return render_template("home.html", data_dict=data_dict)


# @app.route('/city/')
# def add_w():
#     return render_template("city.html")


@app.route('/city/', methods=['GET', 'POST'])
def add_w():
    if request.method == "GET":
        return render_template("city.html")
    elif request.method == "POST":
        # Get from html
        name = request.form.get("name")
        data_dict1 = []
        if name == "Astana":
            print("start")
            # Parse the city
            site_1 = requests.get("https://www.gismeteo.kz/weather-astana-5164/", headers=headers)
            soup = bs4.BeautifulSoup(site_1.content, "html.parser")
            print(name)

            # find and get the weather info
            temp1 = soup.find("span", class_="unit unit_temperature_c").text
            dict1 = {"name": temp1, "city": "Astana", "today": "Today"}
            data_dict1.append(dict1)
            print(dict1)

            # write to json
            with open("templates/db2.json", "w") as w_file:
                json.dump(data_dict1, w_file)
        elif name == "Almaty":
            # parse the city 2
            site_2 = requests.get("https://www.gismeteo.kz/weather-almaty-5205/", headers=headers)
            soup = bs4.BeautifulSoup(site_2.content, "html.parser")
            print(name)

            # find and get the weather info
            temp1 = soup.find("span", class_="unit unit_temperature_c").text
            dict2 = {'name': temp1, "city": "Almaty", "today": "Today"}
            data_dict1.append(dict2)
            print(dict2)

            # write to json
            with open("templates/db2.json", "w") as w_file:
                json.dump(data_dict1, w_file)
                print("stop")

        # read from json
        with open("templates/db2.json", "r") as r_file:
            data_ = json.load(r_file)
            print(data_)
        return render_template("home.html", data_=data_)
