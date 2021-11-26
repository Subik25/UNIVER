# -- coding: utf-8 --
q = int(input('Введите число:\n'))
w = 2
while q % w != 0:
    w += 1
print(w)
