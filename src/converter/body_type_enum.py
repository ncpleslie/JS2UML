"""==========================================
; Title:  What we are looking for in a JS file
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from enum import Enum


class BodyType(Enum):
    """The different types of parts of a parsed JS file
    """

    # The string representation of a method
    METHOD = "MethodDefinition"

    # The string representation of a constructor
    CONSTRUCTOR = "constructor"

    # The string representation of a new object
    NEW = "NewExpression"
