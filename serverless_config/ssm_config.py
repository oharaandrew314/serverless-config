'''Config backed by AWS SSM'''

import boto3

from .config_base import ConfigBase

class SsmConfig(ConfigBase):
    '''SsmConfig'''

    def __init__(self):
        self.client = boto3.client('ssm')

    def get_str(self, prop_name, default_value=None):
        '''Get the str property by name'''
        try:
            response = self.client.get_parameter(
                Name=prop_name,
                WithDecryption=True
            )
            return response['Parameter']['Value']
        except Exception:
            if default_value:
                return default_value
            raise ValueError('Property not found: ' + prop_name)

    def put(self, prop_name, prop_value):
        ''' Set property by name.

            Only affects the environment for this python process.
        '''
        self.client.put_parameter(
            Name=prop_name,
            Value=prop_value,
            Type='String',
            Overwrite=True
        )
