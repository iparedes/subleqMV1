# Generated from /Users/nacho/Documents/python-projects/movemak/subleqasm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("H\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\'\n")
        buf.write("\5\f\5\16\5*\13\5\3\5\3\5\5\5.\n\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\7\5\66\n\5\f\5\16\59\13\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6A\n\6\3\7\3\7\3\b\3\b\3\b\3\b\2\3\b\t\2\4\6\b\n\f")
        buf.write("\16\2\5\3\2\6\7\3\2\b\t\4\2\n\n\16\16\2I\2\21\3\2\2\2")
        buf.write("\4\25\3\2\2\2\6\34\3\2\2\2\b-\3\2\2\2\n@\3\2\2\2\fB\3")
        buf.write("\2\2\2\16D\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2\2\22\23\3")
        buf.write("\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25\26")
        buf.write("\5\6\4\2\26\27\5\f\7\2\27\30\5\6\4\2\30\31\5\f\7\2\31")
        buf.write("\32\5\6\4\2\32\33\7\16\2\2\33\5\3\2\2\2\34\35\5\b\5\2")
        buf.write("\35\7\3\2\2\2\36\37\b\5\1\2\37 \7\t\2\2 .\5\b\5\b!\"\7")
        buf.write("\b\2\2\".\5\b\5\7#.\5\n\6\2$(\5\16\b\2%\'\7\16\2\2&%\3")
        buf.write("\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2*(\3\2")
        buf.write("\2\2+,\5\b\5\3,.\3\2\2\2-\36\3\2\2\2-!\3\2\2\2-#\3\2\2")
        buf.write("\2-$\3\2\2\2.\67\3\2\2\2/\60\f\6\2\2\60\61\t\2\2\2\61")
        buf.write("\66\5\b\5\7\62\63\f\5\2\2\63\64\t\3\2\2\64\66\5\b\5\6")
        buf.write("\65/\3\2\2\2\65\62\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\67")
        buf.write("8\3\2\2\28\t\3\2\2\29\67\3\2\2\2:;\7\f\2\2;<\5\b\5\2<")
        buf.write("=\7\r\2\2=A\3\2\2\2>A\7\3\2\2?A\7\5\2\2@:\3\2\2\2@>\3")
        buf.write("\2\2\2@?\3\2\2\2A\13\3\2\2\2BC\t\4\2\2C\r\3\2\2\2DE\7")
        buf.write("\5\2\2EF\7\13\2\2F\17\3\2\2\2\b\23(-\65\67@")
        return buf.getvalue()


class subleqasmParser ( Parser ):

    grammarFileName = "subleqasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'*'", "'/'", "'+'", "'-'", "','", "':'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "DIGIT", "VARIABLE", "MULT", 
                      "DIV", "PLUS", "MINUS", "COMMA", "COLON", "OPAR", 
                      "CPAR", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_instr = 1
    RULE_val = 2
    RULE_expr = 3
    RULE_atom = 4
    RULE_sep = 5
    RULE_label = 6

    ruleNames =  [ "program", "instr", "val", "expr", "atom", "sep", "label" ]

    EOF = Token.EOF
    NUMBER=1
    DIGIT=2
    VARIABLE=3
    MULT=4
    DIV=5
    PLUS=6
    MINUS=7
    COMMA=8
    COLON=9
    OPAR=10
    CPAR=11
    NEWLINE=12
    WS=13

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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.instr()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << subleqasmParser.NUMBER) | (1 << subleqasmParser.VARIABLE) | (1 << subleqasmParser.PLUS) | (1 << subleqasmParser.MINUS) | (1 << subleqasmParser.OPAR))) != 0)):
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.val()
            self.state = 20
            self.sep()
            self.state = 21
            self.val()
            self.state = 22
            self.sep()
            self.state = 23
            self.val()
            self.state = 24
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
        self.enterRule(localctx, 4, self.RULE_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = subleqasmParser.MinExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 29
                self.match(subleqasmParser.MINUS)
                self.state = 30
                self.expr(6)
                pass

            elif la_ == 2:
                localctx = subleqasmParser.SumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(subleqasmParser.PLUS)
                self.state = 32
                self.expr(5)
                pass

            elif la_ == 3:
                localctx = subleqasmParser.AtoExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.atom()
                pass

            elif la_ == 4:
                localctx = subleqasmParser.LabelExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.label()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==subleqasmParser.NEWLINE:
                    self.state = 35
                    self.match(subleqasmParser.NEWLINE)
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 41
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = subleqasmParser.MulExprContext(self, subleqasmParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 46
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==subleqasmParser.MULT or _la==subleqasmParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = subleqasmParser.AddExprContext(self, subleqasmParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 49
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==subleqasmParser.PLUS or _la==subleqasmParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(4)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [subleqasmParser.OPAR]:
                localctx = subleqasmParser.ParExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(subleqasmParser.OPAR)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(subleqasmParser.CPAR)
                pass
            elif token in [subleqasmParser.NUMBER]:
                localctx = subleqasmParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(subleqasmParser.NUMBER)
                pass
            elif token in [subleqasmParser.VARIABLE]:
                localctx = subleqasmParser.VarAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
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
        self.enterRule(localctx, 10, self.RULE_sep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
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
            self.state = 66
            self.match(subleqasmParser.VARIABLE)
            self.state = 67
            self.match(subleqasmParser.COLON)
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
        self._predicates[3] = self.expr_sempred
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
         




