"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
"""
def odd_nums(max_value):
    n=1
    while n <= max_value:
        yield n
        n += 2

odd_to_15 = odd_nums(15)