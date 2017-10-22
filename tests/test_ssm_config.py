'''Env Config Tests'''

import pytest
import boto3
from moto import mock_ssm

from serverless_config import ssm_config
from . import STRING_PROP_1, INT_PROP_1


@pytest.fixture
def config():
    '''Return config'''
    return ssm_config()


@pytest.fixture
def ssm():
    '''Return ssm client'''
    return boto3.client('ssm')


def test_get_missing_prop(config):
    '''Test get missing prop'''
    with mock_ssm():
        with pytest.raises(ValueError):
            config.get_str(STRING_PROP_1)


def test_get_default_prop(config):
    '''Test getting a missing prop while providing a default value'''
    with mock_ssm():
        assert config.get_str(STRING_PROP_1, 'foobar') == 'foobar'


def test_get_prop(config, ssm):
    '''Test getting a prop that exists'''
    with mock_ssm():
        ssm.put_parameter(
            Name=STRING_PROP_1, Value='tolltrolls', Type='String')
        assert config.get_str(STRING_PROP_1) == 'tolltrolls'


def test_get_prop_with_default(config, ssm):
    '''Test getting a prop that exists while providing a default'''
    with mock_ssm():
        ssm.put_parameter(
            Name=STRING_PROP_1, Value='tolltrolls', Type='String')
        assert config.get_str(STRING_PROP_1, 'foobar') == 'tolltrolls'


def test_get_int_prop(config, ssm):
    '''Test getting an int prop'''
    with mock_ssm():
        ssm.put_parameter(Name=INT_PROP_1, Value='123', Type='String')
        assert config.get_int(INT_PROP_1) == 123


def test_get_invalid_int_prop(config, ssm):
    '''Test getting an int prop that isn't an int'''
    with mock_ssm():
        ssm.put_parameter(
            Name=STRING_PROP_1, Value='tolltrolls', Type='String')
        with pytest.raises(ValueError):
            config.get_int(STRING_PROP_1)
