"""==========================================
; Title:  Controller and CLI for JS2UML
; Author: Nick Leslie
; Date:   12/08/2020
=============================================
"""
from cmd import Cmd
from src.io.read_write import ReadWrite


class CommandLine(Cmd):
    intro = "JS2UML - A CLI application for converting JavaScript (ECMAScript 2015+) and TypeScript to UML class diagrams.\nType help or ? to list commands.\nIf this is your first time running this program, please run 'setup'"
    prompt = "JS2UML >>> "

    def __init__(self, controller):
        super().__init__(self)
        self._controller = controller

    def do_setup(self, arg):
        print('Failed set up')

    def do_parse(self, arg):
        'THIS IS A STRING THAT NEEDS TO BE REPLACED'
        self._controller.run()
