import json
import os

from flask import Blueprint, Response
from supabase import create_client

glucose_api = Blueprint("glucose_api", __name__, template_folder="glucose")
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
database = create_client(url, key)


@glucose_api.route("/v1/glucose")
def get_latest_glucose_reading():
    data, count = database.table('glucose').select('*').order('date', desc=True).limit(1).single().execute()
    data_json = json.dumps(data[1], indent=4)
    return Response(data_json,
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 's-maxage=300, must-revalidate'},
                    mimetype="application/json")


@glucose_api.route("/v1/glucose/all")
def get_all_glucose_reading():
    data, count = database.table('glucose').select('*').order('date', desc=True).limit(10).execute()
    data_json = json.dumps(data[1], indent=4)
    return Response(data_json,
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 's-maxage=300, must-revalidate'},
                    mimetype="application/json")


@glucose_api.route("/v1/glucose/<glucose_value>")
def insert_glucose_value(glucose_value):
    database.table('glucose').insert({"value": glucose_value}).execute()
    return Response("Glucose level successfully inserted",
                    headers={'Access-Control-Allow-Origin': '*'},
                    mimetype="application/json")
