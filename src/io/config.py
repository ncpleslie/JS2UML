"""==========================================
; Title:  Config Saver/Loader
; Author: Nick Leslie
; Date:   18/08/2020
=============================================
"""

from pickle import Pickler, dump, load
from os import path
from src.js2uml_constants import JS2UMLConstants


class Config(Pickler):
    """Will store the users configs on the device
    """

    # The preferred storage name
    __pickle = "config"

    # The preferred file type
    __accepted_file_formats = JS2UMLConstants.accepted_file_formats()

    @classmethod
    def get_default_filename(cls) -> str:
        """Returns the default filename

        Returns:
            str: default filename

        >>> result = Config.get_default_filename()
        >>> print(result)
        filename
        """
        return cls.__open('default_filename')

    @classmethod
    def get_default_filetype(cls) -> str:
        """Returns default filetype

        Returns:
            str: default filetype
        >>> result = Config.get_default_filetype()
        >>> print(result)
        png
        """
        return cls.__open('default_filetype')

    @classmethod
    def get_default_storage_location(cls) -> str:
        """Returns default storage location

        Returns:
            str: default storage location

        >>> result = Config.get_default_storage_location()
        >>> print(result)
        tests
        """
        return cls.__open('storage_location')

    @classmethod
    def set_default_filename(cls, default_filename: str) -> None:
        """Sets the default filename

        Args:
            default_filename (str): filename

        >>> Config.set_default_filename("filename")
        """
        if default_filename:
            filename_dict = {'default_filename': default_filename}
            cls.__save(filename_dict)

    @classmethod
    def set_default_filetype(cls, default_filetype: str) -> None:
        """Sets the default filetype

        Args:
            default_filetype (str): filetype

        Raises:
            IOError: if wrong file type
        >>> Config.set_default_filetype("png")
        """
        if default_filetype and default_filetype in cls.__accepted_file_formats:
            filetype_dict = {'default_filetype': default_filetype}
            cls.__save(filetype_dict)
        else:
            raise IOError('Wrong file type')

    @classmethod
    def set_default_storage_location(cls, storage_location: str) -> None:
        """Sets default storage location

        Args:
            storage_location (str): default storage location
        >>> Config.set_default_storage_location("tests")
        """
        if storage_location:
            storage_dict = {'storage_location': storage_location}
            cls.__save(storage_dict)

    @classmethod
    def __open(cls, data_name):
        """Opens the pickle config

        Args:
            data_name ([string]): name of pickle

        Raises:
            error: if file not found

        Returns:
            [string]: the config
        """
        try:
            with open(path.join(path.realpath('.'), 'config', data_name), 'rb') as config:
                new_data = load(config)
                if new_data and new_data[data_name]:
                    return new_data[data_name]
        except FileNotFoundError as error:
            raise error

    @classmethod
    def __save(cls, data) -> None:
        """Saves the config

        Args:
            data ([type]): The current config to be saved

        Raises:
            error: IOerror, OSError if unable to save
        """
        try:
            with open(path.join(path.realpath('.'), 'config', list(data.keys())[0]), 'wb') as config:
                dump(data, config)
        except (IOError, OSError) as error:
            raise error
