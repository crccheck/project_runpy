import logging
import unittest

try:
    from unittest2 import TestCase
except ImportError:
    from unittest import TestCase
import os


from project_runpy import (
    ColorizingStreamHandler,
    env,
    ImproperlyConfigured,
    ReadableSqlFilter,
)


class TestTimEnv(TestCase):
    def setUp(self):
        self.key = '_tim_test'

    def tearDown(self):
        if self.key in os.environ:
            os.environ.pop(self.key)
        if 'ENVIRONMENT' in os.environ:
            os.environ.pop('ENVIRONMENT')

    def set_val(self, value):
        """Shortcut for setting the environment variable."""
        os.environ[self.key] = str(value)

    def test_gets_value(self):
        self.set_val('foobar')
        result = env.get(self.key)
        self.assertEqual(result, 'foobar')

    def test_geting_empty_is_null_string(self):
        result = env.get(self.key)
        self.assertIs(result, '')

    def test_reads_from_default(self):
        result = env.get(self.key, 'qwerty')
        self.assertEqual(result, 'qwerty')

    def test_gets_as_bool_if_default_is_bool(self):
        self.set_val('1')
        result = env.get(self.key, True)
        self.assertIs(result, True)

    def test_get_bool_coerced_version_true(self):
        self.set_val('1')
        result = env.get(self.key, 'True', type_func=bool)
        self.assertIs(result, True)

    def test_get_bool_coerced_version_false(self):
        self.set_val('0')
        result = env.get(self.key, 'True', type_func=bool)
        self.assertIs(result, False)

    def test_coerced_bool_no_default_no_value_is_true(self):
        result = env.get(self.key, type_func=bool)
        self.assertIs(result, True)

    def test_zero_gives_false(self):
        self.set_val('0')
        result = env.get(self.key, True)
        self.assertIs(result, False)

    def test_f_gives_false(self):
        self.set_val('f')
        result = env.get(self.key, True)
        self.assertIs(result, False)

    def test_false_gives_false(self):
        self.set_val('fAlsE')
        result = env.get(self.key, True)
        self.assertIs(result, False)

    def test_can_coerce_to_other_types(self):
        self.set_val('20')
        result = env.get(self.key, 10)
        self.assertIs(result, 20)

    def test_reads_from_environment_if_set(self):
        result = env.get(self.key, 'qwerty', DEV='dvorak')
        self.assertEqual(result, 'qwerty')
        os.environ['ENVIRONMENT'] = 'DEV'
        result = env.get(self.key, 'qwerty', DEV='dvorak')
        self.assertEqual(result, 'dvorak')
        del os.environ['ENVIRONMENT']  # teardown

    def test_no_default_unless_in_environment(self):
        result = env.get(self.key, DEV='dvorak')
        self.assertEqual(result, '')
        os.environ['ENVIRONMENT'] = 'DEV'
        result = env.get(self.key, DEV='dvorak')
        self.assertEqual(result, 'dvorak')
        del os.environ['ENVIRONMENT']  # teardown

    def test_no_default_unless_in_environment_and_bool(self):
        result = env.get(self.key, DEV=False)
        self.assertEqual(result, '')
        os.environ['ENVIRONMENT'] = 'DEV'
        result = env.get(self.key, DEV=False)
        self.assertEqual(result, False)
        del os.environ['ENVIRONMENT']  # teardown

    def test_require_raises_exception(self):
        with self.assertRaises(ImproperlyConfigured):
            env.require('FOO')

    def test_require_raises_exception_with_stupid_default(self):
        with self.assertRaises(ImproperlyConfigured):
            env.require('FOO', default='')

        with self.assertRaises(ImproperlyConfigured):
            env.require('FOO', default=u'')

    def test_require_acts_like_get(self):
        os.environ['FOO'] = 'BAR'
        self.assertEqual(env.require('FOO'), 'BAR')
        del os.environ['FOO']  # teardown


class HeidiColorizingStreamHandler(TestCase):
    def test_it_works(self):
        # assert can add handler without an exception getting raised
        logger = logging.getLogger('test')
        logger.addHandler(ColorizingStreamHandler())


class HeidiReadableSqlFilter(TestCase):
    def test_it_works(self):
        # assert can add filter without an exception getting raised
        logger = logging.getLogger('test')
        logger.addFilter(ReadableSqlFilter())


if __name__ == '__main__':
    unittest.main()
