# -- coding: utf-8 --
x=int(input('Введите число:\n'))
y=0
while x!=0:
    z=int(input('Введите число:\n'))
    if (z!=0) and(x<z):
        y+=1
    x=z
print(y)
