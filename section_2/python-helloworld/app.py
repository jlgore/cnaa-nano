from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

health_check = 0
metric_check = 0

@app.route("/")
def hello():
    return "Fellow World!"

@app.route("/status")
def status():
    global health_check
    health_check = health_check + 1
    user = request.headers.get('User-Agent')
    response = jsonify(success=True, result="OK - Healthy", user=user, status=200)
    return response

@app.route("/metrics")
def metrics():
    global metric_check
    metric_check = metric_check + 1
    response = jsonify(success=True, healthcheck = health_check, metriccheck = metric_check)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
