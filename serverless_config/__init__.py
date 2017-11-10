'''slsconf'''

from .env_config import EnvConfig  # noqa F401
from .ssm_config import SsmConfig  # noqa F401
from .cached_config import CachedConfig
from .composite_config import CompositeConfig
from .config_base import ConfigBase
assert ConfigBase


def default_config():
    ''' Return a Composite Config.

        Searches in the system environment, and SSM, in that order.

        NOTE: The IAM Role for this machine must have an appropriate SSM
        Policy attached to it.
    '''
    return CachedConfig(
        CompositeConfig(EnvConfig(), SsmConfig())
    )
