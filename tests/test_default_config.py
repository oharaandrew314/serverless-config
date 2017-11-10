'''test default config'''

from serverless_config import default_config
from moto import mock_ssm

from . import INT_PROP_1


def test_default_config(monkeypatch):
    '''test default config'''
    with mock_ssm():
        config = default_config()
        assert config.get_int(INT_PROP_1, default_value=2) == 2

        # prop should be cached
        monkeypatch.setenv(INT_PROP_1, 1)
        assert config.get_int(INT_PROP_1, default_value=2) == 2

        # invalidate cache
        config.clear()
        assert config.get_int(INT_PROP_1, default_value=2) == 1
