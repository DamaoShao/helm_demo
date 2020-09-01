import os

import redis
from flask import Flask
pool = redis.ConnectionPool(host=os.getenv("HOST", "127.0.0.1"),
                            port=os.getenv("PORT", 6379),
                            db=os.getenv("DB", 0),
                            password=os.getenv("PASSWORD", "P@ssw0rd"))
r = redis.StrictRedis(connection_pool=pool)
app = Flask(__name__)


@app.route('/')
def hello():
    r.incr('counter')
    html = "<h1>Hello {name}, Welcome to Helm chart demo 'Counter</h1>"
    return html.format(name=os.getenv("NAME", "world"))


@app.route('/counter')
def counter():
    html = "<h1>Counter: {counter}</h1>"
    return html.format(counter=r.get('counter'))


@app.route('/clear')
def clear():
    r.delete('counter')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv("HTTP_PORT", 8080))