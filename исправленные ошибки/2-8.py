def N():
    x=int(input("Введите входные данные 1 числа\n"))
    y=int(input("Введите входные данные 2 числа\n"))
    z=int(input("Введите входные данные 3 числа\n"))
    print("ответ:")
    if(x==y==z):
        return 3
    elif(x==y or z==y or x==z):
        return 2
    else:
        return 0
print(N())