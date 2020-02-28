from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


app = Flask(__name__)
api = Api(app)


@app.route("/")
def main():
	return "Welcome"


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8071, debug=True)
