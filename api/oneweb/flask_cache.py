from flask_caching import Cache


class FlaskCache:

    cache_from_flask = None

    @staticmethod
    def get_cache():
        if FlaskCache.cache_from_flask is None:
            FlaskCache.cache_from_flask = Cache()
            return FlaskCache.cache_from_flask
        else:
            return FlaskCache.cache_from_flask

    @staticmethod
    def clear_cache():
        if FlaskCache.cache_from_flask is not None and FlaskCache.cache_from_flask:
            FlaskCache.cache_from_flask.clear()