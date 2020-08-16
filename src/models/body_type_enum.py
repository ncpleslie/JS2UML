from enum import Enum


class BodyType(Enum):
    METHOD = "MethodDefinition"
    CONSTRUCTOR = "constructor"
    NEW = "NewExpression"
