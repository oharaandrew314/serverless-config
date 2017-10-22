'''slsconf'''

from .env_config import EnvConfig
from .ssm_config import SsmConfig
from .composite_config import CompositeConfig
from .config_base import ConfigBase
assert ConfigBase


def env_config():
    '''Return a new System Environment Config'''
    return EnvConfig()


def ssm_config():
    '''Return a new AWS SSM Config

        NOTE: The IAM Role for this machine must have an appropriate SSM
        Policy attached to it.
    '''
    return SsmConfig()


def default_config():
    ''' Return a Composite Config.

        Searches in the system environment, and SSM, in that order.

        NOTE: The IAM Role for this machine must have an appropriate SSM
        Policy attached to it.
    '''
    return CompositeConfig(env_config(), ssm_config())


def custom_composite_config(*configs):
    ''' Return a custom Composite Config.

        Pass ion as many configs as you want in order of precedence.
    '''
    return CompositeConfig(*configs)
