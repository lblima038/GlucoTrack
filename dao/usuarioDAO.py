from entidades.usuario import Usuario
import json
import os

# classe DAO para manipulação de usuarios no banco de dados (arquivos)
class UsuarioDAO:

    # caminho para o arquivo de usuarios no computador
    arquivo = 'dados/usuarios.json'

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

    # insere um usuario no arquivo se não existir um usuário com o mesmo e-mail cadastrado
    def inserir(self, usuario):
        usuarios = self._ler_todos()
        # verifica se existe usuario com o mesmo email
        for r in usuarios:
            if r['email'] == usuario.email:
                return -1
        
        proximo_codigo = 0
        for r in usuarios:
            if r['codigo'] > proximo_codigo:
                proximo_codigo = r['codigo']
            
        usuario_dic = {'codigo': proximo_codigo + 1, 'email': usuario.email, 'senha': usuario.senha}
        usuarios.append(usuario_dic)
        self._grava_todos(usuarios)
        return usuario_dic['codigo']

    # faz uma busca no arquivo pelo usuário com o codigo especificado
    def buscar(self, codigo):
        usuarios = self._ler_todos()
        for usuario in usuarios:
            if usuario['codigo'] == codigo:
                return Usuario(usuario['codigo'], usuario['email'], usuario['senha'])
        return None

    def atualizar(self, usuario):
        usuarios = self._ler_todos()
        for r in usuarios:
            if r['codigo'] == usuario.codigo:
                r['email'] = usuario.email
                r['senha'] = usuario.senha
                break
        self._grava_todos(usuarios)

    def apagar(self, codigo):
        usuarios = self._ler_todos()
        usuarios = [usuario for usuario in usuarios if usuario['codigo'] != codigo]
        self._grava_todos(usuarios)

    def logar(self, email, senha):
        usuarios = self._ler_todos()
        for r in usuarios:
            if r['email'] == email:
                if r['senha'] == senha:
                    return r['codigo']
        return -1

    def fechar(self):
        return
    