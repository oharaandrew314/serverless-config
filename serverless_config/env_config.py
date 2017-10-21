'''
    Config that uses the system environment.

    Properties that are set via this config only persist until
    the end of the program.
'''

from os import environ

from .config_base import ConfigBase

class EnvConfig(ConfigBase):
    '''EnvConfig'''

    def get_str(self, prop_name, default_value=None):
        '''Get the str property by name'''
        if prop_name in environ:
            return environ[prop_name]
        elif default_value:
            return default_value
        raise ValueError('Property not found: ' + prop_name)

    def put(self, prop_name, prop_value):
        ''' Set property by name.'''
        environ[prop_name] = str(prop_value)
