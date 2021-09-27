x = {'иван','Иван','ivan','Ivan'}
user_name=''
while len(user_name.strip())<1:
 user_name=input('What is your name?\n')
print('It was nice to meet you,' + user_name + '!')
age=int(input('How old are you?\n'))
if user_name in x:
  print('Извините но вы нам не подходите')
else: 
  if age>=16 and 0<age<75: 
    print('Поздравляем вы поступили в ВГУИТ!!!')
  else:
    print('Сначало нужно закончить школу')
    s=18-age
    print('Осталось',s,'лет')