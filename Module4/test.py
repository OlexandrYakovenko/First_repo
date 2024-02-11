import sys
print(__file__)
print(sys.argv[0])
if len(sys.argv)==2:
    fname=sys.argv[1]
    with open(fname,"r") as file:
        print(file.read())