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
        ''' Get a str property by name.

            Raises ValueError if not found.
        '''
        if prop_name in environ:
            return environ[prop_name]
        elif default_value:
            return default_value
        raise ValueError('Property not found: ' + prop_name)

    def get_int(self, prop_name, default_value=None, **kwargs):
        ''' Get an int property by name.

            Raises ValueError if not found.
            Raises ValueError if not an int.
        '''
        return int(self.get_str(prop_name))
