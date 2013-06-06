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


def get_env(key, default, force_bool=False, type_func=None, **defaults):
    env = os.environ.get('ENVIRONMENT')
    a = os.environ.get(key, defaults.get(env, default))
    if force_bool:
        return str(a).lower() in ['1', 'yes', 'true', ]
    return a if type_func is None else type_func(a)


class _Env(dict):
    """A wrapper around os.environ that supports environments and `Boolean`."""
    def __init__(self):
        self.update(os.environ.copy())

    def get(self, key, default=None, *args, **kwargs):
        """
        Get information from your environment.

        A wrapper around dj-settings-helper's ``get_env`` that mimics the api of
        ``os.environ``.
        """
        return get_env(key, default, *args, **kwargs)


env = _Env()
