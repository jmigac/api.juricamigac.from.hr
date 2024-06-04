from flask import Response, Flask
from glucose.glucose_apis import glucose_api

app = Flask(__name__)
app.register_blueprint(glucose_api)


@app.route("/")
def index():
    return Response(response="Home Page",
                    headers={'Access-Control-Allow-Origin': '*'},
                    mimetype="application/json")


if __name__ == "__main__":
    app.run()
