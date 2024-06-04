from flask import Flask, render_template
from api.glucose.glucose_apis import glucose_api

app = Flask(__name__)
app.register_blueprint(glucose_api)
app.static_folder = "static"


@app.route("/")
def index():
    return render_template('index.html')
