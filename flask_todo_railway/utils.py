import contextlib
import sqlite3


def crte_db():
    with contextlib.closing(sqlite3.connect('databases/database.db')) as connection:
        cursor = connection.cursor()
        cursor.execute('''
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
''')


class Db:
    @staticmethod
    def select(query: str):
        """
        Show data(s) in the DB (SQLite3)!
        """
        with contextlib.closing(sqlite3.connect('databases/database.db')) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows is None:
                raise Exception("No products found")
            return rows

    @staticmethod
    def insert_to_db(query: str, value: tuple) -> bool:
        """
        Insert "Product" to DB (SQLite3)!
        """
        with contextlib.closing(sqlite3.connect('databases/database.db')) as connection:
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
        with contextlib.closing(sqlite3.connect('databases/database.db')) as connection:
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
    def select_one(query: str, one_val: tuple):
        """
        This method show one row in SQLite3!
        """
        with contextlib.closing(sqlite3.connect('databases/database.db')) as connection:
            cursor = connection.cursor()
            cursor.execute(query, one_val)
            rows = cursor.fetchone()
            return rows

    @staticmethod
    def update(query: str, upd_data: tuple) -> bool:
        with contextlib.closing(sqlite3.connect('databases/database.db')) as connection:
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


if __name__ == '__main__':
    crte_db()
