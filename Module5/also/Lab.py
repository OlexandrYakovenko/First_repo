from Lab2 import PI,G,sum
def f1():
    print("Something other")
    print(f"__name__=={__name__}")
print(__file__)
if __name__=="__main__":
    f1()
    print(PI)
    print(G)

