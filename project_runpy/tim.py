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

    def get(self, key, default=None, type_func=None, **defaults):
        """
        Get information from your environment.
        """
        env = os.environ.get('ENVIRONMENT')
        a = os.environ.get(key, defaults.get(env, default))
        if force_bool:
            return str(a).lower() in ['1', 'yes', 'true', ]
        return a if type_func is None else type_func(a)


env = _Env()
