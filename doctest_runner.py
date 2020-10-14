import doctest
import unittest
from js2uml.converter import js_parser
from js2uml.converter import digraph_converter
from js2uml.converter import converter
from js2uml.io import read
from js2uml.io import config
from js2uml.console_view import console_view

tests = [js_parser, digraph_converter, converter, read, config, console_view]
print('Running doctests')
for aTest in tests:
    print("=========================================================")
    print(f'Running test {aTest}')
    doctest.testmod(aTest)
    print("=========================================================")

print('Doctests finished')
