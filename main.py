import os

def funcao ():
    os.system('cls') 
    print("========= GlucoTrack (versão: 1.0) =========")
    print()
    print("1. Entrar")
    print("2. Cadastrar usuário")
    print("0. Sair")
    print("============================================")
    print()
    opcao=input("Digite sua opção: ")
    
    match(opcao):
        case 1:
            pass
        case 2:
            pass
        case 0:
            exit()
    
    
    
if __name__ == "__main__":
    funcao()
    
