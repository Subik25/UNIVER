a = int(input("Введите первое число\n"))
b = int(input("Введите первое число\n"))
if a<b:
  for i in range(a, b + 1):
      print(i)
else:
  for i in range(a,b-1,-1):
      print(i)
 
