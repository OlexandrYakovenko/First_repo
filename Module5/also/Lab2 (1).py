from pathlib import Path

path=Path('data.txt')
def total_salary(path):
    with open(path, 'r') as fh:
        fh=fh.readlines()
        outlist=[]
    for line in fh:
        line=line.split(",")    
        outlist.append(int(line[1]))
    s=sum(outlist)
    a=s/len(outlist)
    print(f'total:{s}, avg:{a}')
    return s,a