"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
import math

x = int(input('Input number: '))

odd = 0
even = 0

def last_odd_or_even(x):
  global odd, even
  last_digit = x % 10
  if last_digit % 2 == 0:
    even += 1
  else:
    odd += 1

last_odd_or_even(x)

while x >= 10:
  x = math.floor(x / 10)
  last_odd_or_even(x)

print('Odd:', odd)
print('Even:', even)