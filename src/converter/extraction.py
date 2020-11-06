class Extraction:
    """
        The returned product from a code parser. 
        Can be converted to a Digraph object
    """

    def __init__(self):
        self.__class_name = None
        self.__methods = None
        self.__attributes = None
        self.__relationships = None

    def set_name(self, name: str) -> None:
        """Set the class name"""
        self.__class_name = name

    def set_methods(self, methods: list) -> None:
        """Set the methods list"""
        self.__methods = methods

    def set_attributes(self, attributes: list) -> None:
        """Set the attributes list"""
        self.__attributes = attributes

    def set_relationships(self, relationships: list) -> None:
        """Set the relationships set"""
        self.__relationships = relationships

    def get_class_name(self) -> str:
        """Returns the class name"""
        return self.__class_name

    def get_methods(self) -> list:
        """Returns the methods list"""
        return self.__methods

    def get_attributes(self) -> list:
        """Returns the attributes list"""
        return self.__attributes

    def get_relationships(self) -> set:
        """Returns the relationships set"""
        return self.__relationships
