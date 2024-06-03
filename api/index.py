import json
import os
from flask import Response, Flask
from supabase import create_client, Client

app = Flask(__name__)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
Client = create_client(url, key)


@app.route("/v1/glucose")
def get_latest():
    data, count = Client.table('glucose').select('*').order('date', desc=True).limit(1).single().execute()
    data_json = json.dumps(data[1], indent=4)
    return Response(data_json,
                    headers={'Access-Control-Allow-Origin': '*'},
                    mimetype="application/json")


@app.route("/v1/glucose/all")
def get_latest():
    data, count = Client.table('glucose').select('*').order('date', desc=True).limit(10).execute()
    data_json = json.dumps(data[1], indent=4)
    return Response(data_json,
                    headers={'Access-Control-Allow-Origin': '*'},
                    mimetype="application/json")


@app.route("/glucose/<glucose_value>")
def insert_glucose_value(glucose_value):
    Client.table('glucose').insert({"value": glucose_value}).execute()
    return Response("Glucose level successfully inserted",
                    headers={'Access-Control-Allow-Origin': '*'},
                    mimetype="application/json")
