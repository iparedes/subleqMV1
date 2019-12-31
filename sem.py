from gen.subleqasmListener import *


class Sem(subleqasmListener):

    def __init__(self,context):
        self.MemPointer=0
        self.Stack=[]
        self.Labels={}
        self.Context=context


    def push(self,val):
        self.Stack.append(val)

    def pop(self):
        a=self.Stack.pop()
        return a


        # Enter a parse tree produced by subleqasmParser#program.
    def enterProgram(self, ctx:subleqasmParser.ProgramContext):
        pass

    # Exit a parse tree produced by subleqasmParser#program.
    def exitProgram(self, ctx:subleqasmParser.ProgramContext):
        pass


    # Enter a parse tree produced by subleqasmParser#instr.
    def enterInstr(self, ctx:subleqasmParser.InstrContext):
        pass

    # Exit a parse tree produced by subleqasmParser#instr.
    def exitInstr(self, ctx:subleqasmParser.InstrContext):
        c=self.pop()
        b=self.pop()
        a=self.pop()
        instr=[a,b,c]
        self.Context['instr'].append(instr)

    # Enter a parse tree produced by subleqasmParser#val.
    def enterVal(self, ctx:subleqasmParser.ValContext):
        pass

    # Exit a parse tree produced by subleqasmParser#val.
    def exitVal(self, ctx:subleqasmParser.ValContext):
        self.MemPointer+=1


    # Enter a parse tree produced by subleqasmParser#minExpr.
    def enterMinExpr(self, ctx:subleqasmParser.MinExprContext):
        pass

    # Exit a parse tree produced by subleqasmParser#minExpr.
    def exitMinExpr(self, ctx:subleqasmParser.MinExprContext):
        a=self.pop()
        a=-a
        self.push(a)


    # Enter a parse tree produced by subleqasmParser#sumExpr.
    def enterSumExpr(self, ctx:subleqasmParser.SumExprContext):
        pass

    # Exit a parse tree produced by subleqasmParser#sumExpr.
    def exitSumExpr(self, ctx:subleqasmParser.SumExprContext):
        pass

    # Enter a parse tree produced by subleqasmParser#addExpr.
    def enterAddExpr(self, ctx:subleqasmParser.AddExprContext):
        pass

    # Exit a parse tree produced by subleqasmParser#addExpr.
    def exitAddExpr(self, ctx:subleqasmParser.AddExprContext):
        b=self.pop()
        a=self.pop()

        if ctx.op.type == subleqasmParser.PLUS:
            self.push(a+b)
        else:
            self.push(a-b)


    # Enter a parse tree produced by subleqasmParser#mulExpr.
    def enterMulExpr(self, ctx:subleqasmParser.MulExprContext):
        pass

    # Exit a parse tree produced by subleqasmParser#mulExpr.
    def exitMulExpr(self, ctx:subleqasmParser.MulExprContext):
        b=self.pop()
        a=self.pop()

        if ctx.op.type == subleqasmParser.MULT:
            self.push(a*b)
        else:
            self.push(int(a/b))


    # Enter a parse tree produced by subleqasmParser#labelExpr.
    def enterLabelExpr(self, ctx:subleqasmParser.LabelExprContext):
        pass

    # Exit a parse tree produced by subleqasmParser#labelExpr.
    def exitLabelExpr(self, ctx:subleqasmParser.LabelExprContext):
        pass


    # Enter a parse tree produced by subleqasmParser#atoExpr.
    def enterAtoExpr(self, ctx:subleqasmParser.AtoExprContext):
        pass

    # Exit a parse tree produced by subleqasmParser#atoExpr.
    def exitAtoExpr(self, ctx:subleqasmParser.AtoExprContext):
        pass


    # Enter a parse tree produced by subleqasmParser#parExpr.
    def enterParExpr(self, ctx:subleqasmParser.ParExprContext):
        pass

    # Exit a parse tree produced by subleqasmParser#parExpr.
    def exitParExpr(self, ctx:subleqasmParser.ParExprContext):
        pass


    # Enter a parse tree produced by subleqasmParser#numberAtom.
    def enterNumberAtom(self, ctx:subleqasmParser.NumberAtomContext):
        self.push(int(ctx.getText()))

    # Exit a parse tree produced by subleqasmParser#numberAtom.
    def exitNumberAtom(self, ctx:subleqasmParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by subleqasmParser#varAtom.
    def enterVarAtom(self, ctx:subleqasmParser.VarAtomContext):
        l=ctx.getText()
        a=self.Labels[l]
        self.push(a)

    # Exit a parse tree produced by subleqasmParser#varAtom.
    def exitVarAtom(self, ctx:subleqasmParser.VarAtomContext):
        pass


    # Enter a parse tree produced by subleqasmParser#sep.
    def enterSep(self, ctx:subleqasmParser.SepContext):
        pass

    # Exit a parse tree produced by subleqasmParser#sep.
    def exitSep(self, ctx:subleqasmParser.SepContext):
        pass


    # Enter a parse tree produced by subleqasmParser#label.
    def enterLabel(self, ctx:subleqasmParser.LabelContext):
        # remove the colon
        l=ctx.getText()[:-1]
        self.Labels[l]=self.MemPointer


    # Exit a parse tree produced by subleqasmParser#label.
    def exitLabel(self, ctx:subleqasmParser.LabelContext):
        pass





