def sum_digits(number):
    res = 0
    while number != 0:
        res += number % 10
        number //= 10
    return res

arr = [i ** 3 for i in range(1, 1001)]

res1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, arr))
res2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, arr))

print(res1)
print(res2)
