def get_sign(x):
    if x[0] in '+-':
        return x[0]

arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
out = []

for elem in arr:
    if elem.isdigit():
        number = int(elem)
        if number < 10:
            str_number = '"' + "0" + str(number) + '"'
        else:
            str_number = '"' + str(number) + '"'
        out.append(str_number)
    elif elem[0] in "+-":
        number = int(elem[1:])
        if number < 10:
            str_number = '"' + elem[0] + "0" + str(number) + '"'
        else:
            str_number = '"' + str(number) + '"'
        out.append(str_number)
    else:
        out.append(elem)

out_string = " ".join(out)
print(out_string)

