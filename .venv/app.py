import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import os.path

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "database.db")
#db_path = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_choreos(n_of_m):
    conn = get_db_connection()
    chor = conn.execute('SELECT * FROM gmedium WHERE members=?',
                        (n_of_m,)).fetchall()
    conn.close()
    if chor is None:
        abort(404)
    return chor

app = Flask(__name__)
app.config['SECRET_KEY'] = '987654321'

@app.route('/')
def index():
    conn = get_db_connection()
    choreos = conn.execute('SELECT * FROM gmedium').fetchall()
    conn.close()
    return render_template('index.html', choreos=choreos)

@app.route('/<int:n_of_m>')
def chor(n_of_m):
    chor = get_choreos(n_of_m)
    return render_template('options.html', chor=chor)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        members = request.form['members']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO suggestions (name, members) VALUES (?, ?)',
                         (title, members))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        lvl = request.form['lvl']
        members = request.form['members']
        bg = request.form['bg']
    
    
        if (not lvl) or (not bg) or (not members):
            flash('All fields should be filled!')
        else:
            if bg == 'Boys' or bg == 'boys':
                return redirect(url_for('results', members=members, lvl=lvl, g=2))
            
            elif bg == 'Girls' or bg == 'girls':
                return redirect(url_for('results', members=members, lvl=lvl, g=1))
        
    return render_template('search.html')

@app.route('/results/<members>/<lvl>/<g>')
def results(members, lvl, g):

    g = int(g)
    if g == 1:
        conn = get_db_connection()
        choreos = conn.execute('SELECT name FROM girls WHERE members=? AND lvl=?',
                (members,lvl,)).fetchall()
        conn.close()

        
    elif g == 2:
        conn = get_db_connection()
        choreos = conn.execute('SELECT name FROM boys WHERE members=? AND lvl=?',
                (members,lvl,)).fetchall()
        conn.close()
        #print(choreos[0], flush = True)
    
    return render_template('results.html', choreos=choreos)