from flask import Flask
from PageHome import PageHome

app = Flask(__name__)
app.register_blueprint(PageHome)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"