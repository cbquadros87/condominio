torres = []

class Torre:

    idContador = 1

    def __init__(self):
        self.__id = Torre.idContador
        self.__nome = None
        self.__endereco = None
        Torre.idContador += 1

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    def _set_nome(self):
        while True:
            nome = input("Qual o nome da Torre cadastrada?").strip()
            if nome:
                self.__nome = nome
                break
            else:
                print("Digite um nome válido.")

    def _set_endereco(self):
        while True:
            end = input("Qual o endereço da torre cadastrada?").strip()
            if end:
                self.__endereco = end
                break
            else:
                print("Digite um endereço válido.")

    def cadastrar(self):
        self._set_nome()
        self._set_endereco()
        torres.append(self)

    def __str__(self):
        return f"Torre {self.__nome}, localizada no endereço: {self.__endereco}. ID da torre: {self.__id}"

    def imprimir(self):
        print(self)

    
    

