from crud.crud_usuario import login

def logar():
    email = input("Informe seu e-mail: ")
    senha = input("Informe sua senha: ")
    return login(email, senha)
