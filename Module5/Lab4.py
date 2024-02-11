from collections import defaultdict

d1=defaultdict()
d1.default_factory=int
s1="абагаламага"
for letter in s1:
    d1[letter]+=1       
print(d1)
d1['s1']=s1
d1.default_factory=set
for letter in s1:
    d1["uniq"].update(letter)
print(d1)
