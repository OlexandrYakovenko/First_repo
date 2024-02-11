import random
# def max(list=None):
#     if list is not None:
#         max=0
#         for i in list:
#             if max<i:
#                 max=i
#     return max



# list=[]
# while len(list)<10:
#     a=random.randint(0,10)
#     if a not in list:
#         list.append(a)
# print(list)
# print(max(list))
# random.setstate(state)
random.seed()
list1=[]
while len(list1)<10:
    a=random.randint(0,10)
    if a not in list1:
        list1.append(a)
print(list1)
s=random.sample(list1,6)
print(s)
# print(max(list1))

