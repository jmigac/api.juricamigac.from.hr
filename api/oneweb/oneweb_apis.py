import json
import os
from . import flask_cache as cache_from_flask

from flask import Blueprint, Response, request
from flask_caching import CachedResponse

from api.oneweb.contentful_request import ContentfulRequest
from api.oneweb.oneweb_constants import (APPLICATION_JSON,
                                         ENVIRONMENT, SPACE_ID, APP_TOKEN, CACHE_DURATION, INVALIDATION_TOKEN,
                                         ACCESS_CONTROL_ALLOW_ORIGIN, QUERY_TOKEN, RESPONSE_LIMIT, HOMEPAGE_ID)

oneweb_api = Blueprint("oneweb_api", __name__, template_folder="oneweb")
environment = os.environ[ENVIRONMENT]
space_id = os.environ[SPACE_ID]
token = os.environ[APP_TOKEN]
cache_duration = os.environ[CACHE_DURATION]
flaskCache = cache_from_flask.FlaskCache.get_cache()
invalidation_token = os.environ[INVALIDATION_TOKEN]
response_limit = os.environ[RESPONSE_LIMIT]
homepage_id = os.environ[HOMEPAGE_ID]
contentful = ContentfulRequest(space_id=space_id,
                               environment=environment,
                               token=token,
                               response_limit=response_limit,
                               homepage_id=homepage_id)


@oneweb_api.route('/v1/oneweb/homePage')
@flaskCache.cached(timeout=cache_duration)
def get_home_page():
    home_page = contentful.get_homepage()
    response = Response(json.dumps(home_page, indent=4),
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'Vercel-CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400'},
                    mimetype=APPLICATION_JSON)
    return CachedResponse(response=response, timeout=cache_duration)


@oneweb_api.route("/v1/oneweb/invalidate")
def invalidate():
    message = ""
    user_invalidation_token = request.args.get(QUERY_TOKEN)
    if user_invalidation_token == invalidation_token:
        flaskCache.cache.clear()
        message = "Content is successfully invalidated"
    else:
        message = "Missing token header, content isn't invalidated"
    return Response(message,
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)

