import flask
from flask import Flask, request, url_for
from flask_peewee.rest import RestAPI, RestResource
from models.Email import *
from models.Category import *
from models.Form import *

app = Flask(__name__)
api = RestAPI(app)

api.register(Email, UserResource)
api.register(Category)
api.register(Form)

# configure the urls
api.setup()

if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT',5000)),host="0.0.0.0",debug=True)
