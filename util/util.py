from datetime import date
import os

def converte_json_para_date(data_json):
    dia = data_json[:2]
    mes = data_json[3:5]
    ano = data_json[6:10]

    data_date = date(int(ano), int(mes), int(dia))
    
    return data_date

def converte_date_para_json(data_date):
    dia = data_date.day
    mes = data_date.month
    ano = data_date.year

    data_json = str(dia) + "/" + str(mes) + "/" + str(ano)

    return data_json

def limpa_tela():
    os.system("cls")

def tela_inicial():
    limpa_tela()
    nome_sistema()
    menu_inicial()
    
def menu_inicial():
    print("1 - Entrar no sistema")
    print("2 - Cadastrar-se no sistema")
    print("0 - Finalizar")
    print("")

def nome_sistema():
    print("==============================================================================")
    print("======================== GlucoTrack - Versão 1.0 =============================")
    print("")
