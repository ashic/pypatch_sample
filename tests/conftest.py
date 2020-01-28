import pytest
from unittest.mock import patch


@pytest.fixture(scope='module', autouse=True)
def foo_settings():
    # the first with is unnecessary, as the function calls some_path, but here to show
    # multiple patches. Leaving this in can mess up other patches if they patch
    # the underlying variable, but not the function.
    # with patch("patch_test.config.foo_settings.function_to_get_something", return_value="hola"):
        with patch("patch_test.config.foo_settings.some_path", "hola"):
            yield


@pytest.fixture(scope="module")
def foo_settings_w_p(request):
        with patch("patch_test.config.foo_settings.some_path", request.param):
            yield
