project_runpy
=============

.. image:: https://github.com/crccheck/project_runpy/actions/workflows/ci.yaml/badge.svg?branch=master
    :target: https://github.com/crccheck/project_runpy/actions/workflows/ci.yaml

Generic helpers I wish existed or am constantly copying into my Python projects.


``env``
-------

Get information about your environment variables.

``.get(key, ...)``
~~~~~~~~~~~~~~~~~~

You can use ``env.get`` as a drop-in replacement for ``os.environ.get``. It
acts the same but is smarter about types and has extra magic for ENVIRONMENT
based settings::

    from project_runpy import env

    env.get('DATABASE_URL')  # get an environment variable
    env.get('DATABASE_URL', 'sqlite:///:memory:')  # provide a default
    env.get('DEBUG', True)  # default can be bool
    env.get('WORKERS', 10)  # default can be other types too, like int
    env.get('DEBUG', True, type_func=bool)  # explicitly get bool

If additional kwargs are specified, they will become the default if ENVIRONMENT
matches the key::

    from project_runpy import env

    env.get('WORKERS', 10, DEV=1)  # if ENVIRONMENT == DEV: default = 1
    env.get('DEBUG', FALSE, type_func=bool, TEST=False)  # combine it

``.require(key, ...)``
~~~~~~~~~~~~~~~~~~~~~~

If you want to be extra strict/cautious, you can raise an exception if the
environment variable was not set by using ``.require`` instead of ``.get``.

Demo::

    >>> from project_runpy import env
    >>> env.require('SHIRTSNSHOES')
    ImproperlyConfigured: Environment variable not found: SHIRTSNSHOES


``ColorizingStreamHandler``
---------------------------

Logging handler that produces colorized console output

Usage::

    import logging

    from project_runpy import ColorizingStreamHandler

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ColorizingStreamHandler())

Django::

    LOGGING = {

        ...

        'handlers': {

            ...

            'console': {
                'level': 'DEBUG',
                'class': 'project_runpy.ColorizingStreamHandler',
            },
        },

        ...

    }

``ReadableSqlFilter``
---------------------

A logging filter designed to make the ``django.db.backends`` output more
readable in local dev. This is an alternate to Django Debug Toolbar's SQL panel
(which, you should be using too) and adds feedback for queries outside HTML.
This **will slow down** your dev server, but it's a tradeoff for getting faster
feedback for optimizing your queries.

Django compatibility: Django >= 2.0

Turns::

    (0.002) SELECT "tx_elevators_building"."id", "tx_elevators_building"."elbi",
    "tx_elevators_building"."name_1", "tx_elevators_building"."name_2",
    "tx_elevators_building"."address_1", "tx_elevators_building"."address_2",
    "tx_elevators_building"."city", "tx_elevators_building"."zip_code",
    "tx_elevators_building"."county", "tx_elevators_building"."owner",
    "tx_elevators_building"."contact", "tx_elevators_building"."latitude",
    "tx_elevators_building"."longitude" FROM "tx_elevators_building" LIMIT 21;
    args=()

Into::

    (0.002) SELECT...FROM "tx_elevators_building" LIMIT 21

And when you have many queries, they all line up nicely in your terminal.

To install, edit your Django settings::

        LOGGING = {
            ...
            'filters': {
                'readable_sql': {
                    '()': 'project_runpy.ReadableSqlFilter',
                },
            },
            'loggers': {
                'django.db.backends': {
                    'filters': ['readable_sql'],
                    ...
                },
            },
            ...
        }

About
-----

Inspired by `dj-settings-helpers`_, `ansistrm.py`_, and tornado_'s ``define``.

.. _dj-settings-helpers: https://github.com/tswicegood/dj-settings-helpers
.. _ansistrm.py: https://gist.github.com/vsajip/758430
.. _tornado: http://www.tornadoweb.org/en/latest/options.html#tornado.options.define
