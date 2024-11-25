from sb.FileManager.file_manager import FileManager
from sb.library_manager import LibraryManager
from sb.gcc_prompt import GCCPrompt
from sb.config import Config
from sb.utils import get_name

import os
import click


class SimpleBuild:
    def __init__(self):
        self.config = Config()
        self.config.load()

        self.gcc = GCCPrompt(self.config.data["cpp"])
        self.fileManager = FileManager()
        self.libraryManager = LibraryManager()


    def build(self):
        includes = self.config.data["Include"]["paths"]

        changes = self.fileManager.updateChanges(includes)
        source_changes = []

        sources = [f for f in self.fileManager.db.getFiles() if ".c" in f or ".cpp" in f]
        self.fileManager.db.close()

        main = self.config.data["main"].replace(' ', '')
        
        if not main:
            click.echo("Main not included in config.toml")
            return
        

        # BUILD PATH
        output_path = self.config.data["output_path"]

        if output_path.replace(' ', '') != "":
            if output_path[-1] != "/":
                output_path += '/'

        else:
            if not os.path.exists("./build"):
                os.mkdir("./build")

            output_path = "./build/"


        # GET CHANGES
        for c in changes:
            if ".c" in c or ".cpp" in c:
                if c != main:
                    source_changes.append(c)

        for sc in source_changes:
            self.libraryManager.makeDynamicLibrary(sc, includes)

        self.libraryManager.removeUnnecessary(sources, self.config.data["Libraries"]["include"])

        # ADD MAIN
        self.gcc.addMain(main)

        # ADD OTHER
        self.gcc.add(self.config.data["Other"]["other"])

        # ADD LIBRARY DIR
        self.gcc.addIncludeLibrary(self.libraryManager.dir)

        # ADD LIBRARIES
        config_libs = self.libraryManager.extractNames(self.config.data["Libraries"]["include"])
        libraries = self.libraryManager.extractNames(self.libraryManager.getLibraries())

        for cl in config_libs:
            self.gcc.addLibrary(cl)


        for l in libraries:
            if not l in config_libs:
                self.gcc.addLibrary(l)


        # ADD INCLUDES
        for include in includes:
            self.gcc.addInclude(include)


        # OUTPUT
        self.gcc.addOutput(output_path + get_name(main, True))

        print_line = "".join(['-' for i in range(len(self.gcc.input))])
        print(print_line)
        print(self.gcc.input)
        print(print_line)
        print("\n")
        self.gcc.run()