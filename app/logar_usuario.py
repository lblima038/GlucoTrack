from util.util import limpa_tela, nome_sistema
from crud.crud_usuario import login

def logar():
    email = ""
    senha = ""

    limpa_tela()
    nome_sistema()
    while(email == ""):
        email = input("Informe seu e-mail: ")
        if email == "":
            print("e-mail inválido!")
    
    while(senha == ""):
        senha = input("Informe sua senha : ")
        if senha == "":
            print("Senha inválida!")

    resultado = login(email, senha)
    if resultado == -1:
        input("Usuário/senha inválido. Pressione qualquer tecla...")
    
    return resultado
