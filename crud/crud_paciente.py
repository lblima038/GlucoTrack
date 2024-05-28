from entidades.paciente import Paciente
from util.util import converte_json_para_date
from util.util import converte_date_para_json
import json
import os

# caminho para o arquivo de dados no computador
arquivo = 'dados/pacientes.json'

    # se não existir o arquivo, cria um arquivo vazio
def _criar_bd():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f)

# método de uso interno:
# carrega todos os registros do arquivo para a memória
def _ler_todos():
    _criar_bd()

    with open(arquivo, 'r') as f:
        return json.load(f)

# método de uso interno:
# grava todos os registos para o arquivo
def _salvar_todos(registros):
    _criar_bd()

    with open(arquivo, 'w') as f:
        json.dump(registros, f, indent=4)

# insere um paciente no arquivo se não existir um paciente para o mesmo usuario
# devolve o código do paciente se gravou com sucesso.
# devolve -1 se já existir um paciente para o mesmo usuario
# devolve -2 se o paciente não tiver código de usuario associado
def _inserir(paciente):
    # valida se o campo codigo_usuario está preenchindo
    if paciente.codigo_usuario == None:
        print("Paciente sem códico de usuário")
        return -2
      
    pacientes = _ler_todos()
    # verifica se existe paciente com o mesmo codigo de usuario.
    for r in pacientes:
        if r['codigo_usuario'] == paciente.codigo_usuario:
            print("Já existe um paciente com este usuário cadastrado")
            return -1

    # converte a data de nascimento de datetime para string para poder salvar no arquivo
    data_nascimento = converte_date_para_json(paciente.data_nascimento)

    # procura o maior código de paciente cadastrado no banco para adicionar mais 1       
    proximo_codigo = 0
    for r in pacientes:
        if r['codigo'] > proximo_codigo:
            proximo_codigo = r['codigo']
            
    paciente_dic = { 'codigo':          proximo_codigo + 1, 
                     'codigo_usuario':  paciente.codigo_usuario, 
                     'nome':            paciente.nome, 
                     'data_nascimento': data_nascimento, 
                     'codigo_sexo':     paciente.codigo_sexo, 
                     'peso':            paciente.peso, 
                     'altura':          paciente.altura,
                     'codigo_diabete':  paciente.codigo_diabete }
    
    pacientes.append(paciente_dic)
    _salvar_todos(pacientes)
    return paciente_dic['codigo']

# insere um registro no arquivo.
# devolve o código se gravou com sucesso.
# devolve -1 se registro não for encontrado
def inserir_paciente(codigo_usuario, nome, data_nascimento, codigo_sexo, peso, altura, codigo_diabete):

    paciente = Paciente(None, codigo_usuario, nome, data_nascimento, codigo_sexo, peso, altura, codigo_diabete)

    return _inserir(paciente)

# faz uma busca no arquivo pelo paciente com o codigo especificado
# se encontrar devole o paciente encontrado
# se não encontrar devolve -1
def buscar_paciente(codigo):
    pacientes = _ler_todos()
    for r in pacientes:
        if r['codigo'] == codigo:
            # se encontrou converte a data de nascimento no formato string para o formato datetime
            data_nascimento = converte_json_para_date(r['data_nascimento'])
            
            return Paciente(r['codigo'], 
                            r['codigo_usuario'], 
                            r['nome'], 
                            data_nascimento, 
                            r['codigo_sexo'], 
                            r['peso'], 
                            r['altura'],
                            r['codigo_diabete'])

    print("Paciente não encontrado")
    return -1

# faz uma busca no arquivo pelo paciente com o codigo especificado
def buscar_paciente_por_codigo_usuario(codigo_usuario):
    pacientes = _ler_todos()
    for r in pacientes:
        if r['codigo_usuario'] == codigo_usuario:
            # se encontrou converte a data de nascimento no formato string para o formato datetime
            data_nascimento = converte_json_para_date(r['data_nascimento'])

            return Paciente(r['codigo'], 
                            r['codigo_usuario'], 
                            r['nome'], 
                            data_nascimento, 
                            r['codigo_sexo'], 
                            r['peso'], 
                            r['altura'],
                            r['codigo_diabete'])
        
    print("Paciente não encontrado")
    return -1

# atualiza um objeto paciente no banco
# se não encontrar devolve -1
def atualizar_paciente(codigo, codigo_usuario, nome, data_nascimento, codigo_sexo, peso, altura, codigo_diabete):

    paciente = Paciente(codigo, codigo_usuario, nome, data_nascimento, codigo_sexo, peso, altura, codigo_diabete)

    return _atualizar(paciente)

# atualiza um objeto paciente no banco
# se não encontrar devolve -1
def _atualizar(paciente):
    encontrou = False

    # carrega todos os registro do banco numa lista
    pacientes = _ler_todos()
    
    # percorre a lsita a procura do paciente com o codigo fornecido
    for r in pacientes:
        if r['codigo'] == paciente.codigo:
            r['nome'] = paciente.nome
            r['data_nascimento'] = converte_json_para_date(paciente.data_nascimento)
            r['codigo_sexo'] = paciente.codigo_sexo
            r['peso'] = paciente.peso
            r['altura'] = paciente.altura
            r['codigo_diabete'] = paciente.codigo_diabete
            encontrou = True
            break
        _salvar_todos(pacientes)
    
    # retorno True se atualizou com sucesso ou False se não encontrou o registro
    return encontrou

# remove um paciente do banco a partir do codigo especificado
def apagar_paciente(codigo):
    # carrega todos os registros do banco de daos para uma lista
    pacientes = _ler_todos()

    nova_lista_pacientes = []
    # percorre toda a lista removendo o paciente com o codigo especificado
    for paciente in pacientes:
        if paciente['codigo'] != codigo:
            nova_lista_pacientes.append(paciente)

    # grava lista no banco de dados
    _salvar_todos(nova_lista_pacientes)

def buscar_pacientes():
    pacientes = _ler_todos()
    lista_de_pacientes = []

    for r in pacientes:
        data_nascimento = converte_json_para_date(r['data_nascimento'])

        paciente = Paciente(r['codigo'], 
                            r['codigo_usuario'], 
                            r['nome'], 
                            data_nascimento, 
                            r['codigo_sexo'], 
                            r['peso'], 
                            r['altura'], 
                            r['codigo_diabete'])
        lista_de_pacientes.append(paciente)
        
    return lista_de_pacientes
