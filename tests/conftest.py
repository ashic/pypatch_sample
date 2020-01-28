import pytest
from unittest.mock import patch

@pytest.fixture(scope='module', autouse=True)
def foo_settings():
    # the first with is unnecessary, as the function calls some_path, but here to show
    # multiple patches
    with patch("patch_test.config.foo_settings.function_to_get_something", return_value="hola"):
        with patch("patch_test.config.foo_settings.some_path", "hola"):
            yield
