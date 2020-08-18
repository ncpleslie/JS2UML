"""==========================================
; Title:  What we are looking for in a JS file
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""

from enum import Enum


class BodyType(Enum):
    METHOD = "MethodDefinition"
    CONSTRUCTOR = "constructor"
    NEW = "NewExpression"
