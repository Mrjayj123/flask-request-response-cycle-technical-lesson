#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get("Host")
    appname = current_app.name
    return f'''<h1> The Host for this page is {host}</h1>
            <h2> This app is called {appname} </h2>
            <h2> The users path is {g.path}</h2>
            ''', 202

if __name__ == '__main__':
    app.run(port=5555, debug=True)
