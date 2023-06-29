import contextlib
import sqlite3


class DB:

    @staticmethod
    def select_all(query: str):
        """
        Show all datas on DB (SQLite3)!
        """
        with contextlib.closing(sqlite3.connect('database/database.db')) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows is None:
                raise Exception("Not have proposes")
            return rows

    @staticmethod
    def insert_to_db(query: str, value: tuple) -> bool:
        """
        Insert "Product" to DB (SQLite3)!
        """
        with contextlib.closing(sqlite3.connect('database/database.db')) as connection:
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


if __name__ == "__main__":
    def create_sql():
        with contextlib.closing(sqlite3.connect("database/database.db")) as conn:
            with conn as cur:
                cur.execute(
                    "CREATE TABLE something"
                    "(_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "name TEXT NOT NULL, "
                    "title TEXT NOT NULL, "
                    "description TEXT)"
                )

    # create_sql()