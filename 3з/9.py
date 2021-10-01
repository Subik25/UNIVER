n = int(input("Введите число\n"))
sum = 0
(q, w) = (0, 1)
while q <= n:
    (q, w) = (w, q + w)
    if q <= n:
        sum += q
print("Сумма", sum)
