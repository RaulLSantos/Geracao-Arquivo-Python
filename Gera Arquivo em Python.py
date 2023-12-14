
from tkinter import *
import tkinter.messagebox 

import pandas as pd
import datetime
import pyodbc
import os
os.system('cls')

# Função que emite janela com mensagem de sucesso ao final da geração do arquivo
def popUp():
    tkinter.messagebox.showinfo("Finalizado!", "Arquivo gerado com sucesso.")


# Conectar ao banco de dados SQL Server
conexaobanco = pyodbc.connect('Driver={SQL Server};'
                      'Server= Nome + Instância SQL;'
                      'Database= Nome da Base;'
                      'UID= Usuário;'
                      'PWD= Senha;'
                      )

def Gera_Script():
    #Conecta ao banco
    cursor = conexaobanco.cursor()
    script_gera = """INSERIR SCRIPT AQUI"""
    # Executar o script SQL
    cursor.execute(script_gera)

    # Fechar a conexão com o banco de dados
    results = cursor.fetchall()

    
    data_atual = datetime.datetime.now()
    # Abaixo deve-se informar o caminho desejado para geração do arquivo. Ex: C:/user/raul/pastateste
    nome_arquivo = f'informar_caminho_para_gravaçaõ_do_arquivo_{data_atual.strftime("%d-%m-%Y_%H-%M")}.txt'
    
    # Gerar o arquivo com os resultados, se necessário
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        for row in results:
            file.write(','.join(str(value) for value in row) + '\n')
    popUp()
    
    
Gera_Script()
