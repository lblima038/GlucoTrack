from dao.glicemiaDAO import GlicemiaDAO
from datetime import datetime
from util.util import listar_dados, menu_padrao

def tela_glicemia(codigo_paciente):
    menu_padrao("Home > Glicemia", [
        "Registrar nova aferição", lambda: cadastrar_glicemia(codigo_paciente),
        "Lista de aferições", lambda: listar_aferições,
    ])
    pass

def cadastrar_glicemia(codigo_paciente):
    data = input("Informe a data do registro de glicose (dd/mm/aaaa): ")
    conv = datetime.strptime(data, '%d/%m/%Y')
    dia = conv.day
    mes = conv.month
    ano = conv.year
    print("Data registrada: ", conv.day, "/", conv.month, "/", conv.year)

    valor_glicêmico = int(input("Indique o valor de glicose registrada: "))
    print("Valor: ", valor_glicêmico)

    glicemiaDAO = GlicemiaDAO()
    glicemiaDAO.inserirPorDados(codigo_paciente, dia, mes, ano, valor_glicêmico)

def listar_aferições(codigo_paciente):
    pass