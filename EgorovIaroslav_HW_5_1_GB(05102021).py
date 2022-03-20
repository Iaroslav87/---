firma = {}
n = int(input("Количество предприятий"))
s = 0
for i in range(n):
    fName = input(str(i + 1) + "фирма")
    volume = int(input("Прибыль "))
    firma[fName] = volume
    s += volume

avrg = s / n
print("Средняя прибыль {}".format(avrg))
for i in firma:
    if firma[i] > avrg:
        print(i)
