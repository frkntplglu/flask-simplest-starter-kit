from flask import Flask,jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=itusoruyor user=postgres password=")
cursor = conn.cursor()


@app.route('/')
def index():
    cursor.execute('SELECT * FROM categories')
    records = cursor.fetchall()
    return jsonify(records)

@app.route('/category/<id>')
def category(id):
    cursor.execute('SELECT * FROM categories WHERE id = %s', (id,))
    record = cursor.fetchone()
    return jsonify(record)