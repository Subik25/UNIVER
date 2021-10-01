def N():
    n=int(input("Введите входные данные 1 числа\n"))
    m=int(input("Введите входные данные 2 числа\n"))
    k=int(input("Введите входные данные 3 числа\n"))
    print("ответ:")
    if(n*m >k and (k %m ==0 or k%n==0)):
        return "да"
    else:
        return "нет"
print(N())