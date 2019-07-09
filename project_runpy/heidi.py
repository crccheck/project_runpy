"""
Heidi: Helpers related to visuals.
"""
import logging

__all__ = ['ColorizingStreamHandler', 'ReadableSqlFilter']


#
# Copyright (C) 2010-2012 Vinay Sajip. All rights reserved. Licensed under the new BSD license.
# https://gist.github.com/758430
#


class ColorizingStreamHandler(logging.StreamHandler):
    # color names to indices
    color_map = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
    }

    # levels to (background, foreground, bold/intense)
    level_map = {
        logging.DEBUG: (None, 'blue', False),
        logging.INFO: (None, 'white', False),
        logging.WARNING: (None, 'yellow', False),
        logging.ERROR: (None, 'red', False),
        logging.CRITICAL: ('red', 'white', True),
    }
    csi = '\x1b['
    reset = '\x1b[0m'

    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty()

    def emit(self, record):
        try:
            message = self.format(record)
            stream = self.stream
            if not self.is_tty:
                stream.write(message)
            else:
                self.output_colorized(message)
            stream.write(getattr(self, 'terminator', '\n'))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:  # noqa: E722
            self.handleError(record)

    def output_colorized(self, message):
        self.stream.write(message)

    def colorize(self, message, record):
        if record.levelno in self.level_map:
            bg, fg, bold = self.level_map[record.levelno]
            params = []
            if bg in self.color_map:
                params.append(str(self.color_map[bg] + 40))
            if fg in self.color_map:
                params.append(str(self.color_map[fg] + 30))
            if bold:
                params.append('1')
            if params:
                message = ''.join((self.csi, ';'.join(params),
                                   'm', message, self.reset))
        return message

    def format(self, record):
        message = logging.StreamHandler.format(self, record)
        if self.is_tty:
            # Don't colorize any traceback
            parts = message.split('\n', 1)
            parts[0] = self.colorize(parts[0], record)
            message = '\n'.join(parts)
        return message


###########
# FILTERS #
###########

class ReadableSqlFilter(logging.Filter):
    """
    A filter for more readable sql by stripping out the SELECT ... columns.

    Modeled after how debug toolbar displays SQL. This code should be optimized
    for performance. For example, I don't check to make sure record.name is
    'django.db.backends' because I assume you put this filter alongside it. I
    also assume there is going to be a 'FROM' if there's a 'SELECT' and don't
    catch the ValueError that would result from that.

    Sample Usage in Django's `settings.py`:

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
                ...
            },
        }
    """

    def filter(self, record):
        # Django 1.7 changed the way SQL got logged for some reason:
        # https://code.djangoproject.com/ticket/17158
        # https://github.com/django/django/commit/6605ac331a9e0
        if 'SELECT' not in record.sql[:28]:
            # WISHLIST what's the most performant way to see if 'SELECT' was
            # used?
            return True

        # unfortunately, record.msg has already been rendered so we have to
        # modify .msg in-place instead of .sql
        begin = record.msg.index('SELECT')
        try:
            end = record.msg.index('FROM')
        except ValueError:  # not all SELECT statements also have a FROM
            return True
        try:
            very_end = record.msg.rindex(u'; args') + 1
        except ValueError:  # msg does not have "args" to strip
            very_end = None
        record.msg = u'{0} ... {1}'.format(
            record.msg[:begin + 6], record.msg[end:very_end])
        return True
