from entidades.usuario import Usuario
from entidades.paciente import Paciente
from dao.usuarioDAO import UsuarioDAO
from dao.pacienteDAO import PacienteDAO
import os

codigoUsuario = -1

def tela_usuario_logado():
    limpa_tela()
    nome_sistema()
    menu_logado()

def cadastrar_paciente():
    limpa_tela()
    nome_sistema()

    pacienteDAO = PacienteDAO()

    paciente = Paciente(None, codigoUsuario, nome, 0, 0, 0, "M", peso, altura)
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))

    pacienteDAO.inserir(paciente)

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
        print("Usuario ", codigo, " autenticado com sucesso")
        input("")

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
        print("Já existe um usuário com este email")
        input("pressione qualquer tecla")
        return
    elif codigo_usuario > 0:
        print("Usuário cadastrado com sucesso!")
        input("Pressione qualquer tecla para voltar")

def nome_sistema():
    print("================================================================================")
    print("======================== GlucoTracker - Versão 1.0 =============================")
    print("")

def menu_inicial():
    print("1  - Cadastrar-se no sistema")
    print("2  - Entrar no sistema")
    print("99 - Finalizar")
    print("")

def menu_logado():
    print("3  - Cadastrar paciente")
    print("99 - Finalizar")
    print("")

def escolha():
    opcao = int(input("Opção: "))
    match (opcao):
        case 1:
            cadastrar_usuario()

        case 2:
            codigo = logar_usuario()
            if codigo > 0:
                codigoUsuario = codigo
                tela_usuario_logado()
                escolha()

        case 3:
            cadastrar_paciente()
            escolha()

        case 99:
            exit()


def limpa_tela():
    os.system('cls')

def main():
    limpa_tela()
    nome_sistema()
    menu_inicial()
    escolha()
    main()

if __name__ == '__main__':
    main()





# Criar uma instância do DAO
#usuarioDAO = UsuarioDAO()
#pacienteDAO = PacienteDAO()

# Criar uma nova tarefa
#usuario = Usuario(None, "fernando@gmail.com", "42drer")
#codigo_usuario = usuarioDAO.inserir(usuario)
#if codigo_usuario == -1:
#    print("Já existe usuário cadastrado com o mesmo email")
#else:
#    paciente = Paciente(None, codigo_usuario, "Fernando Jose", 26, 12, 1965, 'M', 78, 166)
#    codigo_paciente = pacienteDAO.inserir(paciente)
#    if codigo_paciente == -1:
#        print("Já existe paciente associado ao mesmo usuario")

#print("fim")




#if codigo_usuario != -1:
#    print("Usuario criado com ID:", codigo_usuario)
    # Ler um usuario
#    usuario = usuarioDAO.buscar(codigo_usuario)
#    print("Usuário lido:", usuario.email, "-", usuario.senha)

    # Atualizar um usuario
#    usuario.senha = "4567"
#    usuarioDAO.atualizar(usuario)
#    print("Usuário atualizado")
#    usuarios = usuarioDAO._ler_usuarios()
#    print(usuarios)

    # Deletar uma usuario
 #   usuarioDAO.apagar(codigo_usuario)
 #   print("Usuário deletado")
#else:
#    print("Usuário já existe")
# Fechar a conexão com o banco de dados
#usuarioDAO.fechar()