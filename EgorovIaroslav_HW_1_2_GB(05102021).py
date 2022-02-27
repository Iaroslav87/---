"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
num1 = int(input("Введите 1е число"))
num2 = int(input("Введите 2е число"))
num3 = int(input("Введите 3е число"))
# num 1
if (num2 < num1 < num3) or (num3 < num1 < num2):
    print(num1)
# num 2
if (num1 < num2 < num3) or (num3 < num2 < num1):
    print(num2)
# num 3
if (num1 < num3 < num2) or (num2 < num3 < num1):
    print(num3)