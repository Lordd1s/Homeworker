# TODO  imports
from tkinter import *
from tkinter import ttk
import psycopg2

# TODO  Tkinters parameters
root = Tk()
root.geometry("300x300")  # window size
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="id").grid(column=0, row=0)
input_1 = Entry(frm)
input_1.grid(column=1, row=0)

ttk.Label(frm, text="title").grid(column=0, row=2)
input_2 = Entry(frm)
input_2.grid(column=1, row=2)

ttk.Label(frm, text="description").grid(column=0, row=3)
input_3 = Entry(frm)
input_3.grid(column=1, row=3)

ttk.Label(frm, text="succes").grid(column=0, row=4) # bool on sql
input_4 = Entry(frm)
input_4.grid(column=1, row=4)

ttk.Label(frm, text="deadline").grid(column=0, row=5)
input_5 = Entry(frm)
input_5.grid(column=1, row=5)

ttk.Label(frm, text="data created").grid(column=0, row=6)
input_6 = Entry(frm)
input_6.grid(column=1, row=6)


# TODO Main Function
def read_to_matrix_and_write_to_sql():
    # TODO  Read Written Data
    dict1 = {"id": int(input_1.get()), "title": str(input_2.get()), "description": str(input_3.get()),
             "succes": str(input_4.get().capitalize()), "deadline": str(input_5.get()),
             "data created": str(input_6.get())}
    print(dict1)
    # TODO  Write to Database
    global connection, cursor
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Dias15",
            host="127.0.0.1",                     # attempt to connect datebase
            port="5432",
            dbname="excels",
        )
        connection.autocommit = False
        cursor = connection.cursor()
        # TODO Write to columns
        stringss = f"""INSERT INTO public.excel(id, title, description, succes, deadline, data_created) VALUES (
        '{int(input_1.get())}', '{str(input_2.get())}', '{str(input_3.get())}', '{str(input_4.get())}', '{str(input_5.get())}', '{str(input_6.get())}') """
        cursor.execute(stringss)
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()


ttk.Button(frm, text="Write", command=read_to_matrix_and_write_to_sql).grid(column=1, row=7)
root.mainloop()   # run the program
