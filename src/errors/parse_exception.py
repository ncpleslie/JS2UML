"""==========================================
; Title:  JSParse Exception
; Author: Nick Leslie
; Date:   18/10/2020
=============================================
"""


class ParseException(Exception):
    """For errors involving the process of parsing a file"""

    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
