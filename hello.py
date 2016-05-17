import sys

def main(argv):
    if (len(argv)>0):
        print("Hello "+' '.join(argv)+"!")
    else:
        print("Hello everybody!")
main(sys.argv[1:])
