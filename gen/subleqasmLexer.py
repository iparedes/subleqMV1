# Generated from /Users/nacho/Documents/python-projects/movemak/subleqasm.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\6\2\37\n\2\r\2\16\2 \3\3\3\3\3\4\3\4\7\4\'\n")
        buf.write("\4\f\4\16\4*\13\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\5\r?\n\r\3")
        buf.write("\16\6\16B\n\16\r\16\16\16C\3\16\3\16\2\2\17\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\3\2\7\3\2\62;\4\2C\\c|\5\2\62;C\\c|\4\2\f\f\17\17\5\2")
        buf.write("\f\f\17\17\"\"\2J\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3\36\3\2\2\2\5\"\3\2\2\2\7$\3\2\2")
        buf.write("\2\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21")
        buf.write("\63\3\2\2\2\23\65\3\2\2\2\25\67\3\2\2\2\279\3\2\2\2\31")
        buf.write(">\3\2\2\2\33A\3\2\2\2\35\37\5\5\3\2\36\35\3\2\2\2\37 ")
        buf.write("\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\4\3\2\2\2\"#\t\2\2\2#")
        buf.write("\6\3\2\2\2$(\t\3\2\2%\'\t\4\2\2&%\3\2\2\2\'*\3\2\2\2(")
        buf.write("&\3\2\2\2()\3\2\2\2)\b\3\2\2\2*(\3\2\2\2+,\7,\2\2,\n\3")
        buf.write("\2\2\2-.\7\61\2\2.\f\3\2\2\2/\60\7-\2\2\60\16\3\2\2\2")
        buf.write("\61\62\7/\2\2\62\20\3\2\2\2\63\64\7.\2\2\64\22\3\2\2\2")
        buf.write("\65\66\7<\2\2\66\24\3\2\2\2\678\7*\2\28\26\3\2\2\29:\7")
        buf.write("+\2\2:\30\3\2\2\2;<\7\17\2\2<?\7\f\2\2=?\t\5\2\2>;\3\2")
        buf.write("\2\2>=\3\2\2\2?\32\3\2\2\2@B\t\6\2\2A@\3\2\2\2BC\3\2\2")
        buf.write("\2CA\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\b\16\2\2F\34\3\2\2")
        buf.write("\2\7\2 (>C\3\b\2\2")
        return buf.getvalue()


class subleqasmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    DIGIT = 2
    VARIABLE = 3
    MULT = 4
    DIV = 5
    PLUS = 6
    MINUS = 7
    COMMA = 8
    COLON = 9
    OPAR = 10
    CPAR = 11
    NEWLINE = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "','", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "DIGIT", "VARIABLE", "MULT", "DIV", "PLUS", "MINUS", 
            "COMMA", "COLON", "OPAR", "CPAR", "NEWLINE", "WS" ]

    ruleNames = [ "NUMBER", "DIGIT", "VARIABLE", "MULT", "DIV", "PLUS", 
                  "MINUS", "COMMA", "COLON", "OPAR", "CPAR", "NEWLINE", 
                  "WS" ]

    grammarFileName = "subleqasm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


