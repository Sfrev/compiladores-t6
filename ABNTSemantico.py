from ABNTParser import ABNTParser
from ABNTVisitor import ABNTVisitor
from ABNTSemanticoUtils import ABNTSemanticoUtils
from TabelaDeSimbolos import TabelaDeSimbolos
from typing import List


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
        # Implementar ações semânticas para as citações (articleCitation, bookCitation)
        return super().visitCitation(ctx)
    
    def visitArticleCitation(self, ctx):
        # Implementar ações semânticas para a citação de artigo
        return super().visitArticleCitation(ctx)
    
    def visitBookCitation(self, ctx):
        # Implementar ações semânticas para a citação de livro
        return super().visitBookCitation(ctx)
    
    def visitPeriodico(self, ctx):
        
        if self.tabelaDeSimbolos.existe(ctx.ID().getText()):
            # Erro: variável já declarada
            ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Variável {ctx.ID().getText()} do tipo periódico já declarada")
        
        # Insere variável na tabela de símbolos
        self.tabelaDeSimbolos.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PERIODICO)

        return super().visitPeriodico(ctx)
    
    def visitJornal(self, ctx):
        
        if self.tabelaDeSimbolos.existe(ctx.ID().getText()):
            # Erro: variável já declarada
            ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Variável {ctx.ID().getText()} do tipo jornal já declarada")
        
        # Insere variável na tabela de símbolos
        self.tabelaDeSimbolos.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.JORNAL)
        
        return super().visitJornal(ctx)
    
    def visitPublisher(self, ctx):
        
        if self.tabelaDeSimbolos.existe(ctx.ID().getText()):
            # Erro: variável já declarada
            ABNTSemanticoUtils.adicionarErroSemantico(ctx.start, f"Variável {ctx.ID().getText()} do tipo publicadora já declarada")
        
        # Insere variável na tabela de símbolos
        self.tabelaDeSimbolos.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PUBLICADORA)
        
        return super().visitPublisher(ctx)
    
    def visitNames(self, ctx):
        # Implementar ações semânticas para os nomes
        return super().visitNames(ctx)
    
    def visitTitle(self, ctx):
        # Implementar ações semânticas para os títulos
        return super().visitTitle(ctx)
    
    #Este é apenas um 
    # esqueleto básico para um analisador semântico. 
    # Você precisará preencher cada método de visitação com ações semânticas específicas para cada regra da gramática, 
    # como a verificação de tipos, controle de escopo, detecção de erros semânticos, entre outros.

    #Certifique-se de adaptar o código às suas necessidades específicas e continuar a desenvolver 
    # cada método de visitação de acordo com as verificações semânticas que você deseja realizar
    #Em cada método de visitação, você deve implementar as verificações semânticas relevantes para 
    # aquela regra específica. Por exemplo, no método visitPeriodico, você pode verificar se o ID do periódico é único, 
    # se o ISBN é válido, etc. Da mesma forma, nos métodos visitArticleCitation e visitBookCitation, você pode verificar 
    # se os campos estão sendo preenchidos corretamente e se as referências existem no contexto.
