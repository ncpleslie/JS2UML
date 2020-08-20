if __name__ == "__main__":
    import doctest
    import src.converter.js_parser
    print('Testing JS Parser')
    doctest.testmod(src.converter.js_parser)
    print('Testing Digraph_Converter')
