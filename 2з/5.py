q = int(input('Введите число\n'))
w = int(input('Введите число\n'))
e = int(input('Введите число\n'))
if w >= q <= e:
    print('Наименьшее число','',q)
elif q >= w <= e:
    print('Наименьшее число','',w)
else:
    print('Наименьшее число','',e)