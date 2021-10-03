a = int(input("Введите число:\n"))
if a == 0:
    print(0)
else:
    q,w = 0, 1
    n = 1
    while w <= a:
        if w == a:
            print(n)
            break
        q, w = w, q + w
        n += 1
    else:
        print("Цифра  не является числом Фибоначчи")
