from enum import Enum

class TabelaDeSimbolos:
    class TipoABNT(Enum):
        INTEIRO = 1
        CADEIA = 2
        ID = 3
        PERIODICO = 4
        JORNAL = 5
        PUBLICADORA = 6


    class EntradaTabelaDeSimbolos:
        def __init__(self, nome, tipo):
            self.nome = nome
            self.tipo = tipo

    def __init__(self, tipo):
        self.tabelaDeSimbolos = {}
        self.tabelaTipo = {}
        self.tipo = tipo

    def adicionarTabelaSimbolos(self, nome: str, tipo: TipoABNT):
        etds = TabelaDeSimbolos.EntradaTabelaDeSimbolos(nome, tipo)
        self.tabelaDeSimbolos[nome] = etds

    def adicionarEntradaTabelaSimbolos(self, entradaTabelaSimbolos: EntradaTabelaDeSimbolos):
        self.tabelaDeSimbolos[entradaTabelaSimbolos.nome] = entradaTabelaSimbolos

    def adicionarTipoNome(self, tipoNome: str, entradaTabelaSimbolos: EntradaTabelaDeSimbolos):

        if tipoNome in self.tabelaTipo:
            self.tabelaTipo.get(tipoNome).append(entradaTabelaSimbolos)
        else:
            list = []
            list.append(entradaTabelaSimbolos)
            self.tabelaTipo[tipoNome] = list

    def existe(self, nome: str):
        return nome in self.tabelaDeSimbolos

    def verificar(self, nome: str):
        if self.existe(nome):
            return self.tabelaDeSimbolos[nome].tipo
        
        return None
    
    def verificarTipo(self, nome: str):
        return self.tabelaTipo[nome]
