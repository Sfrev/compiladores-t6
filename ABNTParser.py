# Generated from ABNT.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,165,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,5,0,37,8,0,10,0,12,0,40,9,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,5,3,108,8,3,10,3,12,3,111,9,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,0,0,150,0,38,1,0,0,0,2,41,1,0,0,0,4,72,1,0,0,0,6,103,1,
        0,0,0,8,114,1,0,0,0,10,118,1,0,0,0,12,122,1,0,0,0,14,126,1,0,0,0,
        16,130,1,0,0,0,18,134,1,0,0,0,20,138,1,0,0,0,22,142,1,0,0,0,24,146,
        1,0,0,0,26,150,1,0,0,0,28,154,1,0,0,0,30,158,1,0,0,0,32,162,1,0,
        0,0,34,37,3,2,1,0,35,37,3,4,2,0,36,34,1,0,0,0,36,35,1,0,0,0,37,40,
        1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,1,1,0,0,0,40,38,1,0,0,0,41,
        42,5,1,0,0,42,43,5,2,0,0,43,44,5,3,0,0,44,45,5,4,0,0,45,46,3,6,3,
        0,46,47,5,5,0,0,47,48,5,6,0,0,48,49,5,4,0,0,49,50,3,8,4,0,50,51,
        5,5,0,0,51,52,5,7,0,0,52,53,5,4,0,0,53,54,3,10,5,0,54,55,5,5,0,0,
        55,56,5,8,0,0,56,57,5,4,0,0,57,58,3,14,7,0,58,59,5,5,0,0,59,60,5,
        9,0,0,60,61,5,4,0,0,61,62,3,16,8,0,62,63,5,5,0,0,63,64,5,10,0,0,
        64,65,5,4,0,0,65,66,3,18,9,0,66,67,5,5,0,0,67,68,5,11,0,0,68,69,
        5,4,0,0,69,70,3,20,10,0,70,71,5,12,0,0,71,3,1,0,0,0,72,73,5,13,0,
        0,73,74,5,2,0,0,74,75,5,3,0,0,75,76,5,4,0,0,76,77,3,6,3,0,77,78,
        5,5,0,0,78,79,5,6,0,0,79,80,5,4,0,0,80,81,3,12,6,0,81,82,5,5,0,0,
        82,83,5,14,0,0,83,84,5,4,0,0,84,85,3,22,11,0,85,86,5,5,0,0,86,87,
        5,15,0,0,87,88,5,4,0,0,88,89,3,24,12,0,89,90,5,5,0,0,90,91,5,16,
        0,0,91,92,5,4,0,0,92,93,3,26,13,0,93,94,5,5,0,0,94,95,5,17,0,0,95,
        96,5,4,0,0,96,97,3,28,14,0,97,98,5,5,0,0,98,99,5,18,0,0,99,100,5,
        4,0,0,100,101,3,30,15,0,101,102,5,12,0,0,102,5,1,0,0,0,103,104,5,
        19,0,0,104,109,3,32,16,0,105,106,5,5,0,0,106,108,3,32,16,0,107,105,
        1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,
        1,0,0,0,111,109,1,0,0,0,112,113,5,20,0,0,113,7,1,0,0,0,114,115,5,
        19,0,0,115,116,3,32,16,0,116,117,5,20,0,0,117,9,1,0,0,0,118,119,
        5,19,0,0,119,120,3,32,16,0,120,121,5,20,0,0,121,11,1,0,0,0,122,123,
        5,19,0,0,123,124,3,32,16,0,124,125,5,20,0,0,125,13,1,0,0,0,126,127,
        5,19,0,0,127,128,5,22,0,0,128,129,5,20,0,0,129,15,1,0,0,0,130,131,
        5,19,0,0,131,132,5,22,0,0,132,133,5,20,0,0,133,17,1,0,0,0,134,135,
        5,19,0,0,135,136,5,22,0,0,136,137,5,20,0,0,137,19,1,0,0,0,138,139,
        5,19,0,0,139,140,5,22,0,0,140,141,5,20,0,0,141,21,1,0,0,0,142,143,
        5,19,0,0,143,144,5,22,0,0,144,145,5,20,0,0,145,23,1,0,0,0,146,147,
        5,19,0,0,147,148,3,32,16,0,148,149,5,20,0,0,149,25,1,0,0,0,150,151,
        5,19,0,0,151,152,3,32,16,0,152,153,5,20,0,0,153,27,1,0,0,0,154,155,
        5,19,0,0,155,156,5,22,0,0,156,157,5,20,0,0,157,29,1,0,0,0,158,159,
        5,19,0,0,159,160,5,22,0,0,160,161,5,20,0,0,161,31,1,0,0,0,162,163,
        5,21,0,0,163,33,1,0,0,0,3,36,38,109
    ]

