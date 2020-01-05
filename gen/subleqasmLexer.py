# Generated from /Users/nacho/Documents/python-projects/movemak/subleqasm.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("U\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\6\2#\n\2\r\2\16\2$\3\3\3")
        buf.write("\3\6\3)\n\3\r\3\16\3*\3\3\3\3\3\4\3\4\7\4\61\n\4\f\4\16")
        buf.write("\4\64\13\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\5\17M\n\17\3\20\6\20P\n\20\r\20\16\20Q\3\20\3\20\2\2")
        buf.write("\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21\3\2\b\t\2\"#%(*+..\61;C\\c|\4")
        buf.write("\2C\\c|\5\2\62;C\\c|\3\2\62;\4\2\f\f\17\17\5\2\f\f\17")
        buf.write("\17\"\"\2Y\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3\"\3\2\2\2\5")
        buf.write("&\3\2\2\2\7.\3\2\2\2\t\65\3\2\2\2\13\67\3\2\2\2\r9\3\2")
        buf.write("\2\2\17;\3\2\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3\2\2\2\27")
        buf.write("C\3\2\2\2\31E\3\2\2\2\33G\3\2\2\2\35L\3\2\2\2\37O\3\2")
        buf.write("\2\2!#\5\t\5\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2")
        buf.write("\2%\4\3\2\2\2&(\5\33\16\2\')\t\2\2\2(\'\3\2\2\2)*\3\2")
        buf.write("\2\2*(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\5\33\16\2-\6\3\2")
        buf.write("\2\2.\62\t\3\2\2/\61\t\4\2\2\60/\3\2\2\2\61\64\3\2\2\2")
        buf.write("\62\60\3\2\2\2\62\63\3\2\2\2\63\b\3\2\2\2\64\62\3\2\2")
        buf.write("\2\65\66\t\5\2\2\66\n\3\2\2\2\678\7,\2\28\f\3\2\2\29:")
        buf.write("\7\61\2\2:\16\3\2\2\2;<\7-\2\2<\20\3\2\2\2=>\7/\2\2>\22")
        buf.write("\3\2\2\2?@\7.\2\2@\24\3\2\2\2AB\7<\2\2B\26\3\2\2\2CD\7")
        buf.write("*\2\2D\30\3\2\2\2EF\7+\2\2F\32\3\2\2\2GH\7$\2\2H\34\3")
        buf.write("\2\2\2IJ\7\17\2\2JM\7\f\2\2KM\t\6\2\2LI\3\2\2\2LK\3\2")
        buf.write("\2\2M\36\3\2\2\2NP\t\7\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2")
        buf.write("\2QR\3\2\2\2RS\3\2\2\2ST\b\20\2\2T \3\2\2\2\b\2$*\62L")
        buf.write("Q\3\b\2\2")
        return buf.getvalue()


class subleqasmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    QUOTEDALPHANUM = 2
    VARIABLE = 3
    DIGIT = 4
    MULT = 5
    DIV = 6
    PLUS = 7
    MINUS = 8
    COMMA = 9
    COLON = 10
    OPAR = 11
    CPAR = 12
    QUOTE = 13
    NEWLINE = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "','", "':'", "'('", "')'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "QUOTEDALPHANUM", "VARIABLE", "DIGIT", "MULT", "DIV", 
            "PLUS", "MINUS", "COMMA", "COLON", "OPAR", "CPAR", "QUOTE", 
            "NEWLINE", "WS" ]

    ruleNames = [ "NUMBER", "QUOTEDALPHANUM", "VARIABLE", "DIGIT", "MULT", 
                  "DIV", "PLUS", "MINUS", "COMMA", "COLON", "OPAR", "CPAR", 
                  "QUOTE", "NEWLINE", "WS" ]

    grammarFileName = "subleqasm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


