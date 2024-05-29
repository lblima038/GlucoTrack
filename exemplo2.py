from crud.crud_paciente import buscar_paciente_por_codigo_usuario
from crud.crud_usuario import buscar_usuarios, login
from crud.crud_usuario import inserir_usuario
from util.util import limpa_tela, tela_inicial, nome_sistema

def usuario_logado(codigo_usuario):

    limpa_tela()
    nome_sistema()
    paciente = buscar_paciente_por_codigo_usuario(codigo_usuario)
    codigo_paciente = paciente.codigo
    print("Paciente: ", paciente.nome)
    print("")
    input("pressione qualquer tecla")

def criar_usuario():
    pass

def logar():
    email = input("Informe seu e-mail: ")
    senha = input("Informe sua senha: ")
    return login(email, senha)

def escolha():
    global codigo_usuario

    opcao = int(input("Informe sua opção: "))
    match(opcao):
        case 0:
            exit()

        case 1:
            resultado = logar()
            if resultado != -1:
                usuario_logado(resultado)
                main()
            else:
                main()
        
        case 2:
            criar_usuario()

def main():
    limpa_tela()
    tela_inicial()
    escolha()

if __name__ == '__main__':
    main()
