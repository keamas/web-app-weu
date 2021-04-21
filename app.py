from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! App Service 1 East US"
