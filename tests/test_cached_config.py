'''Test cached config'''

from datetime import datetime, timedelta
from serverless_config import EnvConfig, CachedConfig
from . import STRING_PROP_1


def test_cache_expiration(monkeypatch):
    '''Ensure that cache is expired after expiry time elapses'''
    monkeypatch.setenv(STRING_PROP_1, 'present')

    config = CachedConfig(EnvConfig(), timedelta(days=2))
    config.now = lambda: datetime(2017, 11, 11)
    assert config.get_str(STRING_PROP_1) == 'present'

    # Test immediately after
    monkeypatch.setenv(STRING_PROP_1, 'present2')
    assert config.get_str(STRING_PROP_1) == 'present'

    # test later, but not yet expired
    config.now = lambda: datetime(2017, 11, 12)
    assert config.get_str(STRING_PROP_1) == 'present'

    # test after cache has expired
    config.now = lambda: datetime(2017, 11, 14)
    assert config.get_str(STRING_PROP_1) == 'present2'


def test_cache_invalidation(monkeypatch):
    '''Ensure that cache is expired after it is manually invalidated'''
    monkeypatch.setenv(STRING_PROP_1, 'present')

    config = CachedConfig(EnvConfig(), timedelta(days=2))
    assert config.get_str(STRING_PROP_1) == 'present'

    # Test immediately after
    monkeypatch.setenv(STRING_PROP_1, 'present2')
    assert config.get_str(STRING_PROP_1) == 'present'

    # test after invalidating
    config.clear()
    assert config.get_str(STRING_PROP_1) == 'present2'
