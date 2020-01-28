from .config import foo_settings


def something():
    return f"The setting is {foo_settings.some_path}"

def something_w_fn():
    return f"The setting is {foo_settings.function_to_get_something()}"


def say_something():
    print(f"I say {something()}")