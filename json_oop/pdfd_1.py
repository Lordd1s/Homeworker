import psycopg2


class UpdateMethod:
    def __init__(self, user: str, password: str, host: str, port: str, dbname: str, query: str):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self.query = query

    def update_rows(self):
        with psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port,
                              dbname=self.dbname) as connection:
            connection.autocommit = False
            with connection.cursor() as cursor:
                try:
                    cursor.execute(self.query)
                except Exception as error:
                    connection.rollback()
                    print(error)
                else:
                    connection.commit()

    @staticmethod
    def delete_rows(query: str):
        with psycopg2.connect(user="pgs_user", password="Dias15", host="127.0.0.1", port="5432",
                              dbname="pgs_db") as connection:
            with connection.cursor() as cursor:
                connection.autocommit = False
                try:
                    cursor.execute(query)
                except Exception as error:
                    connection.rollback()
                    print(error)
                else:
                    connection.commit()


class Show(UpdateMethod):
    def show_tables(self):
        with psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port,
                              dbname=self.dbname) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.excel")
                tables = cursor.fetchall()
                return tables


# show = Show(user="pgs_user", password="Dias15", host="127.0.0.1", port="5432",dbname="pgs_db", query="SELECT * FROM public.excel")


update = UpdateMethod(user="pgs_user", password="Dias15", host="127.0.0.1", port="5432", dbname="pgs_db",
                    query="UPDATE public.excel SET title=CONCAT(title, id::text) WHERE id % 2 = 0;") # запросом облажался несколько раз! Из за этого в Title в конце бешенные цифры)

# update.update_rows()


show = UpdateMethod.delete_rows("DELETE FROM public.excel WHERE id  % 2 = 1 ")

