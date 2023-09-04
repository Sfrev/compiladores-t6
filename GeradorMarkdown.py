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
            self.markdown.append(f"# Artigo")
            self.markdown.append(f"```")
            publicacao = self.tabela.obterEntradaTabelaSimbolos(ctx.ID().getText()).valor

            names = ctx.names().getText()
            names = removerAspasDuplas(names)
            nomes = ordenarNomes(names)

            tituloArtigo = ctx.title().getText()
            tituloArtigo = removerAspasDuplas(tituloArtigo)


            self.markdown.append(f"{nomes} {tituloArtigo}. {publicacao[0]}, {publicacao[1]}, v.{ctx.volume().getText()}, p.{ctx.pages().getText()}, {abreviar_mes(ctx.month().getText())} {ctx.year().getText()}. ")

            self.markdown.append(f"```")

        return super().visitArticleCitation(ctx)
    
    def visitBookCitation(self, ctx):
        if ctx.ID() is not None:
            self.markdown.append(f"# Livro")
            self.markdown.append(f"```")
            publicadora = self.tabela.obterEntradaTabelaSimbolos(ctx.ID().getText()).valor

            names = ctx.names().getText()
            names = removerAspasDuplas(names)
            nomes = ordenarNomes(names)

            tituloLivro = ctx.bookTitle().getText()
            tituloLivro = removerAspasDuplas(tituloLivro)

            subTitulo = ''

            if ctx.CADEIA() is not None:
                subTitulo = ctx.CADEIA().getText()
                subTitulo = removerAspasDuplas(subTitulo)

            self.markdown.append(f"{nomes} {tituloLivro}. {subTitulo if ctx.CADEIA() is not None else ''} {ctx.edition().getText()}. ed. {publicadora[2]}, {publicadora[0]}, {abreviar_mes(ctx.publishMonth().getText())} {ctx.publishYear().getText()}.")
            self.markdown.append(f"```")
        return super().visitBookCitation(ctx)
    
    def visitPeriodico(self, ctx: ABNTParser.PeriodicoContext):
        periodico = []
        nome = ctx.CADEIA().getText()
        nome = removerAspasDuplas(nome)
        localTitle = ctx.localTitle().getText()
        localTitle = removerAspasDuplas(localTitle)

        periodico.append(nome)
        periodico.append(ctx.INT().getText())
        periodico.append(localTitle)
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PERIODICO, periodico)

    def visitJornal(self, ctx: ABNTParser.JornalContext):
        jornal = []
        nome = ctx.CADEIA()[0].getText()
        nome = removerAspasDuplas(nome)
        localPublicacao = ctx.localTitle().getText()
        localPublicacao = removerAspasDuplas(localPublicacao)
        dataPublicacao = ctx.CADEIA()[1].getText()

        jornal.append(nome)
        jornal.append(localPublicacao)
        jornal.append(dataPublicacao)
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.JORNAL, jornal)

    def visitPublisher(self, ctx: ABNTParser.PublisherContext):
        publicadora = []
        nome = ctx.CADEIA()[0].getText()
        nome = removerAspasDuplas(nome)
        idioma = ctx.CADEIA()[1].getText()
        idioma = removerAspasDuplas(idioma)
        localTitle = ctx.localTitle().getText()
        localTitle = removerAspasDuplas(localTitle)

        publicadora.append(nome)
        publicadora.append(idioma)
        publicadora.append(localTitle)
        self.tabela.adicionarTabelaSimbolos(ctx.ID().getText(), TabelaDeSimbolos.TipoABNT.PUBLICADORA, publicadora)
    
def ordenarNomes(entrada):
    nomes = entrada.split(',')
    nomes_formatados = []

    for nome in nomes:
        partes = nome.split()
        sobrenome = partes[1].upper()
        nome_formatado = f'{sobrenome}, {partes[0]}'
        nomes_formatados.append(nome_formatado)

    return '; '.join(nomes_formatados) + '.'

def removerAspasDuplas(entrada):
    return entrada.replace('"', '')

def abreviar_mes(mes):
    meses = {
        '1': 'jan.',
        '2': 'fev.',
        '3': 'mar.',
        '4': 'abr.',
        '5': 'mai.',
        '6': 'jun.',
        '7': 'jul.',
        '8': 'ago.',
        '9': 'set.',
        '10': 'out.',
        '11': 'nov.',
        '12': 'dez.'
    }
    return meses[mes]