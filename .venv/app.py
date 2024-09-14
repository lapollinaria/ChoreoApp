import sqlite3
from flask import Flask, render_template
import os.path

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "database.db")
#db_path = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    choreos = conn.execute('SELECT * FROM gmedium').fetchall()
    conn.close()
    return render_template('index.html', choreos=choreos)