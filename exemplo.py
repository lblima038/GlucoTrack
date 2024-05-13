from dao.sexoDAO import SexoDAO
from entidades.usuario import Usuario
from dao.usuarioDAO import UsuarioDAO

from entidades.paciente import Paciente
from dao.pacienteDAO import PacienteDAO

from entidades.medicacao import Medicacao
from dao.medicacaoDAO import MedicacaoDAO

from entidades.tipo_diabete import TipoDiabete
from dao.tipoDiabeteDAO import TipoDiabeteDAO

from entidades.glicemia import Glicemia
from dao.glicemiaDAO import GlicemiaDAO

from datetime import datetime
import os

def listar_glicemia(codigo_paciente):
    limpa_tela()
    nome_sistema()

    pacienteDAO = PacienteDAO()
    glicemiaDAO = GlicemiaDAO()
    paciente = pacienteDAO.buscar_por_codigo(codigo_paciente)
    glicemias = glicemiaDAO.buscar_por_codigo_paciente(codigo_paciente)
    print("")
    print("Paciente: ", paciente.nome)
    for m in glicemias:
        print("========================================")
        print("Data: {:02d}/{:02d}/{:04d}".format(m.dia, m.mes, m.ano))
        print("Valor: ", m.valor)
    print("========================================")
    input("")

def cadastrar_glicemia(codigo_paciente):
    limpa_tela()
    nome_sistema()

    glicemiaDAO = GlicemiaDAO()

    data = input("Data (dd/mm/aaaa): ")
    nasc = datetime.strptime(data, '%d/%m/%Y')
    dia = nasc.day
    mes = nasc.month
    ano = nasc.year

    valor = int(input("Valor: "))

    glicemia = Glicemia(None, codigo_paciente, dia, mes, ano, valor)
    codigo = glicemiaDAO.inserir(glicemia)
    if codigo > 0:
        print("Glicemia incluida com sucesso!")
        input("")
    else:
        input("Erro na inclusão da glicemia")

def listar_medicacoes(codigo_paciente):
    limpa_tela()
    nome_sistema()

    pacienteDAO = PacienteDAO()
    medicacaoDAO = MedicacaoDAO()
    paciente = pacienteDAO.buscar_por_codigo(codigo_paciente)
    medicacoes = medicacaoDAO.buscar_por_codigo_paciente(codigo_paciente)
    print("")
    print("Paciente: ", paciente.nome)
    for m in medicacoes:
        print("========================================")
        print("Nome do remédio: ", m.nome)
        print("Hora inicial: ", m.hora_inicial)
        print("Periodicidade (horas): ", m.periodo)
        print("Lembrar: ", m.lembrar)
    print("========================================")
    input("")

def cadastrar_medicacoes(codigo_paciente):
    limpa_tela()
    nome_sistema()

    medicacaoDAO = MedicacaoDAO()

    nome = str(input("Nome do remédio: "))
    hora_inicial = str(input("Hora inicial: "))
    periodo = int(input("De quantas em quantas horas?: "))
    lembrar = str(input("Lembrar ? (S/N): "))

    medicacao = Medicacao(None, codigo_paciente, nome, hora_inicial, periodo, lembrar)
    codigo = medicacaoDAO.inserir(medicacao)
    if codigo > 0:
        print("Medicacão incluida com sucesso!")
        input("")
    else:
        input("Erro na inclusão da medicação")

def cadastrar_paciente(codigo_usuario):
    limpa_tela()
    nome_sistema()
    print("")

    pacienteDAO = PacienteDAO()
    tipoDiabeteDAO = TipoDiabeteDAO()
    sexoDAO = SexoDAO()

    nome = str(input("Nome: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (cm): "))
    nascimento = input("Data nascimento (dd/mm/aaaa): ")
    nasc = datetime.strptime(nascimento, '%d/%m/%Y')
    dia = nasc.day
    mes = nasc.month
    ano = nasc.year

    print("")
    print("Tipos de Diabete:")
    tipos_diabete = tipoDiabeteDAO.listar_todos()
    for tipo_diabete in tipos_diabete:
        print(tipo_diabete.codigo, " - ", tipo_diabete.descricao)
    print("")
    codigo_diabete = input("Informe seu tipo de diabete: ")

    print("")
    print("Sexo: ")
    sexos = sexoDAO.listar_todos()
    for sexo in sexos:
        print(sexo.codigo, " - ", sexo.descricao)
    print("")
    codigo_sexo = input("Informe seu sexo: ")

    paciente = Paciente(None, codigo_usuario, nome, dia, mes, ano, codigo_sexo, peso, altura, codigo_diabete)
    codigo_paciente = pacienteDAO.inserir(paciente)
    print("")
    input("Cadastro efetuado com sucesso")
    return codigo_paciente

