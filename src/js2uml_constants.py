"""==========================================
; Title:  Constants
; Author: Nick Leslie
; Date:   22/08/2020
=============================================
"""


class JS2UMLConstants:
    """For storage of the constants used throughout JS2UML
    """

    # Accepted file formats. strings
    __accepted_file_formats = [
        "bmp",
        "jpg",
        "jpeg",
        "pdf",
        "png",
        "svg",
        "webp",
    ]

    # supported input files
    __supported_files = ("js", "py")

    @classmethod
    def accepted_file_formats(cls) -> list:
        """A list of acceptable file formats

        Returns:
            list: String
        """
        return cls.__accepted_file_formats

    @classmethod
    def supported_files(cls) -> tuple:
        """A tuple of support file input files

        Returns:
            tuple: [String]
        """
        return cls.__supported_files
