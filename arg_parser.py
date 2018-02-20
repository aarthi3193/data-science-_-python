
# coding: utf-8

# In[ ]:
import sys


def add(a,b):
    print (int(a)+int (b))
def sub(a,b):
    print (int(a)-int (b))
def mul(a,b):
    print (int(a)*int (b))
def div(a,b):
    print (int(a)%int (b))    


def main(args):
    sub(args[0],args[1])

if __name__ == "__main__":
    args = sys.argv[1:]
    if len (args) < 2 :
        print ("Less than 2 args")
        sys.exit (1)
    main(args)

