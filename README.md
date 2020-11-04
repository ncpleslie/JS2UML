# JS2UML

A command-line interface for generating UML 2 Class Diagrams from JavaScript (ES6+) and Python.



This requires GraphViz installed: [Download here](https://graphviz.org/download/)



GraphViz will need to set as an environment variable in order to work

## Run

### Run application

`python main.py`

To parse files run `parse`.
To change the parser run `change`.


To run unit tests

`python test_runner.py`

To run doctests

`python doctest_runner.py`

To run test coverage

```
coverage run --branch --source=src test_runner.py
coverage report -m
coverage html
```


# Contributors

Nicholas Leslie: [ncpleslie](https://github.com/ncpleslie)