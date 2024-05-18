import json
from datetime import datetime
import os

def limpa_tela():
    os.system('cls')


limpa_tela()

def nome_registro_alimentos():
    print("=========================================================================================")
    print("======================== Registro de Alimentos - Versão 1.0 =============================")
    print("")

nome_registro_alimentos()

class RegistroNutricional(object):
    def __init__(self):
        self.registros = []

    def adicionar_registro(self):
        alimento = input("Nome do alimento: ")
        carboidratos = float(input("Carboidratos (em gramas): "))
        proteinas = float(input("Proteínas (em gramas): "))
        gorduras = float(input("Gorduras (em gramas): "))
        
        calorias = (carboidratos * 4) + (proteinas * 4) + (gorduras * 9)
        print(f"Calorias: {calorias}")

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        registro = {
            "Data e Hora": data_hora,
            "Alimento": alimento,
            "Carboidratos (g)": carboidratos,
            "Proteinas (g)": proteinas,
            "Calorias": calorias,
            "Gorduras (g)": gorduras
        }
        self.registros.append(registro)
        self.salvar_em_json("alimentos.json")

    def salvar_em_json(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'w') as file:
                json.dump(self.registros, file, indent=4)
            print("\nAlimento(s) registrado(s) com sucesso.")
        except Exception as e:
            print(f"Erro ao registrar o alimento: {e}")

registro = RegistroNutricional()
registro.adicionar_registro()
