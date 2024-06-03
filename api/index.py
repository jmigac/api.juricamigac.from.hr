import json
from flask import Response, Flask

app = Flask(__name__)

@app.route('/v1/glucose')
def get_glucose():
    experience_articles = "Glucose is good."
    return Response(json.dumps(experience_articles, indent=4))
