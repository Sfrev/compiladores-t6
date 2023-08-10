from enum import Enum

class TabelaDeSimbolos:
    class TipoABNT(Enum):
        INTEIRO = 1
        CADEIA = 2
        ID = 3
        PERIODICO = 4
        JORNAL = 5
        PUBLICADORA = 6
        INVALIDO = 7

    class EntradaTabelaDeSimbolos:
        def __init__(self, nome, tipo):
            self.nome = nome
            self.tipo = tipo

    def __init__(self):
        self.tabelaDeSimbolos = {}

    def adicionarTabelaSimbolos(self, nome: str, tipo: TipoABNT):
        etds = TabelaDeSimbolos.EntradaTabelaDeSimbolos(nome, tipo)
        self.tabelaDeSimbolos[nome] = etds

    def adicionarEntradaTabelaSimbolos(self, entradaTabelaSimbolos: EntradaTabelaDeSimbolos):
        self.tabelaDeSimbolos[entradaTabelaSimbolos.nome] = entradaTabelaSimbolos

    def obterEntradaTabelaSimbolos(self, nome: str):
        return self.tabelaDeSimbolos[nome]

    def existe(self, nome: str):
        return nome in self.tabelaDeSimbolos

    def getTipo(self, nome: str):
        if self.existe(nome):
            return self.tabelaDeSimbolos[nome].tipo
        
        return None
