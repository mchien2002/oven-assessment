from django.core.cache import cache


class RedisClient(object):
    def __init__(self, _patten_key="", value_key=None, timeout=0, _default=None, cache_key=""):
        self._patten_key = _patten_key
        self.value_key = value_key
        self.timeout = timeout
        self._default = _default if _default else {}
        self.cache_key = self.generate_cache_key() if not cache_key else cache_key

    def generate_cache_key(self):
        cache_key = self._patten_key.format(**self.value_key)
        return cache_key

    def set_cache(self, data, timeout=None):
        try:
            if not timeout:
                timeout = self.timeout
            cache.set(self.cache_key, data, timeout)
        except Exception as e:
            return False
        return True

    def clear_cache(self):
        try:
            cache.delete(self.cache_key)
        except Exception as e:
            return False
        return True

    def get_cache(self, _default=None):
        if not _default:
            _default = self._default
        data = _default
        try:
            data = cache.get(self.cache_key, _default)
        except Exception:
            pass
        return data
