from decimal import *
getcontext().prec=6
print((Decimal("1.1")+Decimal("2.2")))

# number = Decimal("0.445")
# number = number.quantize(Decimal("1.23"))
# print(number)      

# number = Decimal("10.035")  
# print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))     