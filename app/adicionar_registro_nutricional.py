from crud.crud_registro_nutricional import inserir_registro_nutricional
from util.util import limpa_tela, nome_sistema
import json
from datetime import datetime

# tela de adição de registro nutricional 
def adicionar_alimentos(codigo_paciente):
    limpa_tela()
    nome_sistema()
    print("Registro de Alimentos")
    print("")

    data_hora = datetime.now()
    alimento = input("Nome do alimento        : ")
    carboidratos = float(input("Carboidratos (em gramas): "))
    proteinas = float(input("Proteínas (em gramas)   : "))
    gorduras = float(input("Gorduras (em gramas)    : "))

    calorias = (carboidratos * 4) + (proteinas * 4) + (gorduras * 9)
    print(f"Calorias                : {calorias}")

    resultado = inserir_registro_nutricional(codigo_paciente, data_hora, calorias, proteinas, gorduras, carboidratos)
    if resultado <= 0:
        input("ERRO na inclusão do registro nutricional !")
    else:
        input("Registro cadastrado com sucesso!")

