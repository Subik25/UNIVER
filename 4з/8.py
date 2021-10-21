x = input("Введите строку, в которой буква h встречается как минимум два раза\n")
q = x[:x.find('h')] 
w = x[x.find('h'):x.rfind('h') + 1]
e = x[x.rfind('h') + 1:]
x = q + w[::-1] + e
print(x)
