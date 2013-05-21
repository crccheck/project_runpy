"""
Tim: Helpers related to functionality.
"""
import os

# ``create_project_dir`` re-provided for convenience
from dj_settings_helpers import create_project_dir, get_env


__all__ = ['create_project_dir', 'env', ]


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
