# uvicorn main:app --reload --host=0.0.0.0 --port=8000
# http://127.0.0.1:8000/
import json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, Response
import requests
from pathlib import Path

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="templates")


# response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# with open("db/file.json", "w") as file_:
#     json.dump(response, file_, indent=4)


class JsonObj:
    def __init__(self, path):
        self.path = Path(path)

    def read_from_json_db(self):
        with open(self.path, "r") as file:
            result = json.load(file)
            return result

    def write_to_json_db(self, data):
        with open(self.path, mode="w") as file:
            json.dump(data, file, indent=4)

    def add_to_json_db(self, item):
        db = self.read_from_json_db()
        pk = db[-1]["id"] + 1
        item["id"] = pk
        db.append(item)
        self.write_to_json_db(db)

    def update_in_json_db(self, pk, new_item):
        db = self.read_from_json_db()
        for i, item in enumerate(db, start=pk):
            if item["id"] != pk:
                item["id"] = pk - item["id"]
                db[i] = new_item
                self.write_to_json_db(db)
                return True
        return False

    def delete_from_json_db(self, pk):
        db = self.read_from_json_db()
        for i, item in enumerate(db):
            if item["id"] == pk:
                del db[i]
                self.write_to_json_db(db)
                return True
        return False


json_obj = JsonObj("db/file.json")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return template.TemplateResponse("index.html", {"request": request})


@app.get("/all", response_class=HTMLResponse)
async def all_jsons(request: Request):
    db = json_obj.read_from_json_db()
    obj = [
        {
            "id": item.get("id"),
            "title": item.get("title"),
            "completed": item.get("completed")
        } for item in db
    ]
    return template.TemplateResponse("all.html", {"request": request, "obj": obj})


@app.get("/add", response_class=HTMLResponse)
async def create_page(request: Request):
    return template.TemplateResponse("create.html", context={"request": request})


@app.post("/add", response_class=HTMLResponse)
async def create_json(request: Request):
    form = await request.form()
    title = form.get("title")
    completed = form.get("completed")
    if completed == "on":
        completed = True
    else:
        completed = False
    dict1 = {"title": title, "completed": completed}
    json_obj.add_to_json_db(dict1)
    return RedirectResponse("/all", status_code=303)

@app.get("/update/{pk}", response_class=HTMLResponse)
async def update_page(request: Request, pk: int):
    db = json_obj.read_from_json_db()
    post_list = [
        {
            "id": item.get("id"),
            "title": item.get("title"),
            "completed": item.get("completed")
        } for item in db
    ]
    post = post_list[pk - 1]
    return template.TemplateResponse("upd.html", context={"request": request, "post": post})
@app.post("/update/{pk}", response_class=HTMLResponse)
async def update_json(request: Request, pk: int):
    form = await request.form()
    title = form.get("title")
    completed = form.get("completed")
    if completed == "on":
        completed = True
    else:
        completed = False
    new_item = {"id": pk, "title": title, "completed": completed}
    updated = json_obj.update_in_json_db(pk=pk, new_item=new_item)
    if updated:
        return RedirectResponse("/all", status_code=303)
    else:
        return Response(f"Item with ID {pk} not found.", status_code=404)


@app.post("/delete/{pk}", response_class=HTMLResponse)
async def delete_json(request: Request, pk: int):
    deleted = json_obj.delete_from_json_db(pk)
    if deleted:
        return RedirectResponse("/all", status_code=303)
    else:
        return Response(f"Item with ID {pk} not found.", status_code=404)
