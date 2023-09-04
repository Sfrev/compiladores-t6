from ABNTParser import ABNTParser
from ABNTVisitor import ABNTVisitor
from ABNTSemanticoUtils import ABNTSemanticoUtils
from TabelaDeSimbolos import TabelaDeSimbolos

class ABNTSemantico(ABNTVisitor):
    def __init__(self):
        self.tabelaDeSimbolos = TabelaDeSimbolos()
    
    def visitPrograma(self, ctx: ABNTParser.ProgramaContext):

        declarouVariaveis = False
        declarouCitacoes = False

        for variable in ctx.variables():
            declarouVariaveis = True
            self.visitVariables(variable)

        for citation in ctx.citation():
            declarouCitacoes = True
            self.visitCitation(citation)

        if not declarouVariaveis:
            ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, "Nenhuma variável declarada")
        
        if not declarouCitacoes:   
            ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, "Nenhuma citação declarada")
    
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
    
    def visitCitation(self, ctx):
        
        articleCitation = ctx.articleCitation()
        bookCitation = ctx.bookCitation()

        if articleCitation is not None:
            self.visitArticleCitation(articleCitation)
        elif bookCitation is not None:
            self.visitBookCitation(bookCitation)
    
    def visitArticleCitation(self, ctx):

        if ctx.ID() is not None:
            if not self.tabelaDeSimbolos.existe(ctx.ID().getText()):
                ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Artigo {ctx.ID().getText()} não declarado")
        return super().visitArticleCitation(ctx)
    
    def visitBookCitation(self, ctx):
        if ctx.ID() is not None:
            if not self.tabelaDeSimbolos.existe(ctx.ID().getText()):
                ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Livro {ctx.ID().getText()} não declarado")
        return super().visitBookCitation(ctx)
    
    def visitPeriodico(self, ctx):
        
        if self.tabelaDeSimbolos.existe(ctx.ID().getText()):
            # Erro: variável já declarada
            ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Periódico {ctx.ID().getText()} já declarado")
        
        # Insere variável na tabela de símbolos
        self.tabelaDeSimbolos.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PERIODICO)

        return super().visitPeriodico(ctx)
    
    def visitJornal(self, ctx):
        
        if self.tabelaDeSimbolos.existe(ctx.ID().getText()):
            # Erro: variável já declarada
            ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Jornal {ctx.ID().getText()} já declarado")
        
        # Insere variável na tabela de símbolos
        self.tabelaDeSimbolos.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.JORNAL)
        
        return super().visitJornal(ctx)
    
    def visitPublisher(self, ctx):
        
        if self.tabelaDeSimbolos.existe(ctx.ID().getText()):
            # Erro: variável já declarada
            ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Publicadora {ctx.ID().getText()} já declarada")
        
        # Insere variável na tabela de símbolos
        self.tabelaDeSimbolos.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PUBLICADORA)
        
        return super().visitPublisher(ctx)