class ABNTParser ( Parser ):

    grammarFileName = "ABNT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!artigo'", "'{'", "'nome'", "'='", "','", 
                     "'titulo'", "'revista'", "'volume'", "'pagina'", "'mes'", 
                     "'ano'", "'}'", "'!livro'", "'edicao'", "'local_publicacao'", 
                     "'editora'", "'mes_publicacao'", "'ano_publicacao'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CADEIA", "INT", "WS" ]

    RULE_citation = 0
    RULE_articleCitation = 1
    RULE_bookCitation = 2
    RULE_names = 3
    RULE_title = 4
    RULE_journalTitle = 5
    RULE_bookTitle = 6
    RULE_volume = 7
    RULE_pages = 8
    RULE_month = 9
    RULE_year = 10
    RULE_edition = 11
    RULE_location = 12
    RULE_publisher = 13
    RULE_publishMonth = 14
    RULE_publishYear = 15
    RULE_name = 16

    ruleNames =  [ "citation", "articleCitation", "bookCitation", "names", 
                   "title", "journalTitle", "bookTitle", "volume", "pages", 
                   "month", "year", "edition", "location", "publisher", 
                   "publishMonth", "publishYear", "name" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    CADEIA=21
    INT=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CitationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def articleCitation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ABNTParser.ArticleCitationContext)
            else:
                return self.getTypedRuleContext(ABNTParser.ArticleCitationContext,i)


        def bookCitation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ABNTParser.BookCitationContext)
            else:
                return self.getTypedRuleContext(ABNTParser.BookCitationContext,i)


        def getRuleIndex(self):
            return ABNTParser.RULE_citation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCitation" ):
                listener.enterCitation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCitation" ):
                listener.exitCitation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCitation" ):
                return visitor.visitCitation(self)
            else:
                return visitor.visitChildren(self)




    def citation(self):

        localctx = ABNTParser.CitationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_citation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==13:
                self.state = 36
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 34
                    self.articleCitation()
                    pass
                elif token in [13]:
                    self.state = 35
                    self.bookCitation()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArticleCitationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def names(self):
            return self.getTypedRuleContext(ABNTParser.NamesContext,0)


        def title(self):
            return self.getTypedRuleContext(ABNTParser.TitleContext,0)


        def journalTitle(self):
            return self.getTypedRuleContext(ABNTParser.JournalTitleContext,0)


        def volume(self):
            return self.getTypedRuleContext(ABNTParser.VolumeContext,0)


        def pages(self):
            return self.getTypedRuleContext(ABNTParser.PagesContext,0)


        def month(self):
            return self.getTypedRuleContext(ABNTParser.MonthContext,0)


        def year(self):
            return self.getTypedRuleContext(ABNTParser.YearContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_articleCitation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArticleCitation" ):
                listener.enterArticleCitation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArticleCitation" ):
                listener.exitArticleCitation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArticleCitation" ):
                return visitor.visitArticleCitation(self)
            else:
                return visitor.visitChildren(self)




    def articleCitation(self):

        localctx = ABNTParser.ArticleCitationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_articleCitation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ABNTParser.T__0)
            self.state = 42
            self.match(ABNTParser.T__1)
            self.state = 43
            self.match(ABNTParser.T__2)
            self.state = 44
            self.match(ABNTParser.T__3)
            self.state = 45
            self.names()
            self.state = 46
            self.match(ABNTParser.T__4)
            self.state = 47
            self.match(ABNTParser.T__5)
            self.state = 48
            self.match(ABNTParser.T__3)
            self.state = 49
            self.title()
            self.state = 50
            self.match(ABNTParser.T__4)
            self.state = 51
            self.match(ABNTParser.T__6)
            self.state = 52
            self.match(ABNTParser.T__3)
            self.state = 53
            self.journalTitle()
            self.state = 54
            self.match(ABNTParser.T__4)
            self.state = 55
            self.match(ABNTParser.T__7)
            self.state = 56
            self.match(ABNTParser.T__3)
            self.state = 57
            self.volume()
            self.state = 58
            self.match(ABNTParser.T__4)
            self.state = 59
            self.match(ABNTParser.T__8)
            self.state = 60
            self.match(ABNTParser.T__3)
            self.state = 61
            self.pages()
            self.state = 62
            self.match(ABNTParser.T__4)
            self.state = 63
            self.match(ABNTParser.T__9)
            self.state = 64
            self.match(ABNTParser.T__3)
            self.state = 65
            self.month()
            self.state = 66
            self.match(ABNTParser.T__4)
            self.state = 67
            self.match(ABNTParser.T__10)
            self.state = 68
            self.match(ABNTParser.T__3)
            self.state = 69
            self.year()
            self.state = 70
            self.match(ABNTParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BookCitationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def names(self):
            return self.getTypedRuleContext(ABNTParser.NamesContext,0)


        def bookTitle(self):
            return self.getTypedRuleContext(ABNTParser.BookTitleContext,0)


        def edition(self):
            return self.getTypedRuleContext(ABNTParser.EditionContext,0)


        def location(self):
            return self.getTypedRuleContext(ABNTParser.LocationContext,0)


        def publisher(self):
            return self.getTypedRuleContext(ABNTParser.PublisherContext,0)


        def publishMonth(self):
            return self.getTypedRuleContext(ABNTParser.PublishMonthContext,0)


        def publishYear(self):
            return self.getTypedRuleContext(ABNTParser.PublishYearContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_bookCitation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBookCitation" ):
                listener.enterBookCitation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBookCitation" ):
                listener.exitBookCitation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBookCitation" ):
                return visitor.visitBookCitation(self)
            else:
                return visitor.visitChildren(self)




    def bookCitation(self):

        localctx = ABNTParser.BookCitationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bookCitation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ABNTParser.T__12)
            self.state = 73
            self.match(ABNTParser.T__1)
            self.state = 74
            self.match(ABNTParser.T__2)
            self.state = 75
            self.match(ABNTParser.T__3)
            self.state = 76
            self.names()
            self.state = 77
            self.match(ABNTParser.T__4)
            self.state = 78
            self.match(ABNTParser.T__5)
            self.state = 79
            self.match(ABNTParser.T__3)
            self.state = 80
            self.bookTitle()
            self.state = 81
            self.match(ABNTParser.T__4)
            self.state = 82
            self.match(ABNTParser.T__13)
            self.state = 83
            self.match(ABNTParser.T__3)
            self.state = 84
            self.edition()
            self.state = 85
            self.match(ABNTParser.T__4)
            self.state = 86
            self.match(ABNTParser.T__14)
            self.state = 87
            self.match(ABNTParser.T__3)
            self.state = 88
            self.location()
            self.state = 89
            self.match(ABNTParser.T__4)
            self.state = 90
            self.match(ABNTParser.T__15)
            self.state = 91
            self.match(ABNTParser.T__3)
            self.state = 92
            self.publisher()
            self.state = 93
            self.match(ABNTParser.T__4)
            self.state = 94
            self.match(ABNTParser.T__16)
            self.state = 95
            self.match(ABNTParser.T__3)
            self.state = 96
            self.publishMonth()
            self.state = 97
            self.match(ABNTParser.T__4)
            self.state = 98
            self.match(ABNTParser.T__17)
            self.state = 99
            self.match(ABNTParser.T__3)
            self.state = 100
            self.publishYear()
            self.state = 101
            self.match(ABNTParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ABNTParser.NameContext)
            else:
                return self.getTypedRuleContext(ABNTParser.NameContext,i)


        def getRuleIndex(self):
            return ABNTParser.RULE_names

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNames" ):
                listener.enterNames(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNames" ):
                listener.exitNames(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNames" ):
                return visitor.visitNames(self)
            else:
                return visitor.visitChildren(self)




    def names(self):

        localctx = ABNTParser.NamesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_names)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ABNTParser.T__18)
            self.state = 104
            self.name()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 105
                self.match(ABNTParser.T__4)
                self.state = 106
                self.name()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ABNTParser.NameContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle" ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle" ):
                listener.exitTitle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTitle" ):
                return visitor.visitTitle(self)
            else:
                return visitor.visitChildren(self)




    def title(self):

        localctx = ABNTParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ABNTParser.T__18)
            self.state = 115
            self.name()
            self.state = 116
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JournalTitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ABNTParser.NameContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_journalTitle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJournalTitle" ):
                listener.enterJournalTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJournalTitle" ):
                listener.exitJournalTitle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJournalTitle" ):
                return visitor.visitJournalTitle(self)
            else:
                return visitor.visitChildren(self)




    def journalTitle(self):

        localctx = ABNTParser.JournalTitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_journalTitle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ABNTParser.T__18)
            self.state = 119
            self.name()
            self.state = 120
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BookTitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ABNTParser.NameContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_bookTitle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBookTitle" ):
                listener.enterBookTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBookTitle" ):
                listener.exitBookTitle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBookTitle" ):
                return visitor.visitBookTitle(self)
            else:
                return visitor.visitChildren(self)




    def bookTitle(self):

        localctx = ABNTParser.BookTitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bookTitle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ABNTParser.T__18)
            self.state = 123
            self.name()
            self.state = 124
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VolumeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ABNTParser.INT, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_volume

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVolume" ):
                listener.enterVolume(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVolume" ):
                listener.exitVolume(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVolume" ):
                return visitor.visitVolume(self)
            else:
                return visitor.visitChildren(self)




    def volume(self):

        localctx = ABNTParser.VolumeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_volume)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(ABNTParser.T__18)
            self.state = 127
            self.match(ABNTParser.INT)
            self.state = 128
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PagesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ABNTParser.INT, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_pages

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPages" ):
                listener.enterPages(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPages" ):
                listener.exitPages(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPages" ):
                return visitor.visitPages(self)
            else:
                return visitor.visitChildren(self)




    def pages(self):

        localctx = ABNTParser.PagesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pages)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ABNTParser.T__18)
            self.state = 131
            self.match(ABNTParser.INT)
            self.state = 132
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ABNTParser.INT, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_month

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMonth" ):
                listener.enterMonth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMonth" ):
                listener.exitMonth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonth" ):
                return visitor.visitMonth(self)
            else:
                return visitor.visitChildren(self)




    def month(self):

        localctx = ABNTParser.MonthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_month)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ABNTParser.T__18)
            self.state = 135
            self.match(ABNTParser.INT)
            self.state = 136
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ABNTParser.INT, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_year

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYear" ):
                listener.enterYear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYear" ):
                listener.exitYear(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYear" ):
                return visitor.visitYear(self)
            else:
                return visitor.visitChildren(self)




    def year(self):

        localctx = ABNTParser.YearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_year)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ABNTParser.T__18)
            self.state = 139
            self.match(ABNTParser.INT)
            self.state = 140
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ABNTParser.INT, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_edition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdition" ):
                listener.enterEdition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdition" ):
                listener.exitEdition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdition" ):
                return visitor.visitEdition(self)
            else:
                return visitor.visitChildren(self)




    def edition(self):

        localctx = ABNTParser.EditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_edition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(ABNTParser.T__18)
            self.state = 143
            self.match(ABNTParser.INT)
            self.state = 144
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ABNTParser.NameContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocation" ):
                listener.enterLocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocation" ):
                listener.exitLocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocation" ):
                return visitor.visitLocation(self)
            else:
                return visitor.visitChildren(self)




    def location(self):

        localctx = ABNTParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ABNTParser.T__18)
            self.state = 147
            self.name()
            self.state = 148
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PublisherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ABNTParser.NameContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_publisher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPublisher" ):
                listener.enterPublisher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPublisher" ):
                listener.exitPublisher(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPublisher" ):
                return visitor.visitPublisher(self)
            else:
                return visitor.visitChildren(self)




    def publisher(self):

        localctx = ABNTParser.PublisherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_publisher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ABNTParser.T__18)
            self.state = 151
            self.name()
            self.state = 152
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PublishMonthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ABNTParser.INT, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_publishMonth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPublishMonth" ):
                listener.enterPublishMonth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPublishMonth" ):
                listener.exitPublishMonth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPublishMonth" ):
                return visitor.visitPublishMonth(self)
            else:
                return visitor.visitChildren(self)




    def publishMonth(self):

        localctx = ABNTParser.PublishMonthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_publishMonth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ABNTParser.T__18)
            self.state = 155
            self.match(ABNTParser.INT)
            self.state = 156
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PublishYearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ABNTParser.INT, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_publishYear

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPublishYear" ):
                listener.enterPublishYear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPublishYear" ):
                listener.exitPublishYear(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPublishYear" ):
                return visitor.visitPublishYear(self)
            else:
                return visitor.visitChildren(self)




    def publishYear(self):

        localctx = ABNTParser.PublishYearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_publishYear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ABNTParser.T__18)
            self.state = 159
            self.match(ABNTParser.INT)
            self.state = 160
            self.match(ABNTParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self):
            return self.getToken(ABNTParser.CADEIA, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = ABNTParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ABNTParser.CADEIA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





