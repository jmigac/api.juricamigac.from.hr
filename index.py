from flask import Response, Flask

app = Flask(__name__)


@app.route("/")
def index():
    return Response(response="Home Page",
                    headers={'Access-Control-Allow-Origin': '*'},
                    mimetype="application/json")

