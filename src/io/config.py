"""==========================================
; Title:  Config Saver/Loader
; Author: Nick Leslie
; Date:   18/08/2020
=============================================
"""

from pickle import Pickler, dump, load


class Config(Pickler):
    """Will store the users configs on the device
    """

    # The preferred storage name
    __pickle = "config.pkl"

    # The preferred file type
    __accepted_file_formats = [
        "bmp",
        "jpg",
        "jpeg",
        "pdf",
        "png",
        "svg",
        "webp",
    ]

    @classmethod
    def get_default_filename(cls) -> str:
        """Returns the default filename

        Returns:
            str: default filename
        """
        return cls.__open('default_filename')

    @classmethod
    def get_default_filetype(cls) -> str:
        """Returns default filetype

        Returns:
            str: default filetype
        """
        return cls.__open('default_filetype')

    @classmethod
    def get_default_storage_location(cls) -> str:
        """Returns default storage location

        Returns:
            str: default storage location
        """
        return cls.__open('storage_location')

    @classmethod
    def set_default_filename(cls, default_filename: str):
        """Sets the default filename

        Args:
            default_filename (str): filename
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
        """
        if storage_location:
            storage_dict = {'storage_location': storage_location}
            cls.__save(storage_dict)

    @classmethod
    def __open(cls, data_name):
        """Opens the pickle config

        Args:
            data_name ([type]): name of pickle

        Raises:
            error: if file not found

        Returns:
            [type]: the config
        """
        try:
            with open(cls.__pickle, 'rb') as pickle:
                new_data = load(pickle)
                if new_data:
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
            with open(cls.__pickle, 'wb') as pickle:
                dump(data, pickle)
        except (IOError, OSError) as error:
            raise error
