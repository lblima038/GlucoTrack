from dao.pacienteDAO import PacienteDAO
from entidades.paciente import Paciente 
from crud.crud_paciente import inserir_paciente, buscar_paciente_por_codigo_usuario

from util.util import limpa_tela, nome_sistema
from util.util import validar_email

# cadastra usuario com email e senha
def cadastrar_paciente(codigo_usuario):
    
    limpa_tela()
    nome_sistema()

    print("Cadastro de Paciente")
    print()

    nome = input("Nome: ")
    
    idade = int(input("Idade: "))

    codigo_sexo = input("Sexo (F/M): ")
    while(codigo_sexo.upper() != 'F' and codigo_sexo.upper() != 'M'):
        codigo_sexo = input("Sexo (F/M): ")

    peso = int(input("Peso (kg): "))

    altura = int(input("Altura (cm): "))

    print("informe qual o tipo de diabetes é acometido.")
    print("1 - Tipo 1")
    print("2 - Tipo 2")
    print("3 - Gestacional")
    print("4 - Outra")
    print("5 - Não possui")
    codigo_diabete = input("Tipo de diabetes: ")
    while(codigo_diabete < '1' and codigo_diabete > '5'):
        codigo_diabete = input("Tipo de diabetes: ")

    comorbidades = input("Comorbidades: ")

    resultado = inserir_paciente(codigo_usuario, nome.upper(), idade, codigo_sexo.upper(), peso, altura, codigo_diabete, comorbidades)

    if resultado == -1:
        print()
        print("Já existe um usuário com este email")
        input("pressione qualquer tecla")
        return
    elif codigo_usuario > 0:
        print()
        print("Usuário cadastrado com sucesso!")
        input("Pressione qualquer tecla para voltar")

def listar_dados_paciente(codigo_usuario):
    limpa_tela()
    nome_sistema()

    paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)
    
    print("Nome: ", paciente.nome)
    print("Idade: ", paciente.idade)
    print("Sexo: ", paciente.codigo_sexo)
    print("Peso: ", paciente.peso)
    print("Altura: ", paciente.altura)
    print("IMC: ", (paciente.peso / ((paciente.altura/100.0) * (paciente.altura/100.0))))
    print("Tipo diabetes: ", paciente.codigo_diabete)
    print("Comorbidades: ", paciente.comorbidades)
    print()
    input("Deseja alterar? (S/N): ")
