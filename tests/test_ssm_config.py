'''Env Config Tests'''

import pytest
import boto3
from moto import mock_ssm

from serverless_config import ssm_config
from . import STRING_PROP_1, INT_PROP_1


def config():
    '''Return config'''
    return ssm_config()


def ssm():
    '''Return ssm client'''
    return boto3.client('ssm')


@mock_ssm
def test_get_missing_prop():
    '''Test get missing prop'''
    with pytest.raises(ValueError):
        config().get_str(STRING_PROP_1)


@mock_ssm
def test_get_default_prop():
    '''Test getting a missing prop while providing a default value'''
    assert config().get_str(STRING_PROP_1, 'foobar') == 'foobar'


@mock_ssm
def test_get_prop():
    '''Test getting a prop that exists'''
    ssm().put_parameter(
        Name=STRING_PROP_1, Value='tolltrolls', Type='String')
    assert config().get_str(STRING_PROP_1) == 'tolltrolls'


@mock_ssm
def test_get_prop_with_default():
    '''Test getting a prop that exists while providing a default'''
    ssm().put_parameter(
        Name=STRING_PROP_1, Value='tolltrolls', Type='String')
    assert config().get_str(STRING_PROP_1, 'foobar') == 'tolltrolls'


@mock_ssm
def test_get_int_prop():
    '''Test getting an int prop'''
    ssm().put_parameter(Name=INT_PROP_1, Value='123', Type='String')
    assert config().get_int(INT_PROP_1) == 123


@mock_ssm
def test_get_invalid_int_prop():
    '''Test getting an int prop that isn't an int'''
    ssm().put_parameter(
        Name=STRING_PROP_1, Value='tolltrolls', Type='String')
    with pytest.raises(ValueError):
        config().get_int(STRING_PROP_1)
