from .config import foo_settings


def something():
    return f"The setting is {foo_settings.some_path}"

def say_something():
    print(f"I say {something()}")