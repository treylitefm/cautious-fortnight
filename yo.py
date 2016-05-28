from flask import Flask, Response, request, json
import time
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/something', methods=['GET', 'POST'])
def something_else():
    return json.jsonify({'omar':'griffin'})

if __name__ == '__main__':
    app.debug = True
    app.run()
