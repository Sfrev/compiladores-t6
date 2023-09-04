from ABNTParser import ABNTParser
from ABNTVisitor import ABNTVisitor
from TabelaDeSimbolos import TabelaDeSimbolos

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
            artigo = self.tabela.obterEntradaTabelaSimbolos(ctx.ID().getText()).valor

            self.markdown.append(f"## {ctx.names().getText()}")
            self.markdown.append(f"## {ctx.title().getText()}")
            self.markdown.append(f"## {artigo[0]}")
            self.markdown.append(f"## {ctx.volume().getText()}")
            self.markdown.append(f"## {ctx.pages().getText()}")
            self.markdown.append(f"## {ctx.month().getText()}")
            self.markdown.append(f"## {ctx.year().getText()}")

        return super().visitArticleCitation(ctx)
    
    def visitBookCitation(self, ctx):
        if ctx.ID() is not None:
            livro = self.tabela.obterEntradaTabelaSimbolos(ctx.ID().getText()).valor

            nomes = ordenar_nomes(ctx.names().getText())
            ##separacao = ctx.names().getText().split()
            ##sobrenome_autor = separacao[-1].upper()
            ##separacao.pop()
            ##nome_autor = ' '.join(separacao)

            self.markdown.append(f"## {nomes}")

            print('alooooooooooooo')

            self.markdown.append(f"### {ctx.bookTitle().getText()}")

            if ctx.CADEIA() is not None:
                self.markdown.append(f"### {ctx.CADEIA().getText()}")

            self.markdown.append(f"### {ctx.edition().getText()}")
            self.markdown.append(f"## {livro[0]}")
            self.markdown.append(f"## {livro[1]}")
            self.markdown.append(f"## {ctx.publishMonth().getText()}")
            self.markdown.append(f"## {ctx.publishYear().getText()}")
            self.markdown.append(f"")
        return super().visitBookCitation(ctx)
    
    def visitPeriodico(self, ctx: ABNTParser.PeriodicoContext):
        periodico = []
        periodico.append(ctx.CADEIA().getText())
        periodico.append(ctx.INT().getText())
        periodico.append(ctx.localTitle().getText())
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PERIODICO, periodico)

    def visitJornal(self, ctx: ABNTParser.JornalContext):
        jornal = []
        jornal.append(ctx.CADEIA()[0].getText())
        jornal.append(ctx.CADEIA()[1].getText())
        jornal.append(ctx.localTitle().getText())
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.JORNAL, jornal)

    def visitPublisher(self, ctx: ABNTParser.PublisherContext):
        publicadora = []
        publicadora.append(ctx.CADEIA()[0].getText())
        publicadora.append(ctx.CADEIA()[1].getText())
        publicadora.append(ctx.localTitle().getText())
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PUBLICADORA, publicadora)
    
def ordenar_nomes(entrada):
    # Divida a entrada em uma lista de nomes
    nomes = entrada.split(', ')

    # Ordene a lista de nomes pelo primeiro nome
    nomes_ordenados = sorted(nomes, key=lambda nome: nome.split()[0])

    # Crie a saída formatada
    saida = ''
    for nome in nomes_ordenados:
        partes_nome = nome.split()
        sobrenome = partes_nome[-1]
        primeiro_nome = ' '.join(partes_nome[:-1])
        saida += f'{sobrenome.upper()}, {primeiro_nome}. '

    # Remova o espaço em branco extra no final
    saida = saida.rstrip()

    return saida