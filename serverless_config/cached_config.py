'''Cached Config'''

from datetime import datetime

from .config_base import ConfigBase


class CachedConfig(ConfigBase):
    '''Cached Config'''

    def __init__(self, config, duration):
        self._config = config
        self._duration = duration
        self._cache = dict()

    def get_str(self, prop_name, default_value=None, **kwargs):
        '''Get the string property by name or None'''
        now = self.now()
        if prop_name not in self._cache or self._cache[prop_name][1] < now:
            print('cache miss')
            value = self._config.get_str(prop_name, default_value, **kwargs)
            self._cache[prop_name] = (value, now + self._duration)

        return self._cache[prop_name][0]

    def get_int(self, prop_name, default_value=None, **kwargs):
        ''' Get an int property by name or None.
            Raises ValueError if not an int.
        '''
        value = self.get_str(prop_name, default_value, **kwargs)
        return int(value) if value else None

    def now(self):
        '''current datetime provider'''
        return datetime.now()

    def clear(self):
        '''Invalidate cache'''
        self._cache.clear()
