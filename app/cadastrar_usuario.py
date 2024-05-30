from dao.usuarioDAO import UsuarioDAO
from entidades.usuario import Usuario
from util.util import limpa_tela, nome_sistema, menu_inicial

def cadastrar_usuario():
    
    limpa_tela()
    nome_sistema()

    usuarioDAO = UsuarioDAO()

    print("Cadastro de Usuario")
    print("")
    email = str(input("Informe seu email: "))
    while(email == ""):
        print("Email inválido!")
        email = str(input("Informe seu email: "))
    
    senha = str(input("Informe sua senha: "))
    while(senha == ""):
        print("Senha inválida!")
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
