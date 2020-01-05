import sys
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
        # a=self.mem_get(self.PC)
        # b=self.mem_get(self.PC+1)
        # c=self.mem_get(self.PC+2)

        # va=self.mem_get(a)
        # vb=self.mem_get(b)
        # vb=vb-va
        


        a=self.mem_get(self.PC)
        b=self.mem_get(self.PC+1)
        c=self.mem_get(self.PC+2)

        if (a==-1):
            # input
            v=ord(sys.stdin.read(1))
            self.mem_set(b,v)
            self.PC+=3
        elif (b==-1):
            # output
            print(chr(self.mem_get(a)),)
            self.PC+=3
        else:
            va=self.mem_get(a)
            vb=self.mem_get(b)
            v=vb-va
            self.mem_set(b,v)

            if v<=0:
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

    def load_inst(self,dir,a,b,c):
        self.mem_set(dir,a)
        self.mem_set(dir+1,b)
        self.mem_set(dir+2,c)

    def load(self,vals):
        dir=0
        while vals:
            item=vals[:3]
            del vals[:3]
            for i in range(0,len(item)%3):
                item.append(0)
            self.load_inst(dir,item[0],item[1],item[2])
            dir+=3

    # returns dump in integers the instruction starting at addr
    def dump_inst_int(self,addr):
        val=str(self.mem_get(addr))+" "+str(self.mem_get(addr+1))+" "+str(self.mem_get(addr+2))
        return val

    # returns dump in integers the instruction starting at addr
    def dump_inst_hex(self,addr):
        val="{:02x}".format(self.mem_get(addr))+" "+"{:02x}".format(self.mem_get(addr+1))+" "+"{:02x}".format(self.mem_get(addr+2))
        return val



