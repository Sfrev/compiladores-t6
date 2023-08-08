from TabelaDeSimbolos import TabelaDeSimbolos
from ABNTParser import ABNTParser
from Escopo import Escopo


class ABNTSemanticoUtils:

    errosSemanticos = []

    @staticmethod
    def adicionarErroSemantico(token, mensagem):

        linha = token.line
        coluna = token.column
        ABNTSemanticoUtils.errosSemanticos.append(f"Linha {linha}, coluna {coluna}: {mensagem}")