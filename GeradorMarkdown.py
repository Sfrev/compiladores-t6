from ABNTParser import ABNTParser
from ABNTVisitor import ABNTVisitor
from TabelaDeSimbolos import TabelaDeSimbolos
from ABNTSemanticoUtils import ABNTSemanticoUtils

class GeradorMarkdown(ABNTVisitor):
    def __init__(self) -> None:
        self.tabela = TabelaDeSimbolos()
        self.markdown = []

    def visitPrograma(self, ctx: ABNTParser.ProgramaContext):
        for variable in ctx.variables():
            self.visitVariables(variable)
        
        for citation in ctx.citation():
            self.visitCitation(citation)

    def visitVariables(self, ctx: ABNTParser.VariablesContext):
        periodico = ctx.periodico()
        jornal = ctx.jornal()
        publisher = ctx.publisher()

        if periodico is not None:
            self.visitPeriodico(periodico)
        elif jornal is not None:
            self.visitJornal(jornal)
        elif publisher is not None:
            self.visitPublisher(publisher)

    def visitCitation(self, ctx: ABNTParser.CitationContext):
        articleCitation = ctx.articleCitation()
        bookCitation = ctx.bookCitation()

        if articleCitation is not None:
            self.visitArticleCitation(articleCitation)
        elif bookCitation is not None:
            self.visitBookCitation(bookCitation)

    def visitArticleCitation(self, ctx):
        if ctx.ID() is not None:
            if not self.tabela.existe(ctx.ID().getText()):
                ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Variável {ctx.ID().getText()} não declarada")
            else:
                variavel = self.tabela.obterEntradaTabelaSimbolos(ctx.ID().getText()).valor

                self.markdown.append(f"## {ctx.names().getText()}")
                self.markdown.append(f"## {ctx.title().getText()}")
                self.markdown.append(f"## {variavel[0]}")
                self.markdown.append(f"## {ctx.volume().getText()}")
                self.markdown.append(f"## {ctx.pages().getText()}")
                self.markdown.append(f"## {ctx.month().getText()}")
                self.markdown.append(f"## {ctx.year().getText()}")

        return super().visitArticleCitation(ctx)
    
    def visitBookCitation(self, ctx):
        if ctx.ID() is not None:
            if not self.tabela.existe(ctx.ID().getText()):
                ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Variável {ctx.ID().getText()} não declarada")
            else:
                variavel = self.tabela.obterEntradaTabelaSimbolos(ctx.ID().getText()).valor

                self.markdown.append(f"### {ctx.names().getText()}")
                self.markdown.append(f"### {ctx.bookTitle().getText()}")

                if ctx.CADEIA() is not None:
                    self.markdown.append(f"### {ctx.CADEIA().getText()}")

                self.markdown.append(f"### {ctx.edition().getText()}")
                self.markdown.append(f"## {variavel[0]}")
                self.markdown.append(f"## {variavel[1]}")
                self.markdown.append(f"## {ctx.publishMonth().getText()}")
                self.markdown.append(f"## {ctx.publishYear().getText()}")
        return super().visitBookCitation(ctx)
    
    def visitPeriodico(self, ctx: ABNTParser.PeriodicoContext):
        periodico = []
        periodico.append(ctx.CADEIA().getText())
        periodico.append(ctx.INT().getText())
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PERIODICO, periodico)

    def visitJornal(self, ctx: ABNTParser.JornalContext):
        jornal = []
        jornal.append(ctx.CADEIA()[0].getText())
        jornal.append(ctx.CADEIA()[1].getText())
        jornal.append(ctx.CADEIA()[2].getText())
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.JORNAL, jornal)

    def visitPublisher(self, ctx: ABNTParser.PublisherContext):
        publicadora = []
        publicadora.append(ctx.CADEIA()[0].getText())
        publicadora.append(ctx.CADEIA()[1].getText())
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PUBLICADORA, publicadora)
    