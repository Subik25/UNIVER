# -- coding: utf-8 --
N=int(input('Введите число:\n'))
z=1
x=0
while z <= N:
    z*=2
    x+=1
    if z<=N:
        print(z,x)
