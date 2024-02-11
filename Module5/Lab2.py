from collections import namedtuple as nt
# t1=("red",123234)
#print(t1)
# nt1=nt('Vehicle',['color','mileage'])
#print(nt1)
# car1=nt1("red",12345)
# print(car1)
# # print(car1.color)
# nt2=nt('Pet',"name type age")
# pets=[nt2('Vasyl',"cat",10),
# nt2('Sirko',"dog",5),
# nt2('Kesha',"parrot",2)]
# for pet in pets:
#     print(pet.age)

l1=[[1,2000],
[2,100],
[15,100],
[16,80000]]

car=nt('Vehicle',['color','mileage'])
# car1=car("red",12345)
# car2=car1._replace(mileage=2345,color=15)
# print(car2)
l2=[]
for pars in l1:
    l2.append(car._make(pars)._asdict()) #На численні прохання
print(l2)