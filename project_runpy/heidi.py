"""
Heidi: Helpers related to visuals.
"""
import logging
import hashlib

__all__ = [
    "ColorizingStreamHandler",
    "ColorizingLevelStreamHandler",
    "ColorizingNameStreamHandler",
    "ReadableSqlFilter",
]


# Copyright (C) 2010-2012 Vinay Sajip. All rights reserved. Licensed under the new BSD license.
# https://gist.github.com/758430
class ColorizingStreamHandler(logging.StreamHandler):
    # color names to indices
    color_map = {
        "black": 0,
        "red": 1,
        "green": 2,
        "yellow": 3,
        "blue": 4,
        "magenta": 5,
        "cyan": 6,
        "white": 7,
    }

    # levels to (background, foreground, bold/intense)
    level_map = {
        logging.DEBUG: (None, "blue", False),
        logging.INFO: (None, "white", False),
        logging.WARNING: (None, "yellow", False),
        logging.ERROR: (None, "red", False),
        logging.CRITICAL: ("red", "white", True),
    }
    csi = "\x1b["
    reset = "\x1b[0m"

    @property
    def is_tty(self):
        isatty = getattr(self.stream, "isatty", None)
        return isatty and isatty()

    def emit(self, record):
        try:
            message = self.format(record)
            stream = self.stream
            if not self.is_tty:
                stream.write(message)
            else:
                self.output_colorized(message)
            stream.write(getattr(self, "terminator", "\n"))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:  # noqa: E722
            self.handleError(record)

    def output_colorized(self, message):
        self.stream.write(message)

    def colorize(self, message: str, record: logging.LogRecord) -> str:
        if record.levelno in self.level_map:
            bg, fg, bold = self.level_map[record.levelno]
            params = []
            if bg in self.color_map:
                params.append(str(self.color_map[bg] + 40))
            if fg in self.color_map:
                params.append(str(self.color_map[fg] + 30))
            if bold:
                params.append("1")
            if params:
                message = "".join(
                    (self.csi, ";".join(params), "m", message, self.reset)
                )
        return message

    def format(self, record):
        message = logging.StreamHandler.format(self, record)
        if self.is_tty:
            # Don't colorize any traceback
            parts = message.split("\n", 1)
            parts[0] = self.colorize(parts[0], record)
            message = "\n".join(parts)
        return message


class ColorizingLevelStreamHandler(ColorizingStreamHandler):
    pass


class ColorizingNameStreamHandler(ColorizingStreamHandler):
    per_logger_colors = [
        (None, "red", False),
        (None, "green", False),
        (None, "yellow", False),
        (None, "blue", False),
        (None, "magenta", False),
        (None, "cyan", False),
    ]

    def colorize(self, message: str, record: logging.LogRecord) -> str:
        bg, fg, bold = self.per_logger_colors[
            int.from_bytes(
                hashlib.blake2s(record.name.encode()).digest()[:8], byteorder="big"
            )
            % len(self.per_logger_colors)
        ]
        params = []
        if bg in self.color_map:
            params.append(str(self.color_map[bg] + 40))
        if fg in self.color_map:
            params.append(str(self.color_map[fg] + 30))
        if bold:
            params.append("1")
        if params:
            message = "".join((self.csi, ";".join(params), "m", message, self.reset))
        return message


# LOGGING FILTERS
#################


class ReadableSqlFilter(logging.Filter):
    """
    A filter for more readable sql by stripping out the SELECT ... columns.

    Modeled after how debug toolbar displays SQL. This code should be optimized
    for performance. For example, I don't check to make sure record.name is
    'django.db.backends' because I assume you put this filter alongside it.

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
        # https://github.com/django/django/blob/febe136d4c3310ec8901abecca3ea5ba2be3952c/django/db/backends/utils.py#L106-L131
        duration, sql, *record_args = record.args
        if sql and "\n" in sql[:28]:
            sql = " ".join(sql.strip().split())
            record.args = (duration, sql, *record_args)
        if not sql or "SELECT" not in sql[:28]:
            # WISHLIST what's the most performant way to see if 'SELECT' was
            # used?
            return super().filter(record)

        begin = sql.index("SELECT")
        try:
            end = sql.index("FROM", begin + 6)
        except ValueError:  # not all SELECT statements also have a FROM
            return super().filter(record)

        sql = "{0}...{1}".format(sql[: begin + 6], sql[end:])
        # Drop "; args=%s" to shorten logging output
        record.msg = "(%.3f) %s"
        record.args = (duration, sql)
        return super().filter(record)
