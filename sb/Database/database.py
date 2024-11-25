from sb.Database.db_schema import *
from datetime import datetime
import sqlite3
import os


class Database:
    def __init__(self) -> None:
        self.__conn = None
        self.__cur = None
        self.connect()


    @property
    def conn(self):
        return self.__conn


    @property
    def cur(self):
        return self.__cur


    def connect(self):
        if not self.__conn:
            self.__conn = sqlite3.connect("./.sb/database.db")
            self.__cur = self.conn.cursor()
    

    def close(self):
        if self.__conn:
            self.conn.close()


    def addTables(self):
        self.cur.execute(t_config)
        self.cur.execute(t_includes)
        self.conn.commit()


    def addFile(self, path, date_modified):
        self.cur.execute("INSERT INTO Includes (file, date_modified) VALUES (?,?)", (path, date_modified,))
        self.conn.commit()


    def updateFile(self, path, date_modified):
        self.cur.execute("UPDATE Includes SET date_modified = ? WHERE file IS ?", (date_modified, path,))
        self.conn.commit()


    def removeFile(self, path):
        self.cur.execute("DELETE FROM Includes WHERE file IS ?", (path,))
        self.conn.commit()


    def removeAllFiles(self):
        self.cur.execute("DROP TABLE Includes")
        self.addTables()
        self.conn.commit()


    # GET FILES WITHOUT MODIFIED DATE
    def getFiles(self) -> list:
        self.cur.execute("SELECT * FROM Includes")

        data = self.cur.fetchall()
        out = []

        for d in data:
            out.append(d[0])

        return out


    # GET FILES WITH MODIFIED DATE
    def getIncludes(self) -> dict:
        includes = {}

        self.cur.execute("SELECT * FROM Includes")

        data = self.cur.fetchall()

        for d in data:
            includes[d[0]] = d[1]

        return includes