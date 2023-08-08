from ABNTParser import ABNTParser
from ABNTVisitor import ABNTVisitor
from TabelaDeSimbolos import TabelaDeSimbolos
from Escopo import Escopo
from typing import List


class ABNTSemantico(ABNTVisitor):
    def __init__(self):
        self.escopos = Escopo()
    
    def visitPrograma(self, ctx):

        for variable in ctx.variables():
            self.visit(variable)

        for citation in ctx.citation():
            self.visit(citation)

        # Implementar ações semânticas para o programa
        return super().visitPrograma(ctx)
    
    def visitVariables(self, ctx):
        # Implementar ações semânticas para as variáveis (periodico, jornal, publisher)
        return super().visitVariables(ctx)
        
    
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
        # Implementar ações semânticas para a definição de periódico
        return super().visitPeriodico(ctx)
    
    def visitJornal(self, ctx):
        # Implementar ações semânticas para a definição de jornal
        return super().visitJornal(ctx)
    
    def visitPublisher(self, ctx):
        # Implementar ações semânticas para a definição de editora
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
