from MV import *
from compiler import *


stream = antlr4.InputStream("start:1+5,7-8,start")
S=Compiler(stream)
S.Walk()
a=S.Context['instr']





J=MV()
i=[15, 17, -1,
   17, -1, -1,
   16, 1, -1,
   16, 3, -1,
   15, 15, 0,
   0, -1, 72,
   101, 108, 108,
   111, 44, 32,
   119, 111, 114,
   108, 100, 33,
   10, 0]
J.load(i)
# J.load(0,3,4,6)
# J.load(3,7,7,7)
# J.load(6,3,4,6)

while(True):
    #print(J.dump_inst_int(J.PC))
    J.step()
