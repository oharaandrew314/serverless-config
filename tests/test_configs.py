'''Env Config Tests'''

import pytest
from moto import mock_ssm

from serverless_config import env_config, ssm_config
from . import STRING_PROP_1


@pytest.mark.parametrize("config", [env_config(), ssm_config()])
def test_get_missing_prop(config):
    '''Test get missing prop'''
    with mock_ssm():
        with pytest.raises(ValueError):
            config.get_str(STRING_PROP_1)


@pytest.mark.parametrize("config", [env_config(), ssm_config()])
def test_get_default_prop(config):
    '''Test getting a missing prop while providing a default value'''
    with mock_ssm():
        assert config.get_str(STRING_PROP_1, 'foobar') == 'foobar'


@pytest.mark.parametrize("config", [env_config(), ssm_config()])
def test_get_prop(config):
    '''Test getting a prop that exists'''
    with mock_ssm():
        config.put(STRING_PROP_1, 'tolltrolls')
        assert config.get_str(STRING_PROP_1) == 'tolltrolls'


@pytest.mark.parametrize("config", [env_config(), ssm_config()])
def test_get_prop_with_default(config):
    '''Test getting a prop that exists while providing a default'''
    with mock_ssm():
        config.put(STRING_PROP_1, 'tolltrolls')
        assert config.get_str(STRING_PROP_1, 'foobar') == 'tolltrolls'
