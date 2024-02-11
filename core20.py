# rate = 1.68
# night_rate = rate / 2
# value_day = 10
# value_night = 20
# payment = rate * value_day + night_rate * value_night
# print(payment)

# length = 2.75
# width = 1.75
# area = length * width
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# print(show)

# length = "2.75"
# width = "1.75"
# area = float(length) * float(width)
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# print(show)

# name = input("Your name? ")
# print(name)
# email = input("Your email? ")
# print(email)
# age = int(input("Your age? "))
# print(age)
# height = float(input("Your height? "))
# print(height)
# is_active = input("Your is_active? ") != ""
# print(is_active)

# length = float(input("Input length?"))
# width = float(input("Input width?"))
# area = length * width
# print(area)

# my_list = []
# my_list.insert(0,2024)
# my_list.insert(1,"Python")
# my_list.insert(2,3.12)
# for i in range(3):
#     elem=my_list[i]
#     print(elem)

# my_list = [2024, 3.12]
# some_data = ['Python']
# my_list.extend(some_data)
# # for i in range(3):
# #     print(my_list[i])
    
# my_list.insert(1,"Python")
# # for i in range(len(my_list)):
# #     print(my_list[i])
    
# my_list.reverse()
# for i in range(len(my_list)):
#     print(my_list[i])

# data = {"year":2024,"lang":"Python","version":3.12}
# for i in data:
#     print("key="+ str(i) + "; value="+ str(data[i]))

# cat = {}
# info = {"status": "vaccinated", "breed": True}
# #cat.extend(info)
# #cat = {value: key for key, value in info.items()} 
# cat.update(info)

# # for i in cat:
# #     print(cat[i])
# cat["nick"] = "Simon"
# cat["age"] = 7
# cat["characteristics"] = ["лагідний", "кусається"]
# print(cat) 
# age = cat.get("age")
# print(age)


# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price * (1-discount)
#         return price
        

#     apply_discount()    
#     return price

# new_price=discount_price(100,0.10)
# print(new_price)

# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)  # Виведе: Привіт, Олексій!

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def number_of_groups(n, k):
#     return int(factorial(n) / (factorial(n-k) * factorial(k)))
    
    
# n = int(input("Input n "))  
# k = int(input("Input k ")) 

# number_of_groups_result = number_of_groups(n,k)
# print("number_of_groups_result="+str(number_of_groups_result) ) 


def first(size, *args):
    print(len(args))
    for arg in args:
        size=size+1
    return size

def second(size, **kwargs):
    print(len(kwargs.items()))
    print(len(kwargs))
    for key, value in kwargs.items():
        size=size+1
    return size

first(1,2,3)
second(0,f=1,r=2)