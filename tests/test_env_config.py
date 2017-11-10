'''Env Config Tests'''

import pytest

from serverless_config import EnvConfig
from . import STRING_PROP_1, INT_PROP_1


@pytest.fixture
def config():
    '''Config object'''
    return EnvConfig()


def test_get_missing_prop(config):
    '''Test get missing prop'''
    assert config.get_str(STRING_PROP_1) is None


def test_get_default_prop(config):
    '''Test getting a missing prop while providing a default value'''
    assert config.get_str(STRING_PROP_1, 'foobar') == 'foobar'


def test_get_prop(monkeypatch, config):
    '''Test getting a prop that exists'''
    monkeypatch.setenv(STRING_PROP_1, 'tolltrolls')
    assert config.get_str(STRING_PROP_1) == 'tolltrolls'


def test_get_prop_with_default(monkeypatch, config):
    '''Test getting a prop that exists while providing a default'''
    monkeypatch.setenv(STRING_PROP_1, 'tolltrolls')
    assert config.get_str(STRING_PROP_1, 'foobar') == 'tolltrolls'


def test_get_int_prop(monkeypatch, config):
    '''Test getting an int prop'''
    monkeypatch.setenv(INT_PROP_1, '123')
    assert config.get_int(INT_PROP_1) == 123


def test_get_invalid_int_prop(monkeypatch, config):
    '''Test getting an int prop that isn't an int'''
    monkeypatch.setenv(STRING_PROP_1, 'tolltroll')
    with pytest.raises(ValueError):
        config.get_int(STRING_PROP_1)
