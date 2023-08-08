# Generated from ABNT.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ABNTParser import ABNTParser
else:
    from ABNTParser import ABNTParser

# This class defines a complete generic visitor for a parse tree produced by ABNTParser.

class ABNTVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ABNTParser#programa.
    def visitPrograma(self, ctx:ABNTParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#variables.
    def visitVariables(self, ctx:ABNTParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#citation.
    def visitCitation(self, ctx:ABNTParser.CitationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#articleCitation.
    def visitArticleCitation(self, ctx:ABNTParser.ArticleCitationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#bookCitation.
    def visitBookCitation(self, ctx:ABNTParser.BookCitationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#periodico.
    def visitPeriodico(self, ctx:ABNTParser.PeriodicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#jornal.
    def visitJornal(self, ctx:ABNTParser.JornalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#publisher.
    def visitPublisher(self, ctx:ABNTParser.PublisherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#names.
    def visitNames(self, ctx:ABNTParser.NamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#title.
    def visitTitle(self, ctx:ABNTParser.TitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#localTitle.
    def visitLocalTitle(self, ctx:ABNTParser.LocalTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#bookTitle.
    def visitBookTitle(self, ctx:ABNTParser.BookTitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#volume.
    def visitVolume(self, ctx:ABNTParser.VolumeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#pages.
    def visitPages(self, ctx:ABNTParser.PagesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#month.
    def visitMonth(self, ctx:ABNTParser.MonthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#year.
    def visitYear(self, ctx:ABNTParser.YearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#edition.
    def visitEdition(self, ctx:ABNTParser.EditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#publishMonth.
    def visitPublishMonth(self, ctx:ABNTParser.PublishMonthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#publishYear.
    def visitPublishYear(self, ctx:ABNTParser.PublishYearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABNTParser#name.
    def visitName(self, ctx:ABNTParser.NameContext):
        return self.visitChildren(ctx)



del ABNTParser