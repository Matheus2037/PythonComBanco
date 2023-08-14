import sqlite3
from sqlite3 import Error

def ConnectDB():
    DBPath = "C:\\Users\\Matheus\\Documents\\ProjetosPy\\PythonComBanco\\PRATICA01\\DB_TESTE01"
    connection = None
    try:
        connection = sqlite3.connect(DBPath)
    except Error as ex:
        print(ex)
    return connection

vcon = ConnectDB()

vsql="""INSERT INTO TB_PESSOAS
              (N_IDPessoa,T_NOMEPessoa,N_SALDO)
        VALUES('1','teste_nome','1000')"""

def insertData(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido!")
    except Error as ex:
        print(ex)

insertData(vcon, vsql)