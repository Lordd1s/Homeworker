# uvicorn main:app --reload --host=0.0.0.0 --port=8000
# http://127.0.0.1:8000/
import json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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

    @staticmethod
    def add_to_json(path=Path('db', 'file.json')):
        pass


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/all", response_class=HTMLResponse)
async def all_jsons(request: Request):
    db = JsonObj.read_from_json_db()
    obj = [
        {
            "id": item.get("id"),
            "title": item.get("title"),
            "completed": item.get("completed")
        } for item in db
    ]
    return templates.TemplateResponse("all.html", {"request": request, "obj": obj})


@app.get("/addd", response_class=HTMLResponse)
async def create_page(request: Request):
    return templates.TemplateResponse("create.html", context={"request": request})


@app.post("/addd", response_class=HTMLResponse)
async def create_json(request: Request):
    form = await request.form()
    title = form.get("title")
    completed = form.get("completed")
    db = JsonObj.read_from_json_db()
    pk = db[-1]["id"] + 1
    dict1 = {"id": pk, "title": title, "completed": completed}
    db.append(dict1)
    with open("db/file.json", mode="w") as file:
        json.dump(db, file, indent=4)
    return RedirectResponse("/all", status_code=303)
