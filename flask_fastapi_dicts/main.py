from flask import Flask, render_template
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = Flask(__name__, template_folder="templates")
appp = FastAPI()
templates = Jinja2Templates(directory="templates")


response = requests.get(url="https://jsonplaceholder.typicode.com/posts").json()


@app.route("/")
def index():
    return render_template("index.html", contexts=response)


@appp.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", context=response)


if __name__ == "__main__":
    # TODO fastapi
    # uvicorn main:app --reload --host=0.0.0.0 --port=8000
    # http://127.0.0.1:8000/

    # TODO flask
    # flask --app main run --debug --host=0.0.0.0
    app.run(debug=True)


    pass