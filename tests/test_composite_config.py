'''Composite Config Tests'''

import pytest
from moto import mock_ssm
import boto3

from serverless_config import (
    default_config, env_config, ssm_config, custom_composite_config
)
from . import STRING_PROP_1, INT_PROP_1


@pytest.fixture
def config():
    '''Return the composite config'''
    return default_config()


@pytest.fixture
def ssm_conf():
    '''Return the SSM Config'''
    return ssm_config()


@pytest.fixture
def ssm():
    '''Return the AWS SSM Client'''
    return boto3.client('ssm')


def test_env_prop(monkeypatch, config):
    '''Test the composite config with an env prop'''
    monkeypatch.setenv(STRING_PROP_1, 'tolltrolls')
    with mock_ssm():
        assert config.get_str(STRING_PROP_1) == 'tolltrolls'


def test_env_prop_with_default(monkeypatch, config):
    '''Test the composite config with an env prop and a default'''
    monkeypatch.setenv(STRING_PROP_1, 'tolltrolls')
    with mock_ssm():
        assert config.get_str(STRING_PROP_1, 'ham') == 'tolltrolls'


def test_ssm_prop(config, ssm_conf, ssm):
    '''Test with an ssm property'''
    with mock_ssm():
        ssm.put_parameter(Name=STRING_PROP_1, Type='String', Value='foobar')
        assert config.get_str(STRING_PROP_1) == 'foobar'


def test_all_props_default_order(monkeypatch, config, ssm_conf, ssm):
    '''Test with both an env and ssm property'''
    monkeypatch.setenv(STRING_PROP_1, 'tolltrolls')
    with mock_ssm():
        ssm.put_parameter(Name=STRING_PROP_1, Type='String', Value='foobar')
        assert config.get_str(STRING_PROP_1) == 'tolltrolls'


def test_all_props_reverse_order(monkeypatch, ssm_conf, ssm):
    '''Test searching in reverse order'''
    config = custom_composite_config(ssm_conf, env_config())

    monkeypatch.setenv(STRING_PROP_1, 'tolltrolls')
    with mock_ssm():
        ssm.put_parameter(Name=STRING_PROP_1, Type='String', Value='foobar')
        assert config.get_str(STRING_PROP_1) == 'foobar'


def test_default_value(config):
    '''Test returning the default value when it is not provided elsewhere'''
    with mock_ssm():
        assert config.get_str(STRING_PROP_1, 'ham') == 'ham'


def test_no_value(config):
    '''Test with no value'''
    with mock_ssm():
        with pytest.raises(ValueError):
            assert config.get_str(STRING_PROP_1)


def test_get_int_prop(monkeypatch, config):
    '''Test getting an int prop'''
    monkeypatch.setenv(INT_PROP_1, '123')
    assert config.get_int(INT_PROP_1) == 123


def test_get_invalid_int_prop(monkeypatch, config):
    '''Test getting an int prop that isn't an int'''
    monkeypatch.setenv(STRING_PROP_1, 'tolltroll')
    with pytest.raises(ValueError):
        config.get_int(STRING_PROP_1)
