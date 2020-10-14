import doctest
import unittest
from src.converter import js_parser
from src.converter import digraph_converter
from src.converter import converter
from src.io import read
from src.io import config
from src.console_view import console_view

tests = [js_parser, digraph_converter, converter, read, config, console_view]
print('Running doctests')
for aTest in tests:
    print("=========================================================")
    print(f'Running test {aTest}')
    doctest.testmod(aTest)
    print("=========================================================")

print('Doctests finished')
