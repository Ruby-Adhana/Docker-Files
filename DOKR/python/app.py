from flask import Flask
import redis
app = Flask(__name__)
# Connect to Redis container by service name
r = redis.Redis(host='redis', port=6379, db=0)
@app.route('/')
def home():
    visits = r.incr('visits')
    return f"Hello! I have been seen {visits} times."
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

