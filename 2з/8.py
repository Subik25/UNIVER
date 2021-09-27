q=int(input('Введите число \n'))
w=int(input('Введите число \n'))
e=int(input('Введите число \n'))
if q == w == e:
    print('Совпадений','',3)
elif q == w or w == e or q == e:
    print('Совпадений','',2)
else:
    print('Совпадений','',0)




