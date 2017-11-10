'''Composite Config Tests'''

import pytest
from moto import mock_ssm, mock_kms
import boto3

from serverless_config import EnvConfig, SsmConfig, CompositeConfig
from . import STRING_PROP_1, INT_PROP_1, SECRET_INT_1, SECRET_STRING_1


@pytest.fixture
def config():
    '''Return the composite config'''
    return CompositeConfig(EnvConfig(), SsmConfig())


@pytest.fixture
def ssm_conf():
    '''Return the SSM Config'''
    return SsmConfig()


@pytest.fixture
def ssm():
    '''Return the AWS SSM Client'''
    return boto3.client('ssm')


def key_id():
    '''Return a KMS Key Id'''
    return boto3.client('kms').create_key()['KeyMetadata']['KeyId']


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
    config = CompositeConfig(ssm_conf, EnvConfig())

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
        assert config.get_str(STRING_PROP_1) is None


def test_get_int_prop(monkeypatch, config):
    '''Test getting an int prop'''
    monkeypatch.setenv(INT_PROP_1, '123')
    assert config.get_int(INT_PROP_1) == 123


def test_get_invalid_int_prop(monkeypatch, config):
    '''Test getting an int prop that isn't an int'''
    monkeypatch.setenv(STRING_PROP_1, 'tolltroll')
    with pytest.raises(ValueError):
        config.get_int(STRING_PROP_1)


@mock_kms
@mock_ssm
def test_get_ssm_secret_encrypted():
    '''Test getting an ssm secret that is encrypted during transit'''
    ssm().put_parameter(
        Name=SECRET_STRING_1, Type='SecureString', KeyId=key_id(),
        Value='secretstuff'
    )
    assert config().get_str(SECRET_STRING_1) != 'secretstuff'


@mock_kms
@mock_ssm
def test_get_ssm_secret_decrypted():
    '''Test getting an ssm secret that is decrypted during transit'''
    ssm().put_parameter(
        Name=SECRET_STRING_1, Type='SecureString', KeyId=key_id(),
        Value='secretstuff'
    )
    assert (
        config().get_str(SECRET_STRING_1, WithDecryption=True) ==
        'secretstuff'
    )


@mock_kms
@mock_ssm
def test_get_ssm_int_secret_decrypted():
    '''Test getting an ssm secret that is decrypted during transit'''
    ssm().put_parameter(
        Name=SECRET_INT_1, Type='SecureString', KeyId=key_id(),
        Value='123'
    )
    assert config().get_int(SECRET_INT_1, WithDecryption=True) == 123
