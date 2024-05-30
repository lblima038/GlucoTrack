import os
from app.cadastrar_usuario import cadastrar_usuario
from util.util import nome_sistema
from util.util import limpa_tela
from app.logar_usuario import logar

def inicio():
    limpa_tela()
    nome_sistema()
    print("1. Entrar")
    print("2. Cadastrar usuário")
    print("0. Sair")
    print("============================================")
    print()
    
    opcao=int(input("Digite sua opção: "))
    
    match(opcao):
        case 1:
            sucesso = logar()
            if sucesso == -1:
                inicio()
            else:
                pass #desenvolver função de usuário logado
        case 2:
            cadastrar_usuario()
            inicio()
        case 0:
            exit()
    
if __name__ == "__main__":
    inicio()
    
