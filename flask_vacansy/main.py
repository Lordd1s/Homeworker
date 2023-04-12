from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, template_folder="templates", static_url_path='/static', static_folder='static')


# 127.0.0.1:8000
# flask --app main --debug run --host=0.0.0.0 --port=8000

@app.route('/')
def home_page():
    return render_template("base.html")


@app.route('/vacancies', methods=['GET', 'POST'])
def show_all_vacancy():
    if request.method == 'GET':
        with psycopg2.connect(user="pgs_user", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="pgs_db") as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.vacs")
                rows = cursor.fetchall()
                print(rows)
                if rows is None:
                    return render_template("not_have.html")
                dict1 = [{
                    "title": x[1],
                    "description": x[2],
                    "salary": x[3]
                } for x in rows]
                return render_template("vacancies.html", rows=dict1)
    elif request.method == 'POST':
        search = request.form['search'].strip()
        with psycopg2.connect(user="pgs_user", password="Dias15", host="127.0.0.1", port="5432", dbname="pgs_db") as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT title, description, salary FROM vacs WHERE title LIKE %s;", ('%' + search + '%',))
                rows = cursor.fetchall()
                print(rows)
                if rows is None:
                    return render_template("not_have.html")
                dict1 = [{
                    "title": x[0],
                    "description": x[1],
                    "salary": x[2]
                } for x in rows]
                return render_template("vacancies.html", rows=dict1)



@app.route('/create', methods=['GET', 'POST'])
def create_vac():
    if request.method == 'GET':
        return render_template("create.html")
    elif request.method == 'POST':
        title = request.form['title'].strip()
        desc = request.form['description'].strip()
        salary = request.form['salary'].strip()
        with psycopg2.connect(user="pgs_user", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="pgs_db") as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO vacs(title, description, salary) VALUES (%s, %s, %s)", (title, desc, salary))
                except Exception as error:
                    print(error)
                    connection.rollback()
                else:
                    connection.commit()
                    return redirect(url_for("show_all_vacancy"))




if __name__ == "__main__":
    app.run(debug=True)















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