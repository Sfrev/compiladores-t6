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
        4,1,30,233,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        4,0,42,8,0,11,0,12,0,43,1,0,1,0,1,0,1,1,1,1,1,1,3,1,52,8,1,1,2,1,
        2,5,2,56,8,2,10,2,12,2,59,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,109,8,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,5,8,184,8,8,10,8,12,8,187,9,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,0,0,219,0,41,1,0,0,0,2,51,1,0,0,0,4,57,1,0,0,0,6,60,1,0,0,0,8,
        93,1,0,0,0,10,130,1,0,0,0,12,145,1,0,0,0,14,164,1,0,0,0,16,179,1,
        0,0,0,18,190,1,0,0,0,20,194,1,0,0,0,22,198,1,0,0,0,24,202,1,0,0,
        0,26,206,1,0,0,0,28,210,1,0,0,0,30,214,1,0,0,0,32,218,1,0,0,0,34,
        222,1,0,0,0,36,226,1,0,0,0,38,230,1,0,0,0,40,42,3,2,1,0,41,40,1,
        0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,
        46,3,4,2,0,46,47,5,0,0,1,47,1,1,0,0,0,48,52,3,10,5,0,49,52,3,12,
        6,0,50,52,3,14,7,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,
        3,1,0,0,0,53,56,3,6,3,0,54,56,3,8,4,0,55,53,1,0,0,0,55,54,1,0,0,
        0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,5,1,0,0,0,59,57,1,
        0,0,0,60,61,5,1,0,0,61,62,5,2,0,0,62,63,5,3,0,0,63,64,5,4,0,0,64,
        65,3,16,8,0,65,66,5,5,0,0,66,67,5,6,0,0,67,68,5,4,0,0,68,69,3,18,
        9,0,69,70,5,5,0,0,70,71,5,7,0,0,71,72,5,4,0,0,72,73,5,8,0,0,73,74,
        5,28,0,0,74,75,5,9,0,0,75,76,5,5,0,0,76,77,5,10,0,0,77,78,5,4,0,
        0,78,79,3,24,12,0,79,80,5,5,0,0,80,81,5,11,0,0,81,82,5,4,0,0,82,
        83,3,26,13,0,83,84,5,5,0,0,84,85,5,12,0,0,85,86,5,4,0,0,86,87,3,
        28,14,0,87,88,5,5,0,0,88,89,5,13,0,0,89,90,5,4,0,0,90,91,3,30,15,
        0,91,92,5,14,0,0,92,7,1,0,0,0,93,94,5,15,0,0,94,95,5,2,0,0,95,96,
        5,3,0,0,96,97,5,4,0,0,97,98,3,16,8,0,98,99,5,5,0,0,99,100,5,6,0,
        0,100,101,5,4,0,0,101,108,3,22,11,0,102,103,5,5,0,0,103,104,5,16,
        0,0,104,105,5,4,0,0,105,106,5,8,0,0,106,107,5,27,0,0,107,109,5,9,
        0,0,108,102,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,111,5,5,
        0,0,111,112,5,17,0,0,112,113,5,4,0,0,113,114,3,32,16,0,114,115,5,
        5,0,0,115,116,5,18,0,0,116,117,5,4,0,0,117,118,5,8,0,0,118,119,5,
        28,0,0,119,120,5,9,0,0,120,121,5,5,0,0,121,122,5,19,0,0,122,123,
        5,4,0,0,123,124,3,34,17,0,124,125,5,5,0,0,125,126,5,20,0,0,126,127,
        5,4,0,0,127,128,3,36,18,0,128,129,5,14,0,0,129,9,1,0,0,0,130,131,
        5,21,0,0,131,132,5,2,0,0,132,133,5,22,0,0,133,134,5,4,0,0,134,135,
        5,28,0,0,135,136,5,5,0,0,136,137,5,3,0,0,137,138,5,4,0,0,138,139,
        5,27,0,0,139,140,5,5,0,0,140,141,5,23,0,0,141,142,5,4,0,0,142,143,
        5,29,0,0,143,144,5,14,0,0,144,11,1,0,0,0,145,146,5,7,0,0,146,147,
        5,2,0,0,147,148,5,22,0,0,148,149,5,4,0,0,149,150,5,28,0,0,150,151,
        5,5,0,0,151,152,5,3,0,0,152,153,5,4,0,0,153,154,5,27,0,0,154,155,
        5,5,0,0,155,156,5,24,0,0,156,157,5,4,0,0,157,158,5,27,0,0,158,159,
        5,5,0,0,159,160,5,25,0,0,160,161,5,4,0,0,161,162,5,27,0,0,162,163,
        5,14,0,0,163,13,1,0,0,0,164,165,5,18,0,0,165,166,5,2,0,0,166,167,
        5,22,0,0,167,168,5,4,0,0,168,169,5,28,0,0,169,170,5,5,0,0,170,171,
        5,3,0,0,171,172,5,4,0,0,172,173,5,27,0,0,173,174,5,5,0,0,174,175,
        5,26,0,0,175,176,5,4,0,0,176,177,5,27,0,0,177,178,5,14,0,0,178,15,
        1,0,0,0,179,180,5,8,0,0,180,185,3,38,19,0,181,182,5,5,0,0,182,184,
        3,38,19,0,183,181,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,
        1,0,0,0,186,188,1,0,0,0,187,185,1,0,0,0,188,189,5,9,0,0,189,17,1,
        0,0,0,190,191,5,8,0,0,191,192,3,38,19,0,192,193,5,9,0,0,193,19,1,
        0,0,0,194,195,5,8,0,0,195,196,3,38,19,0,196,197,5,9,0,0,197,21,1,
        0,0,0,198,199,5,8,0,0,199,200,3,38,19,0,200,201,5,9,0,0,201,23,1,
        0,0,0,202,203,5,8,0,0,203,204,5,29,0,0,204,205,5,9,0,0,205,25,1,
        0,0,0,206,207,5,8,0,0,207,208,5,29,0,0,208,209,5,9,0,0,209,27,1,
        0,0,0,210,211,5,8,0,0,211,212,5,29,0,0,212,213,5,9,0,0,213,29,1,
        0,0,0,214,215,5,8,0,0,215,216,5,29,0,0,216,217,5,9,0,0,217,31,1,
        0,0,0,218,219,5,8,0,0,219,220,5,29,0,0,220,221,5,9,0,0,221,33,1,
        0,0,0,222,223,5,8,0,0,223,224,5,29,0,0,224,225,5,9,0,0,225,35,1,
        0,0,0,226,227,5,8,0,0,227,228,5,29,0,0,228,229,5,9,0,0,229,37,1,
        0,0,0,230,231,5,27,0,0,231,39,1,0,0,0,6,43,51,55,57,108,185
    ]

