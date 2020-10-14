from unittest import TestLoader, TextTestRunner

loader = TestLoader()
start_dir = 'tests/'
suite = loader.discover(start_dir)
runner = TextTestRunner().run(suite)
