from MV import *
from compiler import *
from antlr4 import FileStream



logging.basicConfig(filename="sem.log",level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

inputfile=FileStream("hello.slq")
#stream = antlr4.InputStream("1,2,3")
S=Compiler(inputfile)
S.Walk()

J=MV()
J.load(S.Context['instr'])
# i=[15, 17, -1,
#    17, -1, -1,
#    16, 1, -1,
#    16, 3, -1,
#    15, 15, 0,
#    0, -1, 72,
#    101, 108, 108,
#    111, 44, 32,
#    119, 111, 114,
#    108, 100, 33,
#    10, 0]
#J.load(i)
# J.load(0,3,4,6)
# J.load(3,7,7,7)
# J.load(6,3,4,6)

while(True):
    J.step()
