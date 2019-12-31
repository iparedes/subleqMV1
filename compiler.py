import antlr4
from gen.subleqasmLexer  import *
from sem import *

class Compiler():

    def __init__(self,stream):
        self.Walker=None
        self.Tree=None
        self.Context={}
        self.Context['instr']=[]

        lexer = subleqasmLexer(stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = subleqasmParser(tokens)

        self.Tree=parser.program()
        self.Walker=ParseTreeWalker()


    def Walk(self):
        seq=Sem(self.Context)
        self.Walker.walk(seq,self.Tree)
