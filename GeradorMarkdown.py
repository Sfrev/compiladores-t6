from ABNTParser import ABNTParser
from ABNTVisitor import ABNTVisitor
from TabelaDeSimbolos import TabelaDeSimbolos
from ABNTSemanticoUtils import ABNTSemanticoUtils

class GeradorMarkdown(ABNTVisitor):
    def __init__(self) -> None:
        self.tabela = TabelaDeSimbolos()
        self.markdown = []