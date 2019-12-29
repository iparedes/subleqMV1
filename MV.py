from Word import *

MAX_MEM=1000
CODE_START=0

class MV:
    def __init__(self):
        self.mem=[Word() for i in range(MAX_MEM)]
        self.PC=CODE_START

    # https://unnikked.ga/subleq-a-one-instruction-set-computer-16c7a164a01
    # The subleq instruction subtracts the contents at address a from the contents at address b
    # stores the result at addresses b, and then
    # if the result is not positive, transfers control to address c
    # (if the result is positive, execution proceeds to the next instruction in sequence).
    def step(self):
        a=self.mem_get(self.PC)
        b=self.mem_get(self.PC+1)
        c=self.mem_get(self.PC+2)

        va=self.mem_get(a)
        vb=self.mem_get(b)
        vb=vb-va
        self.mem_set(b,vb)

        if vb<=0:
            self.PC=c
        else:
            self.PC+=3


    def mem_get(self,dir):
        # make sure dir is in bounds
        if (dir<0) or (dir>=MAX_MEM):
            dir = dir % MAX_MEM

        return self.mem[dir].get()

    def mem_get_raw(self,dir):
        # make sure dir is in bounds
        if (dir<0) or (dir>=MAX_MEM):
            dir = dir % MAX_MEM

        return self.mem[dir].get_raw()


    def mem_set(self,dir,value):
        if (dir<0 or dir>=MAX_MEM):
            dir = dir % MAX_MEM
        self.mem[dir].set(value)

    def load(self,dir,a,b,c):
        self.mem_set(dir,a)
        self.mem_set(dir+1,b)
        self.mem_set(dir+2,c)



# J=MV()
# J.load(0,3,4,6)
# J.load(3,7,7,7)
# J.load(6,3,4,6)
#
# while(True):
#     J.step()
