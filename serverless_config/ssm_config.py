'''Config backed by AWS SSM'''

import boto3

from .config_base import ConfigBase


class SsmConfig(ConfigBase):
    '''SsmConfig'''

    def __init__(self):
        self.client = boto3.client('ssm')

    def get_str(self, prop_name, default_value=None, **kwargs):
        ''' Get a str property by name.

            Raises ValueError if not found.
        '''
        try:
            response = self.client.get_parameter(
                Name=prop_name,
                **kwargs
            )
            return response['Parameter']['Value']
        except Exception:
            if default_value:
                return default_value
            raise ValueError('Property not found: ' + prop_name)

    def get_int(self, prop_name, default_value=None, **kwargs):
        ''' Get an int property by name.

            Raises ValueError if not found.
            Raises ValueError if not an int.
        '''
        return int(self.get_str(prop_name, default_value, **kwargs))
