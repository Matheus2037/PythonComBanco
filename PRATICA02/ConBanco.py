import sqlite3
from sqlite3 import Error

def Connection():
    DBpath = "C:\\Users\\Matheus\\Documents\\ProjetosPy\\PythonComBanco\\PRATICA02\\BANCODEDADOS"
    Connection = None

    try:
        Connection = sqlite3.connect(DBpath)
        print("Conexão realisada!")
    except Error as er:
        print(er)
    return Connection

vcon = Connection()