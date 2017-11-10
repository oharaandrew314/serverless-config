'''
    Config that uses the system environment.

    Properties that are set via this config only persist until
    the end of the program.
'''

from os import environ

from .config_base import ConfigBase


class EnvConfig(ConfigBase):
    '''EnvConfig'''

    def get_str(self, prop_name, default_value=None, **kwargs):
        ''' Get a str property by name or None'''
        return environ.get(prop_name, default_value)

    def get_int(self, prop_name, default_value=None, **kwargs):
        ''' Get an int property by name or None.
            Raises ValueError if not an int.
        '''
        value = self.get_str(prop_name, default_value, **kwargs)
        return int(value) if value else None
