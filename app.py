
"""
simple python flask application for MLOPS COURSE
"""

##########################################################################
## Imports
##########################################################################

import os

from flask import Flask, request
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify

from prometheus_flask_exporter import PrometheusMetrics

##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Anime Flask App', version='1.0.3')

counter = metrics.counter(
    'by_endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint, 'path': lambda: request.path, 'method':lambda:request.method}
)

##########################################################################
## Routes
##########################################################################

@app.route("/")
@counter
def home():
    return render_template("home.html")

@app.route("/metrics")
def metrics():
    return metrics.generate_latest()

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()