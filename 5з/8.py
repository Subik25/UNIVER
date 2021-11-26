#-- coding: utf-8 --
x=-1
y=0
z=0
q=int(input('Введите число:\n'))
while q!=0:
    if x==q:
        y+=1
    else:
        x=q
        z=max(z,y)
        y=1
    q=int(input('Введите число:\n'))
z=max(z,y)
print(z)
