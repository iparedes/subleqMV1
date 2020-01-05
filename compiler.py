import antlr4
from gen.subleqasmLexer  import *
from sem import *

class Compiler():

    def __init__(self,stream):
        self.Walker=None
        self.Tree=None
        self.Stage=0
        self.seq=None
        self.Context={}
        self.Context['instr']=[]
        self.Context['stage']=0

        lexer = subleqasmLexer(stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = subleqasmParser(tokens)

        self.Tree=parser.program()
        self.Walker=ParseTreeWalker()


    def Walk(self):
        # First time we walk is for the preprocessing of labels
        # Stes stage to one and Create the sem listener
        self.Context['stage']=1
        seq=Sem(self.Context)
        self.Walker.walk(seq,self.Tree)
        # In the next we set stage to 2 and do the walk for the semantic analysis
        self.Context['stage']=2
        self.Walker.walk(seq,self.Tree)


