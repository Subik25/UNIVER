q=int(input('Введите номер года\n'))
if (q % 4 == 0) and (q % 100 != 0) or (q % 400 == 0):
    print('Да')
else:
    print('Нет')
