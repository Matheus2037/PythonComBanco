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
    nome_Temp = input("Digite o nome do usuário: ")
    saldo_Temp = int(input("Digite o saldo do usuário: "))
    dados_Temp = (nome_Temp,saldo_Temp)

    comando_temp = """INSERT INTO TB_PESSOAS
                        (T_NOMEPessoa,N_SALDO)
                        VALUES(?,?)"""
    
elif option == 2:
    id_Temp = int(input("Digite o ID do usuário que irá modificar: "))
    nome_Temp = input("Digite o nome do usuário: ")
    saldo_Temp = int(input("Digite o saldo do usuário: "))
    dados_Temp = (nome_Temp,saldo_Temp,id_Temp)

    comando_temp = """UPDATE TB_PESSOAS 
                        SET T_NOMEPessoa = ?, N_SALDO = ? WHERE N_IDPessoa = ?"""
    
elif option == 3:
    id_Temp = int(input("Digite o ID do usuário que irá deletar: "))
    dados_Temp = (id_Temp,)

    comando_temp = "DELETE FROM TB_PESSOAS WHERE N_IDPessoa = ?"

elif option == 4:
    id_Temp = int(input("Digite o ID do usuário que irá modificar: "))
    dados_Temp = (id_Temp,)

    comando_temp = "SELECT T_NOMEPessoa,N_SALDO FROM TB_PESSOAS WHERE N_IDPessoa = ?"

vsql = comando_temp


def Commands(conexao,sql,data):
    try:
        c=conexao.cursor()
        c.execute(sql, data)
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


Commands(DBCON.vcon,vsql,dados_Temp)