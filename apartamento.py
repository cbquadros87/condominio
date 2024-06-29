from torre import *

numeros_apartamentos = [101, 102, 103, 104, 201, 202, 203, 204, 301, 302, 303, 304, 401, 402, 403, 404]

class Apartamento:

    idContador = 1

    def __init__(self):
        self.__id = Apartamento.idContador
        self.__numero = None
        self.__torre = None
        self.__vaga = None
        self.proximo = None        
        Apartamento.idContador += 1

    @property
    def id(self):
        return self.__id

    @property
    def numero(self):
        return self.__numero

    @property
    def torre(self):
        return self.__torre

    @property
    def vaga(self):
        return self.__vaga
    
    @vaga.setter
    def vaga(self, vaga):
        self.__vaga = vaga
    
    def _set_numero(self):
        while True:
            try:
                num = int(input("Informe o número do apartamento: "))
                if num in numeros_apartamentos:
                    self.__numero = num
                    break
                else:
                    print("Número de apartamento inválido. Por favor, escolha um número de apartamento existente.")
            except ValueError:
                print("Por favor, digite um número válido.")

    def _set_torre(self):
        print("Lista de torres cadastradas.")
        for torre in torres:
            print(torre)
        while True:
            try:
                idTorre = int(input("Digite o ID da torre que deverá receber o apartamento."))
                if idTorre > 0 and idTorre <= len(torres):
                    self.__torre = torres[idTorre - 1]
                    break
                else:
                    print("Digite um ID válido de torre.")
            except ValueError:
                print("Informe um número válido.")

    def cadastrar(self):
        self._set_numero()
        self._set_torre()

    def __str__(self):
        return f"Apartamento {self.__numero}, Vaga: {self.__vaga}, Torre: {self.__torre}. ID: {self.__id}"

    def imprimir(self):
        print(self)

