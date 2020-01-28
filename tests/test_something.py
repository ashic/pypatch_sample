from patch_test import something
from unittest.mock import patch


@patch("patch_test.config.foo_settings.some_path", "hola")
def test_that_something():
    assert "The setting is hola" == something.something()
