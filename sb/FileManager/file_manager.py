from sb.Database.database import Database

from datetime import datetime
import os


class FileManager:
    def __init__(self) -> None:
        self.__ext = [".cpp", ".c", ".h"]
        self.db = Database()

    
    def __scanFiles(self, dir = './', files: dict = {}) -> tuple[list, dict]:
        sub_dir = []

        for f in os.scandir(dir):
            if f.is_dir():
                sub_dir.append(f.path)

            elif f.is_file():
                if os.path.splitext(f.name)[1].lower() in self.__ext:
                    files[f.path] = datetime.fromtimestamp(os.path.getmtime(f.path))
        
        for _dir in sub_dir:
            s_dir, fs = self.__scanFiles(_dir)
            sub_dir.extend(s_dir)

            for f in fs:
                files[f] = datetime.fromtimestamp(os.path.getmtime(f))

    

        return sub_dir, files


    def getFiles(self, dir = './'):
        _, f = self.__scanFiles(dir)

        return f
    

    def getFilesAndDirs(self, dir = "./"):
        d, f = self.__scanFiles(dir)

        return d, f 
    

    def updateChanges(self, includes: list) -> list:
        self.db.connect()

        if not includes:
            self.db.removeAllFiles()
            return []
        
        changes = []
        dirs, files = self.__scanFiles(includes[0])

        if len(includes) > 1:
            for include in includes[1:]:
                if not include in dirs:
                    d, _  = self.__scanFiles(include, files)

                    dirs.extend(d)


        db_files = self.db.getIncludes()

        # UPDATE CHANGES
        for f in files:
            if db_files.get(f):
                # Compare Datetimes
                if str(files[f]) != db_files[f]:
                    changes.append(f)
                    self.db.updateFile(f, files[f])

            else:
                changes.append(f)
                self.db.addFile(f, files[f])

        # REMOVE FILES THAT ARE EXCLUDED FROM INCLUDES
        # OR PATH CHANGED
        db_files_list = [f for f in db_files]
        for f in db_files_list:
            if not files.get(f):
                self.db.removeFile(f)



        return changes