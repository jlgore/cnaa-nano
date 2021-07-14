from logging import FileHandler, log
from flask import Flask
from flask import jsonify
from flask import request
import logging
import datetime
import os 

app = Flask(__name__)

health_check = 0
metric_check = 0

@app.before_first_request
def before_first_request():
    log_level = logging.DEBUG

    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    
    app.logger.setLevel(log_level)


@app.route("/")
def hello():
    return "Fellow World!"

@app.route("/status")
def status():
    endpoint_name = "status"
    app.logger.info('%s endpoint reached!', endpoint_name)
    app.logger.info('%s', str(datetime.datetime.now()))
    global health_check
    health_check = health_check + 1
    user = request.headers.get('User-Agent')
    response = jsonify(success=True, result="OK - Healthy", user=user, status=200)
    return response

@app.route("/metrics")
def metrics():
    endpoint_name = "metrics"
    app.logger.info('%s endpoint reached! ' + str(datetime.datetime.now()), endpoint_name)
    global metric_check
    metric_check = metric_check + 1
    response = jsonify(success=True, healthcheck = health_check, metriccheck = metric_check)
    return response

if __name__ == "__main__":

    app.run(host='0.0.0.0')