class ABNTParser ( Parser ):

    grammarFileName = "ABNT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'artigo'", "'{'", "'nome'", "'='", "','", 
                     "'titulo'", "'jornal'", "'['", "']'", "'volume'", "'pagina'", 
                     "'mes'", "'ano'", "'}'", "'livro'", "'subtitulo'", 
                     "'edicao'", "'editora'", "'mes_publicacao'", "'ano_publicacao'", 
                     "'periodico'", "'id'", "'ISBN'", "'local_publicacao'", 
                     "'data_publicacao'", "'idioma'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CADEIA", "ID", 
                      "INT", "WS" ]

    RULE_programa = 0
    RULE_variables = 1
    RULE_citation = 2
    RULE_articleCitation = 3
    RULE_bookCitation = 4
    RULE_periodico = 5
    RULE_jornal = 6
    RULE_publisher = 7
    RULE_names = 8
    RULE_title = 9
    RULE_localTitle = 10
    RULE_bookTitle = 11
    RULE_volume = 12
    RULE_pages = 13
    RULE_month = 14
    RULE_year = 15
    RULE_edition = 16
    RULE_publishMonth = 17
    RULE_publishYear = 18
    RULE_name = 19

    ruleNames =  [ "programa", "variables", "citation", "articleCitation", 
                   "bookCitation", "periodico", "jornal", "publisher", "names", 
                   "title", "localTitle", "bookTitle", "volume", "pages", 
                   "month", "year", "edition", "publishMonth", "publishYear", 
                   "name" ]

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
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    CADEIA=27
    ID=28
    INT=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def citation(self):
            return self.getTypedRuleContext(ABNTParser.CitationContext,0)


        def EOF(self):
            return self.getToken(ABNTParser.EOF, 0)

        def variables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ABNTParser.VariablesContext)
            else:
                return self.getTypedRuleContext(ABNTParser.VariablesContext,i)


        def getRuleIndex(self):
            return ABNTParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = ABNTParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.variables()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2359424) != 0)):
                    break

            self.state = 45
            self.citation()
            self.state = 46
            self.match(ABNTParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def periodico(self):
            return self.getTypedRuleContext(ABNTParser.PeriodicoContext,0)


        def jornal(self):
            return self.getTypedRuleContext(ABNTParser.JornalContext,0)


        def publisher(self):
            return self.getTypedRuleContext(ABNTParser.PublisherContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ABNTParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variables)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.periodico()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.jornal()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.publisher()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 4, self.RULE_citation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==15:
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 53
                    self.articleCitation()
                    pass
                elif token in [15]:
                    self.state = 54
                    self.bookCitation()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 59
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


        def ID(self):
            return self.getToken(ABNTParser.ID, 0)

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
        self.enterRule(localctx, 6, self.RULE_articleCitation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ABNTParser.T__0)
            self.state = 61
            self.match(ABNTParser.T__1)
            self.state = 62
            self.match(ABNTParser.T__2)
            self.state = 63
            self.match(ABNTParser.T__3)
            self.state = 64
            self.names()
            self.state = 65
            self.match(ABNTParser.T__4)
            self.state = 66
            self.match(ABNTParser.T__5)
            self.state = 67
            self.match(ABNTParser.T__3)
            self.state = 68
            self.title()
            self.state = 69
            self.match(ABNTParser.T__4)
            self.state = 70
            self.match(ABNTParser.T__6)
            self.state = 71
            self.match(ABNTParser.T__3)
            self.state = 72
            self.match(ABNTParser.T__7)
            self.state = 73
            self.match(ABNTParser.ID)
            self.state = 74
            self.match(ABNTParser.T__8)
            self.state = 75
            self.match(ABNTParser.T__4)
            self.state = 76
            self.match(ABNTParser.T__9)
            self.state = 77
            self.match(ABNTParser.T__3)
            self.state = 78
            self.volume()
            self.state = 79
            self.match(ABNTParser.T__4)
            self.state = 80
            self.match(ABNTParser.T__10)
            self.state = 81
            self.match(ABNTParser.T__3)
            self.state = 82
            self.pages()
            self.state = 83
            self.match(ABNTParser.T__4)
            self.state = 84
            self.match(ABNTParser.T__11)
            self.state = 85
            self.match(ABNTParser.T__3)
            self.state = 86
            self.month()
            self.state = 87
            self.match(ABNTParser.T__4)
            self.state = 88
            self.match(ABNTParser.T__12)
            self.state = 89
            self.match(ABNTParser.T__3)
            self.state = 90
            self.year()
            self.state = 91
            self.match(ABNTParser.T__13)
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


        def ID(self):
            return self.getToken(ABNTParser.ID, 0)

        def publishMonth(self):
            return self.getTypedRuleContext(ABNTParser.PublishMonthContext,0)


        def publishYear(self):
            return self.getTypedRuleContext(ABNTParser.PublishYearContext,0)


        def CADEIA(self):
            return self.getToken(ABNTParser.CADEIA, 0)

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
        self.enterRule(localctx, 8, self.RULE_bookCitation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ABNTParser.T__14)
            self.state = 94
            self.match(ABNTParser.T__1)
            self.state = 95
            self.match(ABNTParser.T__2)
            self.state = 96
            self.match(ABNTParser.T__3)
            self.state = 97
            self.names()
            self.state = 98
            self.match(ABNTParser.T__4)
            self.state = 99
            self.match(ABNTParser.T__5)
            self.state = 100
            self.match(ABNTParser.T__3)
            self.state = 101
            self.bookTitle()
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 102
                self.match(ABNTParser.T__4)
                self.state = 103
                self.match(ABNTParser.T__15)
                self.state = 104
                self.match(ABNTParser.T__3)
                self.state = 105
                self.match(ABNTParser.T__7)
                self.state = 106
                self.match(ABNTParser.CADEIA)
                self.state = 107
                self.match(ABNTParser.T__8)


            self.state = 110
            self.match(ABNTParser.T__4)
            self.state = 111
            self.match(ABNTParser.T__16)
            self.state = 112
            self.match(ABNTParser.T__3)
            self.state = 113
            self.edition()
            self.state = 114
            self.match(ABNTParser.T__4)
            self.state = 115
            self.match(ABNTParser.T__17)
            self.state = 116
            self.match(ABNTParser.T__3)
            self.state = 117
            self.match(ABNTParser.T__7)
            self.state = 118
            self.match(ABNTParser.ID)
            self.state = 119
            self.match(ABNTParser.T__8)
            self.state = 120
            self.match(ABNTParser.T__4)
            self.state = 121
            self.match(ABNTParser.T__18)
            self.state = 122
            self.match(ABNTParser.T__3)
            self.state = 123
            self.publishMonth()
            self.state = 124
            self.match(ABNTParser.T__4)
            self.state = 125
            self.match(ABNTParser.T__19)
            self.state = 126
            self.match(ABNTParser.T__3)
            self.state = 127
            self.publishYear()
            self.state = 128
            self.match(ABNTParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PeriodicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ABNTParser.ID, 0)

        def CADEIA(self):
            return self.getToken(ABNTParser.CADEIA, 0)

        def INT(self):
            return self.getToken(ABNTParser.INT, 0)

        def getRuleIndex(self):
            return ABNTParser.RULE_periodico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeriodico" ):
                listener.enterPeriodico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeriodico" ):
                listener.exitPeriodico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPeriodico" ):
                return visitor.visitPeriodico(self)
            else:
                return visitor.visitChildren(self)




    def periodico(self):

        localctx = ABNTParser.PeriodicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_periodico)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ABNTParser.T__20)
            self.state = 131
            self.match(ABNTParser.T__1)
            self.state = 132
            self.match(ABNTParser.T__21)
            self.state = 133
            self.match(ABNTParser.T__3)
            self.state = 134
            self.match(ABNTParser.ID)
            self.state = 135
            self.match(ABNTParser.T__4)
            self.state = 136
            self.match(ABNTParser.T__2)
            self.state = 137
            self.match(ABNTParser.T__3)
            self.state = 138
            self.match(ABNTParser.CADEIA)
            self.state = 139
            self.match(ABNTParser.T__4)
            self.state = 140
            self.match(ABNTParser.T__22)
            self.state = 141
            self.match(ABNTParser.T__3)
            self.state = 142
            self.match(ABNTParser.INT)
            self.state = 143
            self.match(ABNTParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JornalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ABNTParser.ID, 0)

        def CADEIA(self, i:int=None):
            if i is None:
                return self.getTokens(ABNTParser.CADEIA)
            else:
                return self.getToken(ABNTParser.CADEIA, i)

        def getRuleIndex(self):
            return ABNTParser.RULE_jornal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJornal" ):
                listener.enterJornal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJornal" ):
                listener.exitJornal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJornal" ):
                return visitor.visitJornal(self)
            else:
                return visitor.visitChildren(self)




    def jornal(self):

        localctx = ABNTParser.JornalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_jornal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(ABNTParser.T__6)
            self.state = 146
            self.match(ABNTParser.T__1)
            self.state = 147
            self.match(ABNTParser.T__21)
            self.state = 148
            self.match(ABNTParser.T__3)
            self.state = 149
            self.match(ABNTParser.ID)
            self.state = 150
            self.match(ABNTParser.T__4)
            self.state = 151
            self.match(ABNTParser.T__2)
            self.state = 152
            self.match(ABNTParser.T__3)
            self.state = 153
            self.match(ABNTParser.CADEIA)
            self.state = 154
            self.match(ABNTParser.T__4)
            self.state = 155
            self.match(ABNTParser.T__23)
            self.state = 156
            self.match(ABNTParser.T__3)
            self.state = 157
            self.match(ABNTParser.CADEIA)
            self.state = 158
            self.match(ABNTParser.T__4)
            self.state = 159
            self.match(ABNTParser.T__24)
            self.state = 160
            self.match(ABNTParser.T__3)
            self.state = 161
            self.match(ABNTParser.CADEIA)
            self.state = 162
            self.match(ABNTParser.T__13)
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

        def ID(self):
            return self.getToken(ABNTParser.ID, 0)

        def CADEIA(self, i:int=None):
            if i is None:
                return self.getTokens(ABNTParser.CADEIA)
            else:
                return self.getToken(ABNTParser.CADEIA, i)

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
        self.enterRule(localctx, 14, self.RULE_publisher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ABNTParser.T__17)
            self.state = 165
            self.match(ABNTParser.T__1)
            self.state = 166
            self.match(ABNTParser.T__21)
            self.state = 167
            self.match(ABNTParser.T__3)
            self.state = 168
            self.match(ABNTParser.ID)
            self.state = 169
            self.match(ABNTParser.T__4)
            self.state = 170
            self.match(ABNTParser.T__2)
            self.state = 171
            self.match(ABNTParser.T__3)
            self.state = 172
            self.match(ABNTParser.CADEIA)
            self.state = 173
            self.match(ABNTParser.T__4)
            self.state = 174
            self.match(ABNTParser.T__25)
            self.state = 175
            self.match(ABNTParser.T__3)
            self.state = 176
            self.match(ABNTParser.CADEIA)
            self.state = 177
            self.match(ABNTParser.T__13)
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
        self.enterRule(localctx, 16, self.RULE_names)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ABNTParser.T__7)
            self.state = 180
            self.name()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 181
                self.match(ABNTParser.T__4)
                self.state = 182
                self.name()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 18, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(ABNTParser.T__7)
            self.state = 191
            self.name()
            self.state = 192
            self.match(ABNTParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalTitleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(ABNTParser.NameContext,0)


        def getRuleIndex(self):
            return ABNTParser.RULE_localTitle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalTitle" ):
                listener.enterLocalTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalTitle" ):
                listener.exitLocalTitle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalTitle" ):
                return visitor.visitLocalTitle(self)
            else:
                return visitor.visitChildren(self)




    def localTitle(self):

        localctx = ABNTParser.LocalTitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_localTitle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ABNTParser.T__7)
            self.state = 195
            self.name()
            self.state = 196
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 22, self.RULE_bookTitle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(ABNTParser.T__7)
            self.state = 199
            self.name()
            self.state = 200
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 24, self.RULE_volume)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(ABNTParser.T__7)
            self.state = 203
            self.match(ABNTParser.INT)
            self.state = 204
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 26, self.RULE_pages)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(ABNTParser.T__7)
            self.state = 207
            self.match(ABNTParser.INT)
            self.state = 208
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 28, self.RULE_month)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ABNTParser.T__7)
            self.state = 211
            self.match(ABNTParser.INT)
            self.state = 212
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 30, self.RULE_year)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ABNTParser.T__7)
            self.state = 215
            self.match(ABNTParser.INT)
            self.state = 216
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 32, self.RULE_edition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ABNTParser.T__7)
            self.state = 219
            self.match(ABNTParser.INT)
            self.state = 220
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 34, self.RULE_publishMonth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(ABNTParser.T__7)
            self.state = 223
            self.match(ABNTParser.INT)
            self.state = 224
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 36, self.RULE_publishYear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(ABNTParser.T__7)
            self.state = 227
            self.match(ABNTParser.INT)
            self.state = 228
            self.match(ABNTParser.T__8)
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
        self.enterRule(localctx, 38, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ABNTParser.CADEIA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





