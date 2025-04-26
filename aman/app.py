from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': '12345678'
}

def get_connection(database=None):
    config = db_config.copy()
    if database:
        config['database'] = database
    return mysql.connector.connect(**config)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/databases')
def list_databases():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES;")
        databases = [db[0] for db in cursor.fetchall()]
        return render_template("databases.html", databases=databases)
    except Exception as e:
        return f"Error: {e}"

@app.route('/create_db', methods=['POST'])
def create_database():
    dbname = request.form['dbname']
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {dbname}")
        conn.commit()
        return redirect(url_for('list_databases'))
    except Exception as e:
        return f"Error: {e}"

@app.route('/create_table', methods=['POST'])
def create_table():
    dbname = request.form['dbname']
    tablename = request.form['tablename']
    try:
        conn = get_connection(dbname)
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE {tablename} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                age INT
            )
        ''')
        conn.commit()
        return redirect(url_for('show_tables', dbname=dbname))
    except Exception as e:
        return f"Error: {e}"

@app.route('/<dbname>/tables')
def show_tables(dbname):
    try:
        conn = get_connection(dbname)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = [table[0] for table in cursor.fetchall()]
        return render_template("tables.html", dbname=dbname, tables=tables)
    except Exception as e:
        return f"Error: {e}"

@app.route('/<dbname>/<tablename>')
def show_table_data(dbname, tablename):
    try:
        conn = get_connection(dbname)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {tablename}")
        rows = cursor.fetchall()
        return render_template("table_data.html", dbname=dbname, tablename=tablename, rows=rows)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

