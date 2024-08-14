import json
import os
from datetime import datetime

from api.oneweb.contentful_request import ContentfulRequest
from api.oneweb.oneweb_cache import Cache
from api.oneweb.oneweb_constants import (APPLICATION_JSON,
                                         ENVIRONMENT, SPACE_ID, APP_TOKEN, CACHE_DURATION, INVALIDATION_TOKEN,
                                         ACCESS_CONTROL_ALLOW_ORIGIN, QUERY_TOKEN)
from flask import Blueprint, Response, request


oneweb_api = Blueprint("oneweb_api", __name__, template_folder="oneweb")
environment = os.environ[ENVIRONMENT]
space_id = os.environ[SPACE_ID]
token = os.environ[APP_TOKEN]
cache_duration = os.environ[CACHE_DURATION]
cache = Cache(cache_duration)
invalidation_token = os.environ[INVALIDATION_TOKEN]
contentful = ContentfulRequest(space_id, environment, token)


@oneweb_api.route('/v1/oneweb/projects')
def projects():
    projects_result = ""
    if cache.is_cache_expired() or not cache.projects:
        response = contentful.get_projects()
        projects_result = response
        cache.cache_time = datetime.now()
        cache.projects = response
    else:
        projects_result = cache.projects
    return Response(json.dumps(projects_result, indent=4),
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)


@oneweb_api.route('/v1/oneweb/homePage')
def get_home_page():
    home_page_result = ""
    if cache.is_cache_expired() or not cache.home_page:
        response = contentful.get_homepage()
        home_page_result = response
        cache.cache_time = datetime.now()
        cache.home_page = response
    else:
        home_page_result = cache.home_page
    return Response(json.dumps(home_page_result, indent=4),
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)


@oneweb_api.route("/v1/oneweb/invalidate")
def invalidate():
    message = ""
    user_invalidation_token = request.args.get(QUERY_TOKEN)
    if user_invalidation_token == invalidation_token:
        cache.projects = []
        cache.experiences = []
        cache.home_page = ""
        message = "Content is successfully invalidated"
    else:
        message = "Missing token header, content isn't invalidated"
    return Response(message,
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)

