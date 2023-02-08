from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import psycopg2
from starlette.responses import RedirectResponse, HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Database:
    @staticmethod
    def insert_to_db(name: str, price: float) -> bool:
        with psycopg2.connect(user="postgres", password="Dias15",
                              host="127.0.0.1", port="5432", dbname="currencies") as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
                status = False
                try:
                    cursor.execute("INSERT INTO currencies(name, price)" f"VALUES('{name}', '{price}')")
                except Exception as error:
                    print("Error", error)
                    connection.rollback()
                else:
                    connection.commit()
                    status = True
                finally:
                    return status

    @staticmethod
    def delete_from_db(title: str) -> bool:
        with psycopg2.connect(user="postgres", password="Dias15",
                              host="127.0.0.1", port="5432", dbname="currencies") as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
                status = False
                try:
                    cursor.execute(f"DELETE FROM currencies WHERE name='{title}'")
                except Exception as error:
                    print("error", error)
                    connection.rollback()
                else:
                    connection.commit()
                    status = True
                finally:
                    return status

    @staticmethod
    def update(title: str, price: float) -> bool:
        with psycopg2.connect(user="postgres", password="Dias15",
                              host="127.0.0.1", port="5432", dbname="currencies") as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
                status = False
                try:
                    cursor.execute(f"UPDATE currencies SET name='{title}', price='{price}")
                except Exception as error:
                    print("error", error)
                    connection.rollback()
                else:
                    connection.commit()
                    status = True
                finally:
                    return status


@app.get("/")
async def curr(request: Request):
    with psycopg2.connect(user="postgres", password="Dias15",
                          host="127.0.0.1", port="5432", dbname="currencies") as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM currencies")
            rows = cursor.fetchall()
    arr_dicts = [
        {
            "name": row[1], "price": row[2]
        } for row in rows
    ]
    return templates.TemplateResponse("home.html", {"request": request, "arr_curr": arr_dicts})


# uvicorn main:app --reload
@app.post("/add/")
async def create_val(request: Request):
    form = await request.form()
    name = form.get("name")
    price = form.get("price")
    Database.insert_to_db(name=name, price=price)
    return RedirectResponse("/", status_code=303)


@app.get("/delete/{title}", response_class=HTMLResponse)
async def delete_currence(request: Request, title: str):
    try:
        res = Database.delete_from_db(title=title)
        if res:
            return RedirectResponse("/", status_code=303)
        else:
            raise Exception("Failed to delete record from database")
    except Exception as e:
        print(f"Error deleting record from database: {e}")
        raise e

### i dont realize update method