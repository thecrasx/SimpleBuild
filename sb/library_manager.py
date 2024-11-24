from sb.gcc_prompt import GCCPrompt
from sb.utils import get_name
import os


class LibraryManager:
    def __init__(self, dir: str = "./.sb/lib") -> None:
        if dir[-1] != '/':
            dir += '/'

        self.__dir = dir
        self.gcc = GCCPrompt(True)


    @property
    def dir(self) -> str:
        return self.__dir
    

    def extractNames(self, libs: list) -> list:
        out = []

        for lib in libs:
            if lib != '':

                if '/' in lib:
                    lib = lib.split('/')[-1]
                
                if "lib" == lib[:3]:
                    lib = lib[3:]

                elif 'l' == lib[0]:
                    lib = lib[1:]

                if '.' in lib:
                    lib = lib.split('.')[0]

            out.append(lib)

        return out

 
    def getLibraries(self, full_path = False) -> list:
        libs = os.listdir(self.dir)

        if full_path:
            for i in range(len(libs)):
                libs[i] = self.__dir + libs[i]

        return libs
    

    def getUnnecessary(self, sources: list, config_libs: list):
        s_names = self.extractNames(sources)
        cl_names = self.extractNames(config_libs)

        libs = self.getLibraries(True)
        l_names = self.extractNames(libs)

        out = []

        for i in range(len(l_names)):
            if not l_names[i] in s_names and not l_names[i] in cl_names:
                out.append(libs[i])


        return out
    

    def removeUnnecessary(self, sources: list, config_libs: list):
        u_libs = self.getUnnecessary(sources, config_libs)

        for lib in u_libs:
            os.remove(lib)


    def makeDynamicLibrary(self, source, includes: list = []):
        if not os.path.exists(source):
            raise FileNotFoundError

        output = get_name(source, True) + ".o"
        lib_name = "lib" + get_name(source, True) + ".a"

        self.gcc.addCompile(source)

        for include in includes:
            self.gcc.addInclude(include)

        self.gcc.addOutput(f"{self.__dir}{output}")
        self.gcc.run()

        os.system(f"ar cr {self.__dir}{lib_name} {self.__dir}{output}")

        try:
            os.remove(f"{self.__dir}{output}")
        except:
            pass