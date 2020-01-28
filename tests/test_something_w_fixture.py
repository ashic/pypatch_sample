from patch_test import something
import patch_test
import pytest
from unittest.mock import patch


def test_something_w_fixture(foo_settings):

    real = something.something_w_fn()
    assert "The setting is hola" == real


    real_2 = something.something()
    assert "The setting is hola" == real_2



@pytest.mark.parametrize('foo_settings_w_p', ["adios"], indirect=True)
def test_something_w_fixture_w_p(foo_settings_w_p):
    real = something.something_w_fn()
    assert "The setting is adios" == real

    real_2 = something.something()
    assert "The setting is adios" == real_2


    real_3 = patch_test.config.foo_settings.some_path
    assert "adios" == real_3

    real_4 = patch_test.config.foo_settings.function_to_get_something()
    assert "adios" == real_4

