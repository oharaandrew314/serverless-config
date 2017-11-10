'''Config backed by AWS SSM'''

import boto3
from botocore.exceptions import ClientError

from .config_base import ConfigBase


class SsmConfig(ConfigBase):
    '''SsmConfig'''

    def __init__(self):
        self.client = boto3.client('ssm')

    def get_str(self, prop_name, default_value=None, **kwargs):
        ''' Get a str property by name or None'''
        try:
            response = self.client.get_parameter(
                Name=prop_name,
                **kwargs
            )
            return response['Parameter']['Value']
        except ClientError:
            return default_value

    def get_int(self, prop_name, default_value=None, **kwargs):
        ''' Get an int property by name or None.
            Raises ValueError if not an int.
        '''
        value = self.get_str(prop_name, default_value, **kwargs)
        return int(value) if value else None
