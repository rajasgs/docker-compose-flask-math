from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps


app = Flask(__name__)
api = Api(app)


'''
    http://localhost:8071/
'''
@app.route("/")
def main():
	return "Welcome"

'''
    http://localhost:8071/add

    http://localhost:8071/add?a=2&b=3
'''
@app.route("/add")
def add_api():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    c = a + b

    print('c : ', c)

    return c

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8071, debug=True)
