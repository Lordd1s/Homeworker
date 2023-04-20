import contextlib

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder="templates", static_url_path='/static', static_folder='static')


class Db:
    @staticmethod
    def select_all(query: str):
        """
        Show all datas on DB (PostgreSQL)!
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
        Insert "Product" to DB (PostgreSQL)!
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
        This method DELETE from Database (inputting PostgreSQL request to delete)
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
    def select_one(query: str):
        """
        This method show one row in PostgreSQL!
        """
        with contextlib.closing(sqlite3.connect('database.db')) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchone()
            row = {
                "id": rows[0],
                "title": rows[1],
                "desc": rows[2],
                "price": rows[3],
                "count": rows[4]
            }
            return row

    @staticmethod
    def update(query: str, upd_data: tuple) -> bool:
        with contextlib.closing(sqlite3.connect('database.db')) as connection:
            cursor = connection.cursor()
            status = False
            try:
                cursor.execute(query)
            except Exception as error:
                print("error", error)
                connection.rollback()
            else:
                connection.commit()
                status = True
            finally:
                return status

@app.route('/')
def hom_page():
    return render_template("home.html")


@app.route('/allgoods', methods=['GET'])
def goods():
    arr = Db.select_all('SELECT id, title, description, price, count FROM products')
    products = [
        {
            "id": x[0],
            "title": x[1],
            "desc": x[2],
            "price": x[3],
            "count": x[4],
        }
        for x in arr
    ]
    return render_template("allgoods.html", arr=products)


@app.route('/capitalize', methods=['GET', 'POST'])
def create_product():
    if request.method == 'GET':
        return render_template("capitalize.html")
    elif request.method == 'POST':
        title = request.form.get("title")
        desc = request.form.get("desc")
        price = request.form.get("price")
        count = request.form.get("count")
        Db.insert_to_db('INSERT INTO products (title, description, price, count) VALUES (?, ?, ?, ?)', (title, desc, price, count))
        return redirect(url_for("goods"))


@app.route('/allgoods/<int:pk>/delete', methods=['GET', 'POST', 'DELETE'])
def product_delete(pk):
    Db.delete_from_db('DELETE FROM products WHERE id=?', pk)
    return redirect(url_for("goods"))


@app.route('/allgoods/<int:pk>/update', methods=['GET', 'POST'])
def prod_upd(pk):
    if request.method == 'GET':
        one_product = Db.select_one('SELECT id, title, description, price, count FROM products')
        return render_template('upd.html', product=one_product)
    elif request.method == 'POST':
        title = request.form.get("title")
        desc = request.form.get("desc")
        price = request.form.get("price")
        count = request.form.get("count")
        query = 'UPDATE posts SET title=?, description=?, price=? count=? WHERE id=?'
        values = (title, desc, price, count, pk)
        Db.update(query=query, upd_data=values)
        return redirect(url_for('goods', pk=pk))


def create_sql():
    with contextlib.closing(sqlite3.connect("database.db")) as conn:
        with conn as cur:
            # cur.execute("CREATE TABLE products(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, price REAL, count REAL)")
            # cur.execute("INSERT INTO products (title, description, price, count) VALUES ('Bananas', 'african bananas', 570.52, 300.2)")
            pass
if __name__ == "__main__":
    app.run(debug=True)
    # create_sql()
