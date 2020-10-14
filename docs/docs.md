# Download these

https://www2.graphviz.org/Packages/development/windows/10/msbuild/Release/x86/

## Doctests

>>> t = Read()
>>> result = t.load_file("")
>>> print(result)
None

>>> result = Config.get_default_filename()
>>> print(result)
filename

>>> result = Config.get_default_filetype()
>>> print(result)
png

>>> result = Config.get_default_storage_location()
>>> print(result)
tests

>>> Config.set_default_filename("filename")

>>> Config.set_default_filetype("png")

>>> Config.set_default_storage_location("tests")

>>> t = Converter()
>>> results = t.convert("class Patient {\
    constructor(issue) {\
        this.issue = new Object();\
            }}")
>>> print(type(results))
<class 'graphviz.dot.Digraph'>

>>> t = Converter()
>>> t.save(Digraph(), "filename", "png")

>>> t = DigraphConverter()
>>> results = t.convert([{'class_name': 'Patient', 'attributes': ['issue'], 'methods': ['constructor'], 'edges': {'Object'}}])
>>> print(type(results))
<class 'graphviz.dot.Digraph'>

>>> t = DigraphConverter()
>>> t.render(Digraph(), "filename", "png")

>>> t = JSParser()
>>> results = t.parse("class Patient {\
    constructor(issue) {\
        this.issue = new Object();\
            }}")
>>> print(results)
[{'class_name': 'Patient', 'attributes': ['issue'], 'methods': ['constructor'], 'edges': {'Object'}}]

>>> t = ConsoleView()
>>> t.show("test")
test

>>> t = ConsoleView()
>>> t.get_input("test")
test
''

>>> t = ConsoleView()
>>> result = t.get_yes_not_input("Want to continue")
>>> print(result)
True