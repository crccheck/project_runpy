"""
Tim: Helpers related to functionality.
"""
import os


__all__ = ['create_project_dir', 'env', ]


def create_project_dir(project_path):
    def project_dir(*paths):
        base = os.path.realpath(os.path.dirname(project_path))
        return os.path.join(base, *paths)

    return project_dir


class _Env(dict):
    """A wrapper around os.environ that supports environments and `Boolean`."""
    def __init__(self):
        self.update(os.environ.copy())

    def parse_bool(self, value):
        return str(value).lower() not in ('false', '0', 'f')

    def get(self, key, default=None, type_func=None, **defaults):
        """
        Get information from your environment.

        If additional kwargs are specified, they will become the default if
        ENVIRONMENT matches the key.

        Usage::

            env.get('DATABASE_URL')  # get an environment variable
            env.get('DATABASE_URL', 'sqlite:///:memory:')  # provide a default
            env.get('DEBUG', True)  # default can be bool
            env.get('WORKERS', 10)  # default can be other types too, like int
            env.get('WORKERS', 10, DEV=1)  # if ENVIRONMENT == DEV: default = 1
            env.get('DEBUG', True, type_func=bool)  # explicitly get bool
            env.get('DEBUG', FALSE, type_func=bool, TEST=False)  # combine it

        """
        environment = os.environ.get('ENVIRONMENT')
        value = os.environ.get(key, defaults.get(environment, default))
        if value is None and type_func is None:
            # return early to prevent returning 'None'
            return ''
        if type_func is None:
            # guess the type_func
            type_func = str if default is None else default.__class__
        if type_func is bool:
            # strings will cast as `True` so don't use bool, use parse_bool.
            type_func = self.parse_bool
        return type_func(value)


env = _Env()
