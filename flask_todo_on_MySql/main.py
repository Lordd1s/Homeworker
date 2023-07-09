from flask import Flask, render_template, request, redirect
from utils import DbMySQL

app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route('/')
def index():
    todo_rows = DbMySQL.select(query="SELECT id, title, completed FROM todos")
    todos = [{'id': row[0], 'title': row[1], 'completed': row[2]} for row in todo_rows]
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo').strip()
    if len(todo) < 3:
        return render_template("404.html")
    print(todo)
    DbMySQL.insert_to_db("INSERT INTO todos (title) VALUES (%s)", (todo,))
    return redirect('/')


@app.route('/complete', methods=['POST'])
def complete_todo():
    todo_id = request.form.get('id')

    completed = DbMySQL.select_one("SELECT completed FROM todos WHERE id = %s", one_val=(todo_id,))
    print(completed)

    if completed[0] == 1:
        DbMySQL.update(query="UPDATE todos SET completed = 0 WHERE id = %s", upd_data=(todo_id,))
        return redirect('/')

    DbMySQL.update(query="UPDATE todos SET completed = 1 WHERE id = %s", upd_data=(todo_id,))

    return redirect('/')


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    DbMySQL.delete_from_db("DELETE FROM todos WHERE id = %s", todo_id)
    return redirect('/')


@app.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    new_title = request.form.get('todo')

    DbMySQL.update("UPDATE todos SET title = %s WHERE id = %s", (new_title, todo_id))

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
