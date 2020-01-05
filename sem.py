import logging
logger = logging.getLogger(__name__)

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
        logger.debug("enterProgram %s",ctx.getText())
        self.MemPointer=0
        pass

    # Exit a parse tree produced by subleqasmParser#program.
    def exitProgram(self, ctx:subleqasmParser.ProgramContext):
        pass


    # Enter a parse tree produced by subleqasmParser#instr.
    def enterInstr(self, ctx:subleqasmParser.InstrContext):
        pass

    # Exit a parse tree produced by subleqasmParser#instr.
    def exitInstr(self, ctx:subleqasmParser.InstrContext):
        logger.debug("exitInstr %s",ctx.getText())
        if self.Context['stage']==2:
            c=self.pop()
            b=self.pop()
            a=self.pop()
            instr=[a,b,c]
            self.Context['instr']+=instr


    # Enter a parse tree produced by subleqasmParser#data.
    def enterData(self, ctx:subleqasmParser.DataContext):
        pass

    # Exit a parse tree produced by subleqasmParser#data.
    def exitData(self, ctx:subleqasmParser.DataContext):
        logger.debug("exitData %s",ctx.getText())

        if self.Context['stage']==2:
            instrs=[]
            l=self.pop()
            while(l>=3):
                a=self.pop()
                b=self.pop()
                c=self.pop()
                instr=[a,b,c]
                instrs=instrs+instr
                l-=3
            if l>0:
                pad=3-l
                instr=[]
                for i in range(0,l):
                    a=self.pop()
                    instr.append(a)
                for i in range(0,pad):
                    instr.append(0)
                instrs=instrs+instr
            for i in instrs:
                self.Context['instr'].append(i)



    # Enter a parse tree produced by subleqasmParser#val.
    def enterVal(self, ctx:subleqasmParser.ValContext):
        pass

    # Exit a parse tree produced by subleqasmParser#val.
    def exitVal(self, ctx:subleqasmParser.ValContext):
        logger.debug("exitVal %s",ctx.getText())

        self.MemPointer+=1




    # Enter a parse tree produced by subleqasmParser#valLiteral.
    def enterLiteral(self, ctx:subleqasmParser.LiteralContext):
        logger.debug("enterLiteral %s",ctx.getText())

        if self.Context['stage']==2:
            # Remove the quotes
            l=ctx.getText()[1:-1]
            lon=len(l)
            for i in l[::-1]:
                self.push(ord(i))
            # and finally pushes the length of the literal
            self.push(lon)
            # pad=3-(lon%3)
            # if pad<3:
            #     for i in range(0,pad):
            #         self.push(0)


    # Exit a parse tree produced by subleqasmParser#valLiteral.
    def exitLiteral(self, ctx:subleqasmParser.LiteralContext):
        logger.debug("exitLiteral %s",ctx.getText())

        l=ctx.getText()
        # Modify the mempointer with the length of the literal without the quotes
        self.MemPointer+=len(l)-2
        pass

    # Enter a parse tree produced by subleqasmParser#minExpr.
    def enterMinExpr(self, ctx:subleqasmParser.MinExprContext):
        pass

    # Exit a parse tree produced by subleqasmParser#minExpr.
    def exitMinExpr(self, ctx:subleqasmParser.MinExprContext):
        logger.debug("exitMinExpr %s",ctx.getText())
        if self.Context['stage']==2:
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
        logger.debug("exitAddExpr %s",ctx.getText())
        if self.Context['stage']==2:
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
        logger.debug("exitMulExpr %s",ctx.getText())
        if self.Context['stage']==2:
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
        logger.debug("enterNumberAtom %s",ctx.getText())
        if self.Context['stage']==2:
            self.push(int(ctx.getText()))

    # Exit a parse tree produced by subleqasmParser#numberAtom.
    def exitNumberAtom(self, ctx:subleqasmParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by subleqasmParser#varAtom.
    def enterVarAtom(self, ctx:subleqasmParser.VarAtomContext):
        logger.debug("enterVarAtom %s",ctx.getText())

        if self.Context['stage']==2:
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
        logger.debug("enterLabel %s",ctx.getText())
        # remove the colon
        l=ctx.getText()[:-1]
        self.Labels[l]=self.MemPointer


    # Exit a parse tree produced by subleqasmParser#label.
    def exitLabel(self, ctx:subleqasmParser.LabelContext):
        pass





