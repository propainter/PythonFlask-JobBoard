from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

IndexTemplate = 'index.html'

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

PATH = 'db/jobs.sqlite'
def open_connection():
    connection = getattr(g, '_connection', None)
    if connection  == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection
def execute_sql(sql, values, commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit ==True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchAll()
    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(execption):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

