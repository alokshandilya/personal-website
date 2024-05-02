from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, kaisa hai?'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)