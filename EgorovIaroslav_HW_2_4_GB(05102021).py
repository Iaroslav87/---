"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
n = int(input('Input n: '))

if n == 0:
  print('Sum:', 0)
  exit()

result = 1

for i in range(1, n):
  if i % 2 == 0:
    result += 1 / (2**i)
  else:
    result += 1 / -(2**i)

print('Sum:', result)
