'''Test an unimplemented config'''

import pytest

from serverless_config import ConfigBase
from . import STRING_PROP_1


@pytest.fixture
def config():
    '''Return an unimplemented config'''
    return ConfigBase()


def test_get_str(config):
    '''Test that get_str is not implemented'''
    with pytest.raises(NotImplementedError):
        config.get_str(STRING_PROP_1)
