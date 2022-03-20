a = list(input("Введите первое число"))
b = list(input("Введите второе число"))

suma = hex(int(''.join(a), 16) + int(''.join(b), 16)).split('0x')[1]
multiplication = hex(int(''.join(a), 16) * int(''.join(b), 16)).split('0x')[1]

print(suma, multiplication)