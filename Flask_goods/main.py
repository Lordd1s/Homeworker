from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, template_folder="templates", static_url_path='/static', static_folder='static')


class Db:
    @staticmethod
    def select_all(query: str):
        """
        Show all datas on DB (PostgreSQL)!
        """
        with psycopg2.connect(user="postgres", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="goods") as connection:
            with connection.cursor() as cursor:
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
        with psycopg2.connect(user="postgres", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="goods") as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
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
    def delete_from_db(query: str, pk: tuple) -> bool:
        """
        This method DELETE from Database (inputting PostgreSQL request to delete)
        """
        with psycopg2.connect(user="postgres", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="goods") as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
                status = False
                try:
                    cursor.execute(query, pk)
                except Exception as error:
                    print("error", error)
                    connection.rollback()
                else:
                    connection.commit()
                    status = True
                finally:
                    return status

    @staticmethod
    def select_one(query: str, one_val: tuple):
        """
        This method show one row in PostgreSQL!
        """
        with psycopg2.connect(user="postgres", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="goods") as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, one_val)
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
        with psycopg2.connect(user="postgres", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="goods") as connection:
            with connection.cursor() as cursor:
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

@app.route('/')
def hom_page():
    return render_template("home.html")


@app.route('/allgoods', methods=['GET'])
def goods():
    arr = Db.select_all('SELECT id, title, description, price, count FROM public.goods')
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
        Db.insert_to_db('INSERT INTO public.goods (title, description, price, count) VALUES (%s, %s, %s, %s)', (title, desc, price, count))
        return redirect(url_for("goods"))


@app.route('/allgoods/<int:pk>/delete', methods=['GET', 'POST', 'DELETE'])
def product_delete(pk):
    Db.delete_from_db('DELETE FROM public.goods WHERE id=%s', (pk,))
    return redirect(url_for("goods"))


@app.route('/allgoods/<int:pk>/update', methods=['GET','POST'])
def prod_upd(pk):
    if request.method == 'GET':
        one_product = Db.select_one('SELECT id, title, description, price, count FROM public.goods WHERE id = %s',
                                    (pk,))
        return render_template('upd.html', product=one_product)
    elif request.method == 'POST':
        title = request.form.get("title")
        desc = request.form.get("desc")
        price = request.form.get("price")
        count = request.form.get("count")
        query = 'UPDATE public.goods SET title = %s, description = %s, price = %s, count = %s WHERE id = %s'
        values = (title, desc, price, count, pk)
        Db.update(query=query, upd_data=values)
        return redirect(url_for('goods'))


if __name__ == "__main__":
    app.run(debug=True)
