"""==========================================
; Title:  JSParse Exception
; Author: Nick Leslie
; Date:   18/10/2020
=============================================
"""


class JSParseException(Exception):
    """For errors involving the process of parsing a JS file"""

    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
