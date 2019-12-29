

# Word size in bytes
WORD_SIZE=2


class Word:


    def __init__(self):
        self.data=bytearray(WORD_SIZE)

    # returns a signed integer
    def get(self):
        val=0
        mask=2**(8*WORD_SIZE-1)
        for i in range(WORD_SIZE-1,-1,-1):
            val+=self.data[i]*(256**i)

        if val>mask:
            # negative
            val=mask-val

        return val

    # returns string with hexdump
    def get_raw(self):
        v=""
        for i in range(0,WORD_SIZE):
            v="{:02x}".format(self.data[i])+v
        return v

    def get_unsigned(self):
        val=0

        mask=2**(8*WORD_SIZE-1)
        for i in range(WORD_SIZE-1,-1,-1):
            val+=self.data[i]*(256**i)

        return val

    # Little endian. Stores the least significant value in the lowest position
    # Negative numbers have 1 in the most significant bit
    def set(self, value):
        if value<0:
            negative=True
            value= -value
        else:
            negative=False
        mask=255
        for i in range(0,WORD_SIZE):
            self.data[i]=(value & mask)
            value=value >> 8
            if (i==WORD_SIZE-1) and negative:
                self.data[i]=self.data[i] | 128


    def get_byte(self,i):
        return self.data[i]


# a=Word()
# a.set(-1)
# print (a.get())
