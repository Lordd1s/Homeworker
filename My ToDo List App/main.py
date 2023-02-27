# uvicorn main:app --reload --host=0.0.0.0 --port=8000
# http://127.0.0.1:8000/
import json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import psycopg2
from starlette.responses import RedirectResponse
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# with open("db/file.json", "w") as file_:
#     json.dump(response, file_, indent=4)

class JsonObj:
    @staticmethod
    def read_from_json_db(path=Path('db', 'file.json')):
        with open(path, "r") as file:
            result = json.load(file)
            return result


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    db = JsonObj.read_from_json_db()
    obj = [
        {
            "id": item.get("id"),
            "title": item.get("title"),
            "completed": item.get("completed")
        } for item in db
    ]
    context = {"request": request, "obj": obj}
    return templates.TemplateResponse("home.html", context)
