from apartamento import *

class Lista:

    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, apartamento):
        if self.inicio == None:
            self.inicio = apartamento
            apartamento.vaga = 1
        elif self.tamanho == 1:
            if self.inicio.vaga > 1:
                auxiliar = self.inicio
                apartamento.vaga = 1
                apartamento.proximo = auxiliar
                self.inicio = apartamento
            else:
                apartamento.vaga = 2
                self.inicio.proximo = apartamento
        else:
            anterior = self.inicio
            auxiliar = anterior.proximo
            if anterior.vaga > 1:
                aux = self.inicio
                apartamento.vaga = 1
                apartamento.proximo = aux
                self.inicio = apartamento
            while auxiliar:
                if anterior.vaga - auxiliar.vaga != -1:
                    anterior.proximo = apartamento
                    apartamento.vaga = anterior.vaga + 1
                    apartamento.proximo = auxiliar
                    break
                else:
                    anterior = auxiliar
                    auxiliar = anterior.proximo
            if not auxiliar:
                anterior.proximo = apartamento
                apartamento.vaga = anterior.vaga + 1
        self.tamanho += 1

    def imprimir(self):
        if self.inicio == None:
            print("A lista está vazia.")
        else:
            auxiliar = self.inicio
            while auxiliar:
                print(auxiliar)
                auxiliar = auxiliar.proximo
            print(f"O tamanho da lista é: {self.tamanho}")

    def excluir(self, vaga):
        if self.inicio == None:
            print("A lista está vazia.")
        elif self.tamanho == 1:
            if self.inicio.vaga == vaga:
                self.inicio.vaga = None
                self.inicio.proximo = None
                self.inicio = None
                self.tamanho -= 1
            else:
                print("O ID informado não foi localizado.")
        else:
            if self.inicio.vaga == vaga:
                self.inicio.vaga = None
                self.inicio.proximo = None
                auxiliar = self.inicio.proximo
                self.inicio = auxiliar
                self.tamanho -= 1
            else:
                anterior = self.inicio
                auxiliar = anterior.proximo
                while auxiliar:
                    if auxiliar.vaga == vaga:
                        auxiliar.vaga = None
                        anterior.proximo = auxiliar.proximo
                        auxiliar.proximo = None
                        self.tamanho -= 1
                        break
                    else:
                        anterior = auxiliar
                        auxiliar = anterior.proximo

