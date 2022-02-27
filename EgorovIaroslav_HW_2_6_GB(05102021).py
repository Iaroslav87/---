"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше
введенное пользователем число, чем то, что загадано. Если за 10 попыток
число не отгадано, то вывести загаданное число.
"""
import random

mysterious_number = random.randrange(0, 100)

for i in range(10, 0, -1):
  x = int(input('Your guess: '))
  if x == mysterious_number:
    print('Right!')
    exit()
  elif x < mysterious_number:
    print('Too small')
  else:
    print('Too big')

print('You lose. The answer was: ', mysterious_number)