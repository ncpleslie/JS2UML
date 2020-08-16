from pickle import Pickler, dump, load


class Config(Pickler):
    __pickle = "config.pkl"
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
        return cls.__open('default_filename')

    @classmethod
    def get_default_filetype(cls) -> str:
        return cls.__open('default_filetype')

    @classmethod
    def get_default_storage_location(cls) -> str:
        return cls.__open('storage_location')

    @classmethod
    def set_default_filename(cls, default_filename: str):
        if default_filename:
            filename_dict = {'default_filename': default_filename}
            cls.__save(filename_dict)

    @classmethod
    def set_default_filetype(cls, default_filetype: str):
        if default_filetype and default_filetype in cls.__accepted_file_formats:
            filetype_dict = {'default_filetype': default_filetype}
            cls.__save(filetype_dict)
        else:
            raise IOError('Wrong file type')

    @classmethod
    def set_default_storage_location(cls, storage_location: str) -> None:
        if storage_location:
            storage_dict = {'storage_location': storage_location}
            cls.__save(storage_dict)

    @classmethod
    def __open(cls, data_name):
        try:
            with open(cls.__pickle, 'rb') as pickle:
                new_data = load(pickle)
                if new_data:
                    return new_data[data_name]
        except FileNotFoundError as error:
            raise error

    @classmethod
    def __save(cls, data) -> None:
        try:
            with open(cls.__pickle, 'wb') as pickle:
                dump(data, pickle)
        except (IOError, OSError) as error:
            raise error
