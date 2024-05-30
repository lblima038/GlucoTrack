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
    
def nome_sistema():
    print("☼============================================☼")
    print("☼========= GlucoTrack (versão: 1.0) =========☼")
    print("☼============================================☼")
    print()