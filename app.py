from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Local import
import string_util as su


app = Flask(__name__)
api = Api(app)


'''
    http://localhost:8071/
'''
@app.route("/")
def main():
	return "Welcome"

'''
    http://localhost:8071/reverse

    http://localhost:8071/reverse?content=hello
'''
@app.route("/reverse")
def reverse_string_api():

    content = request.values.get('content')

    print('c : ', content)

    r_content = su.reverse_string(content)

    return r_content

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8071, debug=True)
