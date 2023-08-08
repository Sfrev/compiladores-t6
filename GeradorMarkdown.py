from ABNTParser import ABNTParser
from ABNTVisitor import ABNTVisitor
from TabelaDeSimbolos import TabelaDeSimbolos
from ABNTSemanticoUtils import ABNTSemanticoUtils
from Escopo import Escopo

class GeradorMarkdown(ABNTVisitor):
    def __init__(self) -> None:
        self.tabela = TabelaDeSimbolos(None)
        self.markdown = []