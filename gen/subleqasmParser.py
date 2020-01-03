# Generated from /Users/nacho/Documents/python-projects/movemak/subleqasm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\6\2\27\n\2\r\2\16\2\30\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\7\4%\n\4\f\4\16")
        buf.write("\4(\13\4\5\4*\n\4\3\4\3\4\5\4.\n\4\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\7\6:\n\6\f\6\16\6=\13\6\3\6\3\6\5")
        buf.write("\6A\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6I\n\6\f\6\16\6L\13")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7T\n\7\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\n\2\3\n\13\2\4\6\b\n\f\16\20\22\2\5\3\2\7")
        buf.write("\b\3\2\t\n\4\2\13\13\20\20\2a\2\26\3\2\2\2\4\32\3\2\2")
        buf.write("\2\6)\3\2\2\2\b/\3\2\2\2\n@\3\2\2\2\fS\3\2\2\2\16U\3\2")
        buf.write("\2\2\20X\3\2\2\2\22Z\3\2\2\2\24\27\5\4\3\2\25\27\5\6\4")
        buf.write("\2\26\24\3\2\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2")
        buf.write("\2\2\30\31\3\2\2\2\31\3\3\2\2\2\32\33\5\b\5\2\33\34\5")
        buf.write("\20\t\2\34\35\5\b\5\2\35\36\5\20\t\2\36 \5\b\5\2\37!\7")
        buf.write("\20\2\2 \37\3\2\2\2 !\3\2\2\2!\5\3\2\2\2\"&\5\16\b\2#")
        buf.write("%\7\20\2\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'")
        buf.write("*\3\2\2\2(&\3\2\2\2)\"\3\2\2\2)*\3\2\2\2*+\3\2\2\2+-\5")
        buf.write("\22\n\2,.\7\20\2\2-,\3\2\2\2-.\3\2\2\2.\7\3\2\2\2/\60")
        buf.write("\5\n\6\2\60\t\3\2\2\2\61\62\b\6\1\2\62\63\7\n\2\2\63A")
        buf.write("\5\n\6\b\64\65\7\t\2\2\65A\5\n\6\7\66A\5\f\7\2\67;\5\16")
        buf.write("\b\28:\7\20\2\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2")
        buf.write("\2<>\3\2\2\2=;\3\2\2\2>?\5\n\6\3?A\3\2\2\2@\61\3\2\2\2")
        buf.write("@\64\3\2\2\2@\66\3\2\2\2@\67\3\2\2\2AJ\3\2\2\2BC\f\6\2")
        buf.write("\2CD\t\2\2\2DI\5\n\6\7EF\f\5\2\2FG\t\3\2\2GI\5\n\6\6H")
        buf.write("B\3\2\2\2HE\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\13")
        buf.write("\3\2\2\2LJ\3\2\2\2MN\7\r\2\2NO\5\n\6\2OP\7\16\2\2PT\3")
        buf.write("\2\2\2QT\7\3\2\2RT\7\5\2\2SM\3\2\2\2SQ\3\2\2\2SR\3\2\2")
        buf.write("\2T\r\3\2\2\2UV\7\5\2\2VW\7\f\2\2W\17\3\2\2\2XY\t\4\2")
        buf.write("\2Y\21\3\2\2\2Z[\7\4\2\2[\23\3\2\2\2\r\26\30 &)-;@HJS")
        return buf.getvalue()


