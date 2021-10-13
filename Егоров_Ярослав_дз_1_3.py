for i in range(1, 101):
    num = i
    num %= 10

    if num == 1:
        print(f"{i} процент")
    elif num > 1 and num < 5:
        print(f"{i} процента")
    else:
        print(f"{i} процентов")