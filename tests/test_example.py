"""Example test module."""

import aind_s3_cache


def test_version():
    """Test that version is defined."""
    assert aind_s3_cache.__version__ is not None
    assert isinstance(aind_s3_cache.__version__, str)