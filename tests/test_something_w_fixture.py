from patch_test import something


def test_something_w_fixture(foo_settings):

    real = something.something_w_fn()
    assert "The setting is hola" == real


    real_2 = something.something()
    assert "The setting is hola" == real_2
