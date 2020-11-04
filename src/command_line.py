"""==========================================
; Title:  Controller and CLI for JS2UML
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""
from cmd import Cmd


class CommandLine(Cmd):
    intro = "\nJS2UML - Convert JavaScript "\
        "(ECMAScript 2015+) to UML class diagrams."\
        "\nType help or ? to list commands."\
        "\nType help <command> for detailed information\n"
    prompt = "JS2UML >>> "

    def __init__(self, controller):
        super().__init__(self)
        self._controller = controller

    def do_exit(self, arg):
        "Exits the command line"
        self._controller.exit()

    def do_help(self, arg):
        if arg:
            super().do_help(arg)
        else:
            self._controller.help()

    def do_change(self, arg):
        """Change which files can be parsed. Currently supported are JavaScript and Python"""
        self._controller.change()

    def do_setup(self, arg):
        "Setup allows you initialise the program and set the configurations "\
            "you want. These include default input directory, "\
            "default output file type, default output name.\n\n"\
            "Expected use: \n"\
            "`setup -f <default filename or directory> -o <default output>"\
            "-t <default filetype>` "\
            "or simply, `setup`."\
            "\n\nSupported output types: \n"\
            "'bmp', 'jpg', 'jpeg', 'pdf', 'png', 'svg', 'webp'. \n"
        self._controller.setup(arg)

    def do_parse(self, arg):
        "Call this to parse any JS file to a UML class diagram. "\
            "You can exclude the option arguments(filename or directory, "\
            "the output path and filetype) but the system will ask "\
            "for you them anyway. \n\nSupported output types: \n"\
            "'bmp', 'jpg', 'jpeg', 'pdf', 'png', 'svg', 'webp'. \n\n"\
            "Expected use: \n"\
            "`parse -f <filename or directory> -o <output> -t <filetype>` "\
            "or simply, `parse`.\n"
        self._controller.parse(arg)
