from collections import Counter
# s1="бАабагаламага"
d1={'apple':7,"banana":10,"orange":6}
c1=Counter(d1)
# print(c1)
# d2={'apple':20,"orange":20}
# c1.update(d2)
# print(c1)
# d3={'apple':200,"banana":2,"orange":2}
# c1.subtract(d3)
# print(c1)
# c1=Counter(s1)
# print(c1)
# c1.update('амальгама')
# print(c1)
# c1.subtract('амальгама')
print(c1)
c1.subtract(['apple','apple','apple','apple',"banana"])
print(c1)
