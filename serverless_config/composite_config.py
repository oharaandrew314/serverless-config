''' Composite Config.

    Falls back to other configs if a parameter is not found.

    The order of precedence is provided by the constructor.
'''

from .config_base import ConfigBase


class CompositeConfig(ConfigBase):
    '''Composite Config'''

    def __init__(self, *configs):
        '''Pass in as many configs as you want, in order of precedence'''
        self.configs = configs

    def get_str(self, prop_name, default_value=None, **kwargs):
        '''Get the string property by name'''
        for config in self.configs:
            value = config.get_str(prop_name, **kwargs)
            if value:
                return value

        return default_value

    def get_int(self, prop_name, default_value=None, **kwargs):
        ''' Get an int property by name.

            Raises ValueError if not found.
            Raises ValueError if not an int.
        '''
        value = self.get_str(prop_name, default_value, **kwargs)
        return int(value) if value else None
