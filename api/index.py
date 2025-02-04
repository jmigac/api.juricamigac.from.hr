from flask import Flask, render_template
from api.glucose.glucose_apis import glucose_api
from api.oneweb.flask_cache import FlaskCache
from api.oneweb.oneweb_apis import oneweb_api

app = Flask(__name__)
cache = FlaskCache.get_cache()
cache.init_app(app, config={'CACHE_TYPE': 'SimpleCache'})
app.register_blueprint(glucose_api)
app.register_blueprint(oneweb_api)
app.static_folder = "static"


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
