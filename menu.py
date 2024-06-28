from lista_vagas import *
from fila_espera import *

def menu():

    print("=" * 30)
    print("   MENU GERENCIADOR DO CONDOMÍNIO")
    print("=" * 30)
    print("Selecione uma opção:")
    print("1. Cadastrar Torres")
    print("2. Cadastrar apartamentos")
    print("3. Liberar vaga de garagem")
    print("4. Visualizar fila de espera")
    print("5. Visualizar lista da garagem")
    print("6. Sair")
    print("=" * 30)

    opcao_desejada = None
    
    while True:

        try:
            escolha_usuario = int(input("Qual a opção desejada?"))
            if escolha_usuario < 1 or escolha_usuario > 6:
                print("Escolha um número válido do menu.")
            else:
                opcao_desejada = escolha_usuario
                break
        except ValueError:
            print("Digite um número válido.")

    if opcao_desejada == 1:
        pass
    elif opcao_desejada == 2:
        pass
    elif opcao_desejada == 3:
        pass
    elif opcao_desejada == 4:
        pass
    elif opcao_desejada == 5:
        pass
    elif opcao_desejada == 6:
        print("Programa encerrado.")
        return


