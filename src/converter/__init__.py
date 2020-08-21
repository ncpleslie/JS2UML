from . import js_parser
from . import digraph_converter
from . import converter


def load_tests(loader, tests, ignore):
    import unittest
    import doctest
    tests.addTests(doctest.DocTestSuite(js_parser))
    tests.addTests(doctest.DocTestSuite(digraph_converter))
    tests.addTests(doctest.DocTestSuite(converter))
    return tests
