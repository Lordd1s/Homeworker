from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import contextlib


# Create your views here.

def create_sql():
    with contextlib.closing(sqlite3.connect("database.db")) as conn:
        with conn as cur:
            # cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, jaloba TEXT, phone_number REAL)")
            #  cur.execute("INSERT INTO products (name, phone_number, jaloba) VALUES ('dias', 77083562652, 'what to you want?')")
            pass


class BD:

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
            print(rows)
            return rows

    @staticmethod
    def insert_to_db(query: str, value: tuple) -> bool:
        """
        Insert "Product" to DB (SQLITE3)!
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


def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        nick = request.POST.get('nick')
        phone = request.POST.get('phone')
        jaloba = request.POST.get('jaloba')
        if BD.insert_to_db("INSERT INTO products(name, phone_number, jaloba) VALUES (?, ?, ?)", (nick, phone, jaloba)):
            return render(request, "finish.html")
        else:
            return HttpResponse("Something went wrong")


def writes(request):
    query = BD.select_all("SELECT * FROM products")
    context = [
        {"name": x[1],
         "phone": x[2],
         "jaloba": x[3]
         } for x in query
    ]
    return render(request, 'writes.html', {"jaloby": context})


if __name__ == "__main__":
    # create_sql()
    pass
