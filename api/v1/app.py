#!/usr/bin/python3

"""

Solution for task 3: 

"""
import os
from api.v1.views import app_views
from ..models import storage
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask
from models import storage


app = Flask(__name__)



app.register_blueprint(app_views)



@app.teardown_appcontext

def teardown_thingy(exception=None):

	"""

	this is the teardown method.

	"""

	storage.close()



if __name__ == "__main__":

	host = os.environ.get('HBNB_API_HOST','0.0.0.0')

	port = os.environ.get('HBNB_API_PORT', 5000)

	app.run(host=host, port=port, threaded=True)









