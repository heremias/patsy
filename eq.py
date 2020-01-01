import random
import sys
import os

class Equilizer:
    def __init__(self):    
        cnum1 = "48"
        cnum2 = "5"
        cube = 5**5
        pre = "\033[" + cnum1 + ";" + cnum2 + ";"
        block = "m            "
        for color in range(0, cube, 1):
            bseq0 = "\033[0;0;m"
            color1 = str(random.randrange(16, 51, 1))
            color2 = str(random.randrange(52, 87, 1))
            color3 = str(random.randrange(88, 123, 1))
            color4 = str(random.randrange(124, 159, 1))
            color5 = str(random.randrange(160, 195, 1))
            color6 = str(random.randrange(196, 231, 1))
            color7 = str(random.randrange(196, 231, 1))
            bseq1 = pre + color1
            bseq2 = pre + color2
            bseq3 = pre + color3
            bseq4 = pre + color4
            bseq5 = pre + color5
            bseq6 = pre + color6
            bseq7 = pre + color7
            sys.stdout.write(bseq1 + block + bseq0)
            sys.stdout.write(bseq2 + block + bseq0)
            sys.stdout.write(bseq3 + block + bseq0)
            sys.stdout.write(bseq4 + block + bseq0)
            sys.stdout.write(bseq5 + block + bseq0)
            sys.stdout.write(bseq6 + block + bseq0)
            sys.stdout.write(bseq7 + block + bseq0)
            sys.stdout.flush()
            os.system("clear")
        return

if __name__ == "__main__":
    pass