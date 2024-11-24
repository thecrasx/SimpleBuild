from os import system


class GCCPrompt:
    def __init__(self, cpp = False):
        self.__cpp = cpp
        self.__setupInput()


    @property
    def input(self):
        return self.__input


    def __setupInput(self):
        if self.__cpp:
            self.__input = "g++"
        else:
            self.__input = "gcc"


    def clear(self):
        self.__setupInput()


    def run(self):
        system(self.__input)
        self.clear()


    def add(self, text: str):
        self.__input += f" {text}"


    def addMain(self, path):
        self.__input += f" {path}"


    def addOutput(self, path):
        self.__input += f" -o {path}"


    def addInclude(self, path):
        self.__input += f" -I {path}"


    def addIncludeLibrary(self, path):
        self.__input += f" -L {path}"


    def addLibrary(self, lib: str):
        if lib[0] != 'l':
            lib = 'l' + lib

        self.__input += f" -{lib}"


    def addCompile(self, path):
        self.__input += f" -c {path}"


    def setStatic(self):
        self.__input += " -static"