# uvicorn main:app --reload --host=0.0.0.0 --port=8000
# http://127.0.0.1:8000/
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import psycopg2
from starlette.responses import RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Product:
    def __init__(self, id_: int, title: str, price: float, type_measure: str):
        self.type_measure = type_measure
        self.price = price
        self.title = title
        self.id_ = id_

    @staticmethod
    def prduct_crte(row: tuple):
        return Product(id_=row[0], title=row[1], price=row[2], type_measure=row[3])

    @staticmethod
    def read_from_db(que="select * from products;") -> list[tuple]:
        with psycopg2.connect(user="fastapi", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="fast") as connection:
            with connection.cursor() as cursor:
                cursor.execute(que)
                rows = cursor.fetchall()
                if rows is None:
                    raise Exception("Not have products")
                return rows

    @staticmethod
    def insert_new_product_todb(title: str, price: float, type_measure: str, ) -> bool:
        if len(title) < 3:
            raise Exception("Product Doesn't exist")
        with psycopg2.connect(user="fastapi", password="Dias15",
                              host="127.0.0.1", port="5432", dbname="fast") as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
                status = False
                try:
                    cursor.execute("insert into products(title, price, type_measure) VALUES"
                                   f"('{title}', '{price}', '{type_measure}');")
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
    rows = Product.read_from_db("SELECT title, price, type_measure FROM products;")
    products = [
        {
            "title": x[0],
            "price": x[1],
            "type_measure": x[2],
        }
        for x in rows
    ]
    context = {"request": request, "products": products}
    return templates.TemplateResponse("all.html", context)


@app.post("/create")
async def create_product(request: Request):
    form = await request.form()

    title = form.get("title")
    price = form.get("price")
    type_measure = form.get("type_measure")
    Product.insert_new_product_todb(
        title=title, price=price, type_measure=type_measure
    )
    return RedirectResponse("/", status_code=303)

# cd C:\Program Files\PostgreSQL\15\bin>
# cmd
# psql -U postgres
# \l
# \d
# CREATE USER pgs_usr WITH PASSWORD '12345Qwerty!';
# CREATE DATABASE pgs_db OWNER pgs_usr;
# \connect pgs_db
# CREATE TABLE public.products ( id serial PRIMARY KEY, title VARCHAR(128) unique NOT NULL, price double precision DEFAULT 0.0, count INT default 0, type_measure VARCHAR(10) DEFAULT 'kg', nomeklatura_id VARCHAR(255) );
# \d
# GRANT ALL PRIVILEGES ON DATABASE pgs_db TO pgs_usr;
# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to pgs_usr;
# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to pgs_usr;
# GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to pgs_usr;

# select * from products;
# insert into products (title, price, count, type_measure, nomeklatura_id) VALUES ('Бананы', '1200.07', '60', 'kg', '3_Бананы');
# insert into products (title, price, count, type_measure, nomeklatura_id) VALUES ('Olives', '3600.00', '7', 'kg', '5_Olive');
# insert into products (title, price, count, type_measure, nomeklatura_id) VALUES ('Ananas', '6000.00', '0', 'kg', '666_Ananas');
# select * from products;

# delete from products where id=1;

# \q
