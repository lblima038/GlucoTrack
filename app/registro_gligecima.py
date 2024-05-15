from dao.glicemiaDAO import GlicemiaDAO


def cadastrar_glicemia(codigo_paciente):

    data = input("Data : ")
    valor = int(input("Valor: "))

    # implemetar o código que extrai da variavel 'data' o valor do dia, do mes e do ano
    #
    #
    
    glicemiaDAO = GlicemiaDAO()
    glicemiaDAO.inserir(codigo_paciente, dia, mes, ano, valor)
