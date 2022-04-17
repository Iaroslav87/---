"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода
для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""
from memory_profiler import profile
from pympler import asizeof

@profile
def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

@profile
def myFunc(n):
    b = []
    for i in range(2, n):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            b.append(i)
    return b


if __name__ == "__main__":
    myFunc(100)
    eratosthenes(100)
print(asizeof.asizeof(eratosthenes(100))) #1668
print(asizeof.asizeof(myFunc(100))) #1056

"""
Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     37.1 MiB     37.1 MiB           1   @profile
     5                                         def eratosthenes(n):
     6     37.1 MiB      0.0 MiB           1       sieve = list(range(n + 1))
     7     37.1 MiB      0.0 MiB           1       sieve[1] = 0  # без этой строки итоговый список будет содержать единицу
     8     37.1 MiB      0.0 MiB         102       for i in sieve:
     9     37.1 MiB      0.0 MiB         101           if i > 1:
    10     37.1 MiB      0.0 MiB         171               for j in range(i + i, len(sieve), i):
    11     37.1 MiB      0.0 MiB         146                   sieve[j] = 0
    12     37.1 MiB      0.0 MiB           1       return sieve


1688
Filename: main.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    14     37.1 MiB     37.1 MiB           1   @profile
    15                                         def myFunc(n):
    16     37.1 MiB      0.0 MiB           1       b = []
    17     37.1 MiB      0.0 MiB          99       for i in range(2, n):
    18     37.1 MiB      0.0 MiB          98           result = True
    19     37.1 MiB      0.0 MiB        4851           for j in range(2, i):
    20     37.1 MiB      0.0 MiB        4753               if i % j == 0:
    21     37.1 MiB      0.0 MiB         276                   result = False
    22     37.1 MiB      0.0 MiB          98           if result:
    23     37.1 MiB      0.0 MiB          25               b.append(i)
    24     37.1 MiB      0.0 MiB           1       return b


1056

"""