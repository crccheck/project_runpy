import logging
import os
import unittest
from unittest import TestCase, mock

from project_runpy import (
    ColorizingStreamHandler,
    env,
    ImproperlyConfigured,
    ReadableSqlFilter,
)


VERY_LONG_STRING = "*" * 512


class TestTimEnv(TestCase):
    def setUp(self):
        self.key = "_tim_test"

    def tearDown(self):
        if self.key in os.environ:
            os.environ.pop(self.key)
        if "ENVIRONMENT" in os.environ:
            os.environ.pop("ENVIRONMENT")

    def set_val(self, value):
        """Shortcut for setting the environment variable."""
        os.environ[self.key] = str(value)

    def test_gets_value(self):
        self.set_val("foobar")
        result = env.get(self.key)
        self.assertEqual(result, "foobar")

    def test_geting_empty_is_null_string(self):
        result = env.get(self.key)
        self.assertIs(result, "")

    def test_reads_from_default(self):
        result = env.get(self.key, "qwerty")
        self.assertEqual(result, "qwerty")

    def test_gets_as_bool_if_default_is_bool(self):
        self.set_val("1")
        result = env.get(self.key, True)
        self.assertIs(result, True)

    def test_get_bool_coerced_version_true(self):
        self.set_val("1")
        result = env.get(self.key, "True", type_func=bool)
        self.assertIs(result, True)

    def test_get_bool_coerced_version_false(self):
        self.set_val("0")
        result = env.get(self.key, "True", type_func=bool)
        self.assertIs(result, False)

    def test_coerced_bool_no_default_no_value_is_true(self):
        result = env.get(self.key, type_func=bool)
        self.assertIs(result, True)

    def test_zero_gives_false(self):
        self.set_val("0")
        result = env.get(self.key, True)
        self.assertIs(result, False)

    def test_f_gives_false(self):
        self.set_val("f")
        result = env.get(self.key, True)
        self.assertIs(result, False)

    def test_false_gives_false(self):
        self.set_val("fAlsE")
        result = env.get(self.key, True)
        self.assertIs(result, False)

    def test_can_coerce_to_other_types(self):
        self.set_val("20")
        result = env.get(self.key, 10)
        self.assertIs(result, 20)

    def test_reads_from_environment_if_set(self):
        result = env.get(self.key, "qwerty", DEV="dvorak")
        self.assertEqual(result, "qwerty")
        os.environ["ENVIRONMENT"] = "DEV"
        result = env.get(self.key, "qwerty", DEV="dvorak")
        self.assertEqual(result, "dvorak")
        del os.environ["ENVIRONMENT"]  # teardown

    def test_no_default_unless_in_environment(self):
        result = env.get(self.key, DEV="dvorak")
        self.assertEqual(result, "")
        os.environ["ENVIRONMENT"] = "DEV"
        result = env.get(self.key, DEV="dvorak")
        self.assertEqual(result, "dvorak")
        del os.environ["ENVIRONMENT"]  # teardown

    def test_no_default_unless_in_environment_and_bool(self):
        result = env.get(self.key, DEV=False)
        self.assertEqual(result, "")
        os.environ["ENVIRONMENT"] = "DEV"
        result = env.get(self.key, DEV=False)
        self.assertEqual(result, False)
        del os.environ["ENVIRONMENT"]  # teardown

    def test_require_raises_exception(self):
        with self.assertRaises(ImproperlyConfigured):
            env.require("FOO")

    def test_require_raises_exception_with_stupid_default(self):
        with self.assertRaises(ImproperlyConfigured):
            env.require("FOO", default="")

        with self.assertRaises(ImproperlyConfigured):
            env.require("FOO", default="")

    def test_require_acts_like_get(self):
        os.environ["FOO"] = "BAR"
        self.assertEqual(env.require("FOO"), "BAR")
        del os.environ["FOO"]  # teardown


class HeidiColorizingStreamHandler(TestCase):
    def test_it_can_be_added_to_logger(self):
        logger = logging.getLogger("test")
        logger.addHandler(ColorizingStreamHandler())
        with self.assertLogs(logger, logging.CRITICAL):
            logger.critical("hello")

    def test_it_handles_unicode_loggers(self):
        logger = logging.getLogger("¡tést!")
        logger.addHandler(ColorizingStreamHandler())
        with self.assertLogs(logger, logging.CRITICAL):
            logger.critical("héllø")


class HeidiReadableSqlFilter(TestCase):
    def test_it_can_be_added_to_logger(self):
        logger = logging.getLogger("foo.sql")
        logger.addHandler(logging.NullHandler())
        logger.addFilter(ReadableSqlFilter())
        with self.assertRaises(ValueError):
            # Sanity check
            logger.warning("original msg %s %s %s")
        logger.warning("original msg %s %s %s", "0.1", "NOT SQL", ())

    def test_filter_trivial_case(self):
        logging_filter = ReadableSqlFilter()
        record = mock.MagicMock(args=())
        record = mock.MagicMock(args=(1.0, "foo", ()))
        self.assertTrue(logging_filter.filter(record))
        self.assertEqual("foo", record.args[1])

    def test_filter_runs_when_no_sql_exists(self):
        logging_filter = ReadableSqlFilter()
        record = mock.MagicMock(args=(0.07724404335021973, None, ()))
        self.assertTrue(logging_filter.filter(record))

    def test_filter_params_is_optional(self):
        logging_filter = ReadableSqlFilter()
        record = mock.MagicMock(args=())
        record = mock.MagicMock(args=(1.0, "foo"))
        self.assertTrue(logging_filter.filter(record))
        self.assertEqual("foo", record.args[1])

    def test_filter_formats_select_from(self):
        logging_filter = ReadableSqlFilter()
        record = mock.MagicMock(args=(1.0, "(yolo) SELECT foo FROM moo"))
        self.assertTrue(logging_filter.filter(record))
        self.assertIn("SELECT...FROM moo", record.args[1])

    def test_filter_formats_select_from_long(self):
        logging_filter = ReadableSqlFilter()
        original_sql = "(yolo) SELECT {0} FROM moo".format(VERY_LONG_STRING)
        record = mock.MagicMock(args=(1.0, original_sql))
        self.assertTrue(logging_filter.filter(record))
        self.assertIn("SELECT...FROM moo", record.args[1])

    def test_filter_formats_ignores_select_without_from(self):
        logging_filter = ReadableSqlFilter()
        original_sql = "(yolo) SELECT {0} moo".format(VERY_LONG_STRING)
        record = mock.MagicMock(args=(1.0, original_sql))
        self.assertTrue(logging_filter.filter(record))
        self.assertEqual(original_sql, record.args[1])

    def test_filter_collapses_multiline_sql(self):
        long_sql = """
            (0.002)
                SELECT VERSION(),
                       @@sql_mode,
                       @@default_storage_engine,
                       @@sql_auto_is_null,
                       @@lower_case_table_names,
                       CONVERT_TZ('2001-01-01 01:00:00', 'UTC', 'UTC') IS NOT NULL
            ; args=None
            """
        logging_filter = ReadableSqlFilter()
        record = mock.MagicMock(args=(1.0, long_sql))
        self.assertIn("\n", record.args[1])

        self.assertTrue(logging_filter.filter(record))

        self.assertNotIn("\n", record.args[1])


if __name__ == "__main__":
    unittest.main()
