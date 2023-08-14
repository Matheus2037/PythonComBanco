import sqlite3
from sqlite3 import Error

def ConnectDB():
    DBPath = "C:\\Users\\Matheus\\Documents\\ProjetosPy\\PythonComBanco\\codigos\\DB_TESTE01"
    connection = None
    try:
        connection = sqlite3.connect(DBPath)
    except Error as ex:
        print(ex)
    return connection

vcon = ConnectDB()

vsql="""CREATE TABLE TB_PESSOAS2(
        N_IDPessoa INTEGER PRIMARY KEY AUTOINCREMENT,
        T_NOMEPessoa VARCHAR (30),
        N_SALDO INTEGER
        );"""

def create_table(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada!")
    except Error as ex:
        print(ex)
    

create_table(vcon,vsql) 
    
vcon.close()