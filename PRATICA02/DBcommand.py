import ConBanco as DBCON
import sqlite3
from sqlite3 import Error
DBCON.vcon

option = int(input("Digite qual ação deseja realizar: "
                   "\n1-Inserir valores"
                   "\n2-Alterar valores"
                   "\n3-Excluir valores"
                   "\n4-Filtrar valores\n"))

if option == 1:
    comando_temp = """INSERT INTO TB_PESSOAS
                        (T_NOMEPessoa,N_SALDO)
                        VALUES('Robson','90000')"""
elif option == 2:
    comando_temp = """UPDATE TB_PESSOAS 
                        SET T_NOMEPessoa = 'João', N_SALDO = 47500 WHERE N_IDPessoa = 2"""
elif option == 3:
    comando_temp = "DELETE FROM TB_PESSOAS WHERE N_IDPessoa = 1"
elif option == 4:
    comando_temp = "SELECT T_NOMEPessoa,N_SALDO FROM TB_PESSOAS WHERE N_IDPessoa = 2"

vsql = comando_temp


def Commands(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        if option == 4:
            resultado = c.fetchone()
            nome, saldo = resultado
            if resultado != "":
                print(f"O resultado da busca foi o usuário: {nome}, com saldo de {saldo}")
            else:
                print("Nenhum usuário encontrado!")
        print("Comando Executado com sucesso!")
    except Error as ex:
        print(ex)


Commands(DBCON.vcon,vsql)