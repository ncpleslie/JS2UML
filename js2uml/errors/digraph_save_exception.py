"""==========================================
; Title:  Digraph Save Exception
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""


class DigraphSaveException(Exception):
    """For errors involving the process of saving a Digraph to the system"""

    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