class subleqasmParser ( Parser ):

    grammarFileName = "subleqasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'", "','", "':'", 
                     "'('", "')'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "QUOTEDALPHANUM", "VARIABLE", 
                      "DIGIT", "MULT", "DIV", "PLUS", "MINUS", "COMMA", 
                      "COLON", "OPAR", "CPAR", "QUOTE", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_instr = 1
    RULE_data = 2
    RULE_val = 3
    RULE_expr = 4
    RULE_atom = 5
    RULE_label = 6
    RULE_sep = 7
    RULE_literal = 8

    ruleNames =  [ "program", "instr", "data", "val", "expr", "atom", "label", 
                   "sep", "literal" ]

    EOF = Token.EOF
    NUMBER=1
    QUOTEDALPHANUM=2
    VARIABLE=3
    DIGIT=4
    MULT=5
    DIV=6
    PLUS=7
    MINUS=8
    COMMA=9
    COLON=10
    OPAR=11
    CPAR=12
    QUOTE=13
    NEWLINE=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(subleqasmParser.InstrContext)
            else:
                return self.getTypedRuleContext(subleqasmParser.InstrContext,i)


        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(subleqasmParser.DataContext)
            else:
                return self.getTypedRuleContext(subleqasmParser.DataContext,i)


        def getRuleIndex(self):
            return subleqasmParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = subleqasmParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 18
                    self.instr()
                    pass

                elif la_ == 2:
                    self.state = 19
                    self.data()
                    pass


                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << subleqasmParser.NUMBER) | (1 << subleqasmParser.QUOTEDALPHANUM) | (1 << subleqasmParser.VARIABLE) | (1 << subleqasmParser.PLUS) | (1 << subleqasmParser.MINUS) | (1 << subleqasmParser.OPAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(subleqasmParser.ValContext)
            else:
                return self.getTypedRuleContext(subleqasmParser.ValContext,i)


        def sep(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(subleqasmParser.SepContext)
            else:
                return self.getTypedRuleContext(subleqasmParser.SepContext,i)


        def NEWLINE(self):
            return self.getToken(subleqasmParser.NEWLINE, 0)

        def getRuleIndex(self):
            return subleqasmParser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)




    def instr(self):

        localctx = subleqasmParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.val()
            self.state = 25
            self.sep()
            self.state = 26
            self.val()
            self.state = 27
            self.sep()
            self.state = 28
            self.val()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==subleqasmParser.NEWLINE:
                self.state = 29
                self.match(subleqasmParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(subleqasmParser.LiteralContext,0)


        def label(self):
            return self.getTypedRuleContext(subleqasmParser.LabelContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(subleqasmParser.NEWLINE)
            else:
                return self.getToken(subleqasmParser.NEWLINE, i)

        def getRuleIndex(self):
            return subleqasmParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)




    def data(self):

        localctx = subleqasmParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==subleqasmParser.VARIABLE:
                self.state = 32
                self.label()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==subleqasmParser.NEWLINE:
                    self.state = 33
                    self.match(subleqasmParser.NEWLINE)
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 41
            self.literal()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==subleqasmParser.NEWLINE:
                self.state = 42
                self.match(subleqasmParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(subleqasmParser.ExprContext,0)


        def getRuleIndex(self):
            return subleqasmParser.RULE_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVal" ):
                listener.enterVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVal" ):
                listener.exitVal(self)




    def val(self):

        localctx = subleqasmParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return subleqasmParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MinExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(subleqasmParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(subleqasmParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinExpr" ):
                listener.enterMinExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinExpr" ):
                listener.exitMinExpr(self)


    class SumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(subleqasmParser.PLUS, 0)
        def expr(self):
            return self.getTypedRuleContext(subleqasmParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumExpr" ):
                listener.enterSumExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumExpr" ):
                listener.exitSumExpr(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(subleqasmParser.ExprContext)
            else:
                return self.getTypedRuleContext(subleqasmParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(subleqasmParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(subleqasmParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(subleqasmParser.ExprContext)
            else:
                return self.getTypedRuleContext(subleqasmParser.ExprContext,i)

        def MULT(self):
            return self.getToken(subleqasmParser.MULT, 0)
        def DIV(self):
            return self.getToken(subleqasmParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)


    class LabelExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self):
            return self.getTypedRuleContext(subleqasmParser.LabelContext,0)

        def expr(self):
            return self.getTypedRuleContext(subleqasmParser.ExprContext,0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(subleqasmParser.NEWLINE)
            else:
                return self.getToken(subleqasmParser.NEWLINE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelExpr" ):
                listener.enterLabelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelExpr" ):
                listener.exitLabelExpr(self)


    class AtoExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(subleqasmParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtoExpr" ):
                listener.enterAtoExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtoExpr" ):
                listener.exitAtoExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = subleqasmParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = subleqasmParser.MinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 48
                self.match(subleqasmParser.MINUS)
                self.state = 49
                self.expr(6)
                pass

            elif la_ == 2:
                localctx = subleqasmParser.SumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(subleqasmParser.PLUS)
                self.state = 51
                self.expr(5)
                pass

            elif la_ == 3:
                localctx = subleqasmParser.AtoExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.atom()
                pass

            elif la_ == 4:
                localctx = subleqasmParser.LabelExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.label()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==subleqasmParser.NEWLINE:
                    self.state = 54
                    self.match(subleqasmParser.NEWLINE)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 70
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = subleqasmParser.MulExprContext(self, subleqasmParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 65
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==subleqasmParser.MULT or _la==subleqasmParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 66
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = subleqasmParser.AddExprContext(self, subleqasmParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 68
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==subleqasmParser.PLUS or _la==subleqasmParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.expr(4)
                        pass

             
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return subleqasmParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAR(self):
            return self.getToken(subleqasmParser.OPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(subleqasmParser.ExprContext,0)

        def CPAR(self):
            return self.getToken(subleqasmParser.CPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParExpr" ):
                listener.enterParExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParExpr" ):
                listener.exitParExpr(self)


    class VarAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(subleqasmParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarAtom" ):
                listener.enterVarAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarAtom" ):
                listener.exitVarAtom(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a subleqasmParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(subleqasmParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)



    def atom(self):

        localctx = subleqasmParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [subleqasmParser.OPAR]:
                localctx = subleqasmParser.ParExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(subleqasmParser.OPAR)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(subleqasmParser.CPAR)
                pass
            elif token in [subleqasmParser.NUMBER]:
                localctx = subleqasmParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(subleqasmParser.NUMBER)
                pass
            elif token in [subleqasmParser.VARIABLE]:
                localctx = subleqasmParser.VarAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(subleqasmParser.VARIABLE)
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


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(subleqasmParser.VARIABLE, 0)

        def COLON(self):
            return self.getToken(subleqasmParser.COLON, 0)

        def getRuleIndex(self):
            return subleqasmParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = subleqasmParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(subleqasmParser.VARIABLE)
            self.state = 84
            self.match(subleqasmParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SepContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(subleqasmParser.COMMA, 0)

        def NEWLINE(self):
            return self.getToken(subleqasmParser.NEWLINE, 0)

        def getRuleIndex(self):
            return subleqasmParser.RULE_sep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSep" ):
                listener.enterSep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSep" ):
                listener.exitSep(self)




    def sep(self):

        localctx = subleqasmParser.SepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==subleqasmParser.COMMA or _la==subleqasmParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTEDALPHANUM(self):
            return self.getToken(subleqasmParser.QUOTEDALPHANUM, 0)

        def getRuleIndex(self):
            return subleqasmParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = subleqasmParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(subleqasmParser.QUOTEDALPHANUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




