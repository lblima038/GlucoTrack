from app.area_usuario_logado import tela_principal
from app.cadastro_usuario import cadastrar_usuario
from util.util import nome_sistema, limpa_tela
from app.cadastro_usuario import logar

def inicio():
    limpa_tela()    
    nome_sistema()

    print("1. Entrar")
    print("2. Cadastrar usuário")
    print("0. Sair")
    print()
    
    opcao = input("Digite sua opção: ")
    
    match opcao:
        case '1':
            sucesso = logar()
            if sucesso > 0:
                tela_principal(sucesso)

        case '2':
            cadastrar_usuario()

        case '0':
            print("Obrigado por usar o GlucoTrack.")
            exit()
        
    inicio()
    
if __name__ == "__main__":
    inicio()
    
