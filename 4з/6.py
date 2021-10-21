x = input("Введите строку\n")
if x.count('f') == 1:
    print(-1)
elif x.count('f') < 1:
    print(-2)
else:
    print(x.find('f', x.find('f') + 1))
