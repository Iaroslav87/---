"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
"""

import timeit
import cProfile

def func_v1(m:int = 100, n:int = 1000):
    from random import randint
    from collections import Counter
    a = [randint(0, m) for _ in range(n)]
    res = Counter(a).most_common()[0]
    print(f'Значение {res[0]} повторяется {res[1]} раза, что чаще всего')

def func_v2(m:int = 100, n:int = 1000):
    from random import randint
    b = {}
    a = [randint(0, m) for _ in range(n)]
    for i in a:
        b.update({i: b.get(i, 0) + 1})
    max_val = max([i for _, i in b.items()])
    res = [(idx, val) for idx, val in b.items() if val == max_val][0]
    print(f'Значение {res[0]} повторяется {res[1]} раза, что чаще всего')

cProfile.run('func_v1(10, 100)')
# Значение 6 повторяется 13 раза, что чаще всего
# 1965 function calls (1930 primitive calls) in 0.004 seconds
cProfile.run('func_v1(10000, 100000)')
# Значение 2398 повторяется 24 раза, что чаще всего
# 565219 function calls (565184 primitive calls) in 1.194 seconds

cProfile.run('func_v2(10, 100)')
# Значение 10 повторяется 14 раза, что чаще всего
# 2132 function calls (2105 primitive calls) in 0.004 seconds
cProfile.run('func_v2(10000, 100000)')
# Значение 4228 повторяется 25 раза, что чаще всего
# 765595 function calls (765568 primitive calls) in 1.490 seconds

