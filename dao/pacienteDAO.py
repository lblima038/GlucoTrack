from entidades.paciente import Paciente
import json
import os

# classe DAO para manipulação de pacientes no banco de dados (arquivos)
class PacienteDAO:

    # caminho para o arquivo de pacientes no computador
    arquivo = 'dados/pacientes.json'

    # construtor da classe
    # se não existir o arquivo, cria um arquivo vazio
    def __init__(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w') as f:
                json.dump([], f)

    # método de uso interno:
    # carrega todos os registros do arquivo para a memória
    def _ler_todos(self):
        with open(self.arquivo, 'r') as f:
            return json.load(f)

    # método de uso interno:
    # grava todos os registos para o arquivo
    def _grava_todos(self, registros):
        with open(self.arquivo, 'w') as f:
            json.dump(registros, f, indent=4)

    # insere um paciente no arquivo se não existir um paciente para o mesmo usuario
    # devolve o código do paciente se gravou com sucesso.
    # devolve -1 se já existir um paciente para o mesmo usuario
    def inserir(self, paciente):
        # valida se o campo codigo_usuario está preenchindo
        if paciente.codigo_usuario == None:
            return -2
        
        pacientes = self._ler_todos()
        # verifica se existe paciente com o mesmo codigo de usuario.
        for r in pacientes:
            if r['codigo_usuario'] == paciente.codigo_usuario:
                return -1
        
        proximo_codigo = 0
        for r in pacientes:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']
            
        paciente_dic = {'codigo': proximo_codigo + 1, 'codigo_usuario': paciente.codigo_usuario, 'nome': paciente.nome, 'diaNascimento': paciente.diaNascimento, 'mesNascimento': paciente.mesNascimento, 'anoNascimento': paciente.anoNascimento,'sexo': paciente.sexo, 'peso': paciente.peso, 'altura': paciente.altura}
        pacientes.append(paciente_dic)
        self._grava_todos(pacientes)
        return paciente_dic['codigo']

    # faz uma busca no arquivo pelo paciente com o codigo especificado
    def buscar_por_codigo(self, codigo):
        pacientes = self._ler_todos()
        for paciente in pacientes:
            if paciente['codigo'] == codigo:
                return Paciente(paciente['codigo'], paciente['codigo_usuario'], paciente['nome'], paciente['diaNascimento'], paciente['mesNascimento'], paciente['anoNascimento'], paciente['sexo'], paciente['peso'], paciente['altura'])
        return None

    # faz uma busca no arquivo pelo paciente com o codigo especificado
    def buscar_por_codigo_usuario(self, codigo_usuario):
        pacientes = self._ler_todos()
        for paciente in pacientes:
            if paciente['codigo_usuario'] == codigo_usuario:
                return Paciente(paciente['codigo'], paciente['codigo_usuario'], paciente['nome'], paciente['diaNascimento'], paciente['mesNascimento'], paciente['anoNascimento'], paciente['sexo'], paciente['peso'], paciente['altura'])
        return None

    def atualizar(self, paciente):
        pacientes = self._ler_todos()
        for r in pacientes:
            if r['codigo'] == paciente.codigo:
                r['nome'] = paciente.nome
                r['diaNascimento'] = paciente.diaNascimento
                r['mesNascimento'] = paciente.mesNascimento
                r['anoNascimento'] = paciente.anoNascimento
                r['sexo'] = paciente.sexo
                r['peso'] = paciente.peso
                r['altura'] = paciente.altura
                break
        self._grava_todos(pacientes)

    def apagar(self, codigo):
        pacientes = self._ler_todos()
        pacientes = [paciente for paciente in pacientes if paciente['codigo'] != codigo]
        self._grava_todos(pacientes)

    def fechar(self):
        return
    