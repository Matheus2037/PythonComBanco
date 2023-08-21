import ConBanco as DBCON
import sqlite3
from sqlite3 import Error

DBCON.vcon

id = 1
nome = "Matheus"
saldo = 100000
dados=(id, nome, saldo)

vsql="""CREATE TABLE TB_PESSOAS(
        N_IDPessoa INTEGER PRIMARY KEY AUTOINCREMENT,
        T_NOMEPessoa VARCHAR (30),
        N_SALDO INTEGER
        );"""
vatt= """UPDATE TB_PESSOAS SET N_IDPessoa = ?, T_NOMEPessoa = ?, N_SALDO = ? """

def ADICIONARVALORES(conexao,sql,data):
    try:
        c=conexao.cursor()
        c.execute(sql, data)
        DBCON.vcon.commit()
        print("DADOS CADASTRADOS!")
    except Error as ex:
        print(ex)

teste = ADICIONARVALORES(DBCON.vcon, vatt, dados)
    
