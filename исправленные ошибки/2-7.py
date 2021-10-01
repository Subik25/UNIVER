def N():
    year=int(input("Введите год -\n"))
    print("ответ:")
    if((year % 4 ==0 and year % 100 != 0 ) or year % 400 == 0):
        return "да"
    else:
        return "Нет"
print(N())