from flask import Flask, jsonify
import mysql.connector
from termcolor import cprint

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': '12345678',
    'database': 'school'
}

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students;")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(results)
    except mysql.connector.Error as err:
        return f"Database error: {err}"

if __name__ == '__main__':
    cprint("Starting Flask app on http://0.0.0.0:5000", "cyan")
    app.run(host='0.0.0.0', port=5000)

