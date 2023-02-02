import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
import psycopg2

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# uvicorn main:app --reload
@app.get("/add/")
async def add_(request: Request):
    # print("def started")
    # list1 = []
    # uid = ids
    # f_name = name
    # val = price
    # with open("db.json", "w") as file:
    #     dict1 = {"id": uid, "name": f_name, "price": val}
    #     list1.append(dict1)
    #     json.dump(list1, file)
    #     print("def compleated")
    return templates.TemplateResponse("currencies.html", {"request": request})
    # with psycopg2.connect(user="postgres", password="Dias15",
    #                       host="127.0.0.1", port="5432", dbname="currencies") as connection:
    #     connection.autocommit = False
    #     print("connected")
    #     with connection.cursor() as cursor:
    #         try:
    #             que = f"""INSERT INTO public.currencies(id, name, price) VALUES ({ids}, {name}, {price}"""
    #             cursor.execute(que)
    #             print("done")
    #         except Exception as error:
    #             print("Error", error)
    #             cursor.rollback()
    #         else:
    #             cursor.commit()
    #             print("committed")
    #
    #         finally:
    #             print("response done")
    #             return templates.TemplateResponse("currencies.html", {"request": request})


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/currencies/")
async def curr(request: Request):
    with psycopg2.connect(user="postgres", password="Dias15",
                          host="127.0.0.1", port="5432", dbname="currencies") as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM public.currencies")
            rows = cursor.fetchall()
    arr_dicts = [
        {
            "id": row[0], "name": row[1], "price": row[2]
        } for row in rows
    ]
    return templates.TemplateResponse("currencies.html", {"request": request, "arr_curr": arr_dicts})
