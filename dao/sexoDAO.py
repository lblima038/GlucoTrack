from entidades.sexo import Sexo
import json
import os

# classe DAO para manipulação de usuarios no banco de dados (arquivos)
class SexoDAO:

    # caminho para o arquivo de dados no computador
    arquivo = 'dados/sexo.json'

    # construtor da classe
    # se não existir o arquivo, cria um arquivo vazio
    def __init__(self):
        if not os.path.exists(self.arquivo):
            tipos = [ { "codigo": 1, "descricao": "Feminino" },
                      { "codigo": 2, "descricao": "Masculino" },
                      { "codigo": 3, "descricao": "Não especificado" }]

            with open(self.arquivo, 'w') as f:
                json.dump([], f)

            self._grava_todos(tipos)

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

    # devolve o objeto no banco a partir do codigo especificado
    # se não encontrar retona None
    def buscar(self, codigo):
        sexos = self._ler_todos()
        for sexo in sexos:
            if sexo['codigo'] == codigo:
                return Sexo(sexo['codigo'], sexo['descricao'])
        return None

    # retorna um array com todos os registros do banco
    def listar_todos(self):
        sexos_bd = self._ler_todos()
        sexos = []
        for reg in sexos_bd:
            sexo = Sexo(reg['codigo'], reg['descricao'])
            sexos.append(sexo)
        return sexos
        
    # fecha a tabela do banco.
    # em base de dados em arquivos, nao faz nada. Mantida para uso futuro em bases que nao forem baseadas em arquivos
    def fechar(self):
        pass
    