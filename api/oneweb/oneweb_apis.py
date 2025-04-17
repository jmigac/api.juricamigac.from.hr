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
cache_duration = int(os.environ[CACHE_DURATION])
flaskCache = cache_from_flask.FlaskCache.get_cache()
invalidation_token = os.environ[INVALIDATION_TOKEN]
response_limit = os.environ[RESPONSE_LIMIT]
homepage_id = os.environ[HOMEPAGE_ID]
contentful = ContentfulRequest(space_id=space_id,
                               environment=environment,
                               token=token,
                               response_limit=response_limit,
                               homepage_id=homepage_id,
                               locale="en-US")


def make_cache_key():
    derivative_name = "homepage"
    locale = get_locale()
    derivative_name = derivative_name + "_locale-" + locale
    return derivative_name


@oneweb_api.route('/v1/oneweb/homePage/robots.txt')
@flaskCache.cached(timeout=cache_duration, make_cache_key="robots.txt")
def get_robots_txt():
    home_page = contentful.get_robots_txt()
    response = Response(json.dumps(home_page, indent=4),
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'Vercel-CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400'},
                    mimetype=APPLICATION_JSON)
    return CachedResponse(response=response, timeout=cache_duration)


@oneweb_api.route('/v1/oneweb/homePage')
@flaskCache.cached(timeout=cache_duration, make_cache_key=make_cache_key)
def get_home_page():
    locale = get_locale()
    home_page = contentful.get_homepage(locale=locale)
    response = Response(json.dumps(home_page, indent=4),
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'Vercel-CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400'},
                    mimetype=APPLICATION_JSON)
    return CachedResponse(response = response, timeout=cache_duration)


@oneweb_api.route('/v1/oneweb/projects')
@flaskCache.cached(timeout=cache_duration, make_cache_key="projects")
def get_projects():
    projects = contentful.get_projects()
    response = Response(json.dumps(projects, indent=4),
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'Vercel-CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400'},
                    mimetype=APPLICATION_JSON)
    return CachedResponse(response=response, timeout=cache_duration)


@oneweb_api.route('/v1/oneweb/experiences')
@flaskCache.cached(timeout=cache_duration, make_cache_key="experiences")
def get_experiences():
    experiences = contentful.get_experiences()
    response = Response(json.dumps(experiences, indent=4),
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'Vercel-CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400'},
                    mimetype=APPLICATION_JSON)
    return CachedResponse(response=response, timeout=cache_duration)


@oneweb_api.route('/v1/oneweb/expertises')
@flaskCache.cached(timeout=cache_duration, make_cache_key="expertises")
def get_expertises():
    expertises = contentful.get_expertises()
    response = Response(json.dumps(expertises, indent=4),
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'Vercel-CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400'},
                    mimetype=APPLICATION_JSON)
    return CachedResponse(response=response, timeout=cache_duration)


@oneweb_api.route('/v1/oneweb/footer')
@flaskCache.cached(timeout=cache_duration, make_cache_key="footer")
def get_footer():
    footer = contentful.get_footer()
    response = Response(json.dumps(footer, indent=4),
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'Vercel-CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400'},
                    mimetype=APPLICATION_JSON)
    return CachedResponse(response=response, timeout=cache_duration)


@oneweb_api.route('/v1/oneweb/aboutMe')
@flaskCache.cached(timeout=cache_duration, make_cache_key="aboutMe")
def get_about_me():
    about_me = contentful.get_about_me()
    response = Response(json.dumps(about_me, indent=4),
                    headers={'Access-Control-Allow-Origin': '*',
                             'Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400',
                             'Vercel-CDN-Cache-Control': 'max-age=3600, stale-while-revalidate=86400'},
                    mimetype=APPLICATION_JSON)
    return CachedResponse(response=response, timeout=cache_duration)


@oneweb_api.route('/v1/oneweb/teaser')
@flaskCache.cached(timeout=cache_duration, make_cache_key="teaser")
def get_teaser():
    teaser = contentful.get_teaser()
    response = Response(json.dumps(teaser, indent=4),
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
        cache_from_flask.FlaskCache.clear_cache()
        message = "Content is successfully invalidated"
    else:
        message = "Missing token header, content isn't invalidated"
    return Response(message,
                    headers=ACCESS_CONTROL_ALLOW_ORIGIN,
                    mimetype=APPLICATION_JSON)


def get_locale():
    locale_param = request.args.get('locale')
    return locale_param if locale_param else 'en-US'
