x = input("Введите строку\n")
if x.count('f') == 1:
    print(x.find('f'))
elif x.count('f') >= 2:
    print(x.find('f'), x.rfind('f'))
