from lista_vagas import *
from fila_espera import *

listaVagasGaragem = Lista()
filaEspera = Fila()

def cadastrar_torres():
    novaTorre = Torre()
    novaTorre.cadastrar()
    print("A torre foi cadastrada com sucesso.")
    novaTorre.imprimir()

def cadastrar_apartamentos():
    if len(torres) == 0:
        print("ERRO!")
        print("Impossível cadastrar apartamentos enquanto não houverem torres cadastradas.")
        return
    else:
        novoAp = Apartamento()
        novoAp.cadastrar()
        if listaVagasGaragem.tamanho < 10:
            listaVagasGaragem.adicionar(novoAp)
        else:
            filaEspera.adicionar(novoAp)
        print("O apartamento foi cadastrado com sucesso.")
        novoAp.imprimir()
        return

def liberar_vaga():
    while True:
        try:
            vagaExcluida = int(input("Informe o número da vaga que será liberada: "))
            if vagaExcluida > 0 and vagaExcluida < 11:
                break
            else:
                print("Digite um número entre 1 e 10.")
        except:
            print("Digite um número válido.")
    apExcluido = listaVagasGaragem.excluir(vagaExcluida)
    if filaEspera.tamanho > 0:
        apParaReceberVaga = filaEspera.inicio
        filaEspera.remover()
        listaVagasGaragem.adicionar(apParaReceberVaga)
    filaEspera.adicionar(apExcluido)

def visualizar_fila_espera():
    filaEspera.imprimir()

def visualizar_lista_garagem():
    listaVagasGaragem.imprimir()

def menu():
    opcoes = {
        1: cadastrar_torres,
        2: cadastrar_apartamentos,
        3: liberar_vaga,
        4: visualizar_fila_espera,
        5: visualizar_lista_garagem,
        6: lambda: print("Programa encerrado.")
    }

    while True:
        print("=" * 30)
        print("MENU GERENCIADOR DO CONDOMÍNIO")
        print("=" * 30)
        print("Selecione uma opção:")
        print("1. Cadastrar Torres")
        print("2. Cadastrar apartamentos")
        print("3. Liberar vaga de garagem")
        print("4. Visualizar fila de espera")
        print("5. Visualizar lista da garagem")
        print("6. Sair")
        print("=" * 30)

        try:
            escolha_usuario = int(input("Qual a opção desejada? "))
            if escolha_usuario < 1 or escolha_usuario > 6:
                print("Escolha um número válido do menu.")
            else:
                opcoes[escolha_usuario]()
                if escolha_usuario == 6:
                    break
        except ValueError:
            print("Digite um número válido.")




