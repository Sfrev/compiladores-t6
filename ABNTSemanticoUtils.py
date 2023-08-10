from TabelaDeSimbolos import TabelaDeSimbolos
from ABNTParser import ABNTParser

class ABNTSemanticoUtils:

    errosSemanticos = []

    @staticmethod
    def adicionarErroSemantico(token, mensagem):

        linha = token.line
        coluna = token.column
        ABNTSemanticoUtils.errosSemanticos.append(f"Linha {linha}, coluna {coluna}: {mensagem}")

    @staticmethod
    def getTipo(valor: str) -> TabelaDeSimbolos.TipoABNT:
        tipo = None
        if valor == 'periodico':
            tipo = TabelaDeSimbolos.TipoABNT.PERIODICO
        elif valor == 'jornal':
            tipo = TabelaDeSimbolos.TipoABNT.JORNAL
        elif valor == 'publisher':
            tipo = TabelaDeSimbolos.TipoABNT.PUBLICADORA
        return tipo