def logar_usuario():

    limpa_tela()
    nome_sistema()    
    print("Logar Usuario")
    print("")
    email = str(input("Informe o email: "))
    senha = str(input("Informe sua senha: "))

    usuarioDAO = UsuarioDAO()
    codigo = usuarioDAO.logar(email, senha)
    if codigo == -1:
        input("email ou senha inválidos")
    else:
        print("")
        input("Usuario autenticado com sucesso")        

    return codigo

def cadastrar_usuario():
    
    limpa_tela()
    nome_sistema()

    usuarioDAO = UsuarioDAO()

    print("Cadastro de Usuario")
    print("")
    email = str(input("Informe seu email: "))
    senha = str(input("Informe sua senha: "))

    usuario = Usuario(None, email, senha)

    codigo_usuario = usuarioDAO.inserir(usuario)
    if codigo_usuario == -1:
        print("")
        print("Já existe um usuário com este email")
        input("pressione qualquer tecla")
        return
    elif codigo_usuario > 0:
        print("")
        print("Usuário cadastrado com sucesso!")
        input("Pressione qualquer tecla para voltar")

def tela_usuario_logado(codigo_usuario):
    limpa_tela()
    nome_sistema()
    menu_logado(codigo_usuario)

def escolha(codigo_usuario):
    opcao = int(input("Opção: "))
    match(opcao):
        case 1:
            pacienteDAO = PacienteDAO()
            paciente = pacienteDAO.buscar_por_codigo_usuario(codigo_usuario)
            cadastrar_medicacoes(paciente.codigo)
            tela_usuario_logado(codigo_usuario)
            escolha(codigo_usuario)

        case 2:
            pacienteDAO = PacienteDAO()
            paciente = pacienteDAO.buscar_por_codigo_usuario(codigo_usuario)
            listar_medicacoes(paciente.codigo)
            tela_usuario_logado(paciente.codigo)
            escolha(codigo_usuario)

        case 3:
            pacienteDAO = PacienteDAO()
            paciente = pacienteDAO.buscar_por_codigo_usuario(codigo_usuario)
            cadastrar_glicemia(paciente.codigo)
            tela_usuario_logado(paciente.codigo_usuario)
            escolha(codigo_usuario)

        case 4:
            pacienteDAO = PacienteDAO()
            paciente = pacienteDAO.buscar_por_codigo_usuario(codigo_usuario)
            listar_glicemia(paciente.codigo)
            tela_usuario_logado(paciente.codigo_usuario)
            escolha(codigo_usuario)

        case 99:
            exit()

        case _:
            escolha(codigo_usuario)

def menu_logado(codigo_usuario):
    pacienteDAO = PacienteDAO()
    paciente = pacienteDAO.buscar_por_codigo_usuario(codigo_usuario)
    print(paciente.nome)
    print("===================================")
    print("1  - Cadastrar medicações")
    print("2  - Listar medicações")
    print("3  - Cadastrar glicemia")
    print("4  - Listar glicemia")
    print("99 - Finalizar")
    print("")

def escolha_inicial():
    opcao = int(input("Opção: "))
    match(opcao):
        case 1:
            # Tentar logar no sistema
            codigo_usuario = logar_usuario()
            if codigo_usuario > 0:
                # logado com sucesso
                # verifica se já existe paciente registrado
                pacienteDAO = PacienteDAO()
                paciente = pacienteDAO.buscar_por_codigo_usuario(codigo_usuario)
                if paciente != None:
                    # paciente já registrado
                    tela_usuario_logado(paciente.codigo_usuario)
                    escolha(paciente.codigo_usuario)
                else:
                    limpa_tela()
                    nome_sistema()
                    print("Seja bem vindo ao GlucoTrack !")
                    print("")
                    print("Por favor, na próxima tela cadastre seus dados para que possamos montar seu perfil")
                    print("e, com isto, fazermos um acompanhamento suas medicações,  nível glicêmico, dieta e ")
                    print("saúde física.")
                    print("")
                    input("")
                    cadastrar_paciente(codigo_usuario)
                    tela_usuario_logado(codigo_usuario)
                    escolha(codigo_usuario)

        case 2:
            cadastrar_usuario()

        case 99:
            exit()

        case _:
            escolha_inicial()

def menu_inicial():
    print("1  - Entrar no sistema")
    print("2  - Cadastrar-se no sistema")
    print("99 - Finalizar")
    print("")

def nome_sistema():
    print("==============================================================================")
    print("======================== GlucoTrack - Versão 1.0 =============================")
    print("")

def limpa_tela():
    os.system('cls')

def main():
    limpa_tela()
    nome_sistema()
    menu_inicial()
    escolha_inicial()

if __name__ == '__main__':
    main()

