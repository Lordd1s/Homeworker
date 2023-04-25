# uvicorn main:app --reload --host=0.0.0.0 --port=8000
# http://127.0.0.1:8000/
import sqlite3
import contextlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, Response

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="templates")


def create_sql():
    with contextlib.closing(sqlite3.connect("database.db")) as conn:
        with conn as cur:
            # cur.execute( "CREATE TABLE posts(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, completed
            # Boolean)")
            # cur.execute("INSERT INTO products (title, description, price, count) VALUES ('Bananas',
            # 'african bananas', 570.52, 300.2)")
            pass

class Db:
    @staticmethod
    def select_all(query: str):
        """
        Show all datas on DB (SQLite3)!
        """
        with contextlib.closing(sqlite3.connect('database.db')) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows is None:
                raise Exception("Not have products")
            return rows

    @staticmethod
    def insert_to_db(query: str, value: tuple) -> bool:
        """
        Insert "Product" to DB (SQLite3)!
        """
        with contextlib.closing(sqlite3.connect('database.db')) as connection:
            cursor = connection.cursor()
            status = False
            try:
                cursor.execute(query, value)
            except Exception as error:
                print("error", error)
                connection.rollback()
            else:
                connection.commit()
                status = True
            finally:
                return status

    @staticmethod
    def delete_from_db(query: str, pk: int) -> bool:
        """
        This method DELETE from Database (inputting SQLite3 request to delete)
        """
        with contextlib.closing(sqlite3.connect('database.db')) as connection:
            cursor = connection.cursor()
            status = False
            try:
                cursor.execute(query, (pk,))
            except Exception as error:
                print("error", error)
                connection.rollback()
            else:
                connection.commit()
                status = True
            finally:
                return status

    @staticmethod
    def select_one(query: str, val: tuple = None):
        """
        This method show one row in SQLite3!
        """
        with contextlib.closing(sqlite3.connect('database.db')) as connection:
            cursor = connection.cursor()
            cursor.execute(query, val)
            rows = cursor.fetchone()
            row = {
                "id": rows[0],
                "title": rows[1],
                "completed": rows[2]
            }
            return row

    @staticmethod
    def update(query: str, upd_data: tuple) -> bool:
        with contextlib.closing(sqlite3.connect('database.db')) as connection:
            cursor = connection.cursor()
            status = False
            try:
                cursor.execute(query, upd_data)
            except Exception as error:
                print("error", error)
                connection.rollback()
            else:
                connection.commit()
                status = True
            finally:
                return status


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return template.TemplateResponse("index.html", {"request": request})


@app.get("/all", response_class=HTMLResponse)
async def all_jsons(request: Request):
    db = Db.select_all('SELECT id, title, completed FROM posts')
    obj = [
        {
            "id": item[0],
            "title": item[1],
            "completed": item[2]
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
    Db.insert_to_db('INSERT INTO posts (title, completed) VALUES (?, ?)', (title, completed))
    return RedirectResponse("/all", status_code=303)


@app.get("/update/{pk}", response_class=HTMLResponse)
async def update_page(request: Request, pk: int):
    db = Db.select_one('SELECT id, title, completed FROM posts WHERE id=?', (pk,))
    print(db)
    return template.TemplateResponse("upd.html", context={"request": request, "post": db})


@app.post("/update/{pk}", response_class=HTMLResponse)
async def update_json(request: Request, pk: int):
    form = await request.form()
    title = form.get("title")
    completed = form.get("completed")
    if completed == "on":
        completed = True
    else:
        completed = False
    query = 'UPDATE posts SET title=?, completed=? WHERE id=?'
    values = (title, completed, pk)
    Db.update(query=query, upd_data=values)
    return RedirectResponse("/all", status_code=303)


@app.post("/delete/{pk}", response_class=HTMLResponse)
async def delete_json(request: Request, pk: int):
    Db.delete_from_db('DELETE FROM posts WHERE id=?', pk)
    return RedirectResponse("/all", status_code=303)


if __name__ == "__main__":
    # create_sql()
    pass
