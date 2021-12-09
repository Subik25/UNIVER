# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
import random
def yes():
    messagebox.showinfo(' ', 'Спасибо! Ваш отзыв учтен!')
    quit()

def no(event):
    btnNo.place(x=random.randint(100 , 500), y=random.randint(100 , 500))



def d1():
    arg = txt.get()
    i = 1
    N = int(arg)
    result = ""
    while i * i <= N:
        i+=1
        result += str(i)
    resultlbl_2.configure(text = result)

def d2():
    arg = txt1.get()
    i = 2
    N = int(arg)
    while N % i != 0:
        i += 1
    resultlbl1_2.configure(text = i)

def d3():
    arg = txt2.get()
    i = 2
    powContainer = 2
    counter = 1
    N = int(arg)

    while powContainer * i < N:
        powContainer *= i
        counter+=1
    result = "Cтепень: "  + str(powContainer) + " " + "Показатель степени: " + str(counter) 
    resultlbl2_2.configure(text = result)

def d4():
    x = int(txt3_1.get())
    y = int(txt3_2.get())
    counter = 1
    while x < y:
        x *= 1.1
        counter+=1
    resultlbl3_2.configure(text = counter)

until0Counter1 = 0
def d5():
    global until0Counter1
    arg = txt4.get()
    print(arg)
    if(arg != "0"):
        until0Counter1 += 1
        print(until0Counter1)
    else:
        resultlbl4_2.configure(text = until0Counter1)
        until0Counter1 = 0
    txt4.delete(0, END)

until0Counter2 = 0
sum = 0
def d6():
    global until0Counter2
    arg = txt5.get()
    global sum
    if arg != "0":
        until0Counter2+=1
        sum += int(arg)
    else:
        resultlbl5_2.configure(text = sum / until0Counter2)
        until0Counter2 = 0
        sum = 0
    txt5.delete(0, END)

until0Counter3 = 0
container = 10000000
def d7():
    arg = txt6.get()
    global until0Counter3
    global container
    if(int(arg) > container):
        until0Counter3+=1
    container = int(arg)
    if(arg == "0"):
        resultlbl6_2.configure(text = until0Counter3)
        container = 100000
        until0Counter3 = 0
    txt6.delete(0, END)

until0Counter4 = 0
maxStreak = 0
def d8():
    arg = txt7.get()
    global until0Counter4
    global container
    global maxStreak

    x = int(arg)
    if(x == container):
            until0Counter4 += 1
    else:
        if(maxStreak < until0Counter4):
            maxStreak = until0Counter4
        until0Counter4 = 1
    container = x
    if(x == 0):
        resultlbl7_2.configure(text = (max(maxStreak, until0Counter4)))
        container = 1000000
    txt7.delete(0, END)


window = Tk()
window.title("Интерфейс для 5 практики")
window.geometry('1290x570')
window.resizable(False, False)
lbl = Label(window, text = "Введите данные для 1 программы :", font=("Segoe script", 10))
lbl.grid(column=0, row = 0)
txt = Entry(window, width = 15 )
txt.grid(column=1, row = 0)
btn = Button(window, text = "Выполнить программу №5(1)", font=("Impact", 10),command = d1)
btn.grid(column=2, row = 0)
resultlbl_1 = Label(window, text = "Результат программы: ", font=("Segoe script", 10))
resultlbl_1.grid(column = 3, row = 0)
resultlbl_2 = Label(window, text = "")
resultlbl_2.grid(column=4, row = 0)

lbl1 = Label(window, text = "Введите данные для 2 программы :", font=("Segoe script", 10))
lbl1.grid(column=0, row = 1)
txt1 = Entry(window, width = 15)
txt1.grid(column=1, row = 1)
btn1 = Button(window, text = "Выполнить программу №5(2)", font=("Impact", 10),command = d2)
btn1.grid(column=2, row = 1)
resultlbl1_1 = Label(window, text = "Результат программы: ", font=("Segoe script", 10))
resultlbl1_1.grid(column = 3, row = 1)
resultlbl1_2 = Label(window, text = "")
resultlbl1_2.grid(column=4, row = 1)

lbl2 = Label(window, text = "Введите данные для 3 программы :", font=("Segoe script", 10))
lbl2.grid(column=0, row = 2)
txt2 = Entry(window, width = 15)
txt2.grid(column=1, row = 2)
btn2 = Button(window, text = "Выполнить программу №5(3)", font=("Impact", 10),command = d3)
btn2.grid(column=2, row = 2)
resultlbl2_1 = Label(window, text = "Результат программы: ", font=("Segoe script", 10))
resultlbl2_1.grid(column = 3, row = 2)
resultlbl2_2 = Label(window, text = "")
resultlbl2_2.grid(column=4, row = 2)

lbl3 = Label(window, text = "Введите данные для 4 программы: 1 число : \n 2 число:", font=("Segoe script", 10))
lbl3.grid(column=0, row = 3, rowspan=2)
txt3_1 = Entry(window, width = 15)
txt3_1.grid(column=1, row = 3)
txt3_2 = Entry(window, width = 15)
txt3_2.grid(column=1, row = 4)
btn3 = Button(window, text ="Выполнить программу №5(4)", font=("Impact", 10), command=d4, height = 3, width = 27)
btn3.grid(column=2, row = 3,rowspan=2)
resultlbl3_1 = Label(window, text = "Результат программы: ", font=("Segoe script", 10))
resultlbl3_1.grid(column = 3, row = 3,rowspan=2)
resultlbl3_2 = Label(window, text = "")
resultlbl3_2.grid(column=5, row = 3,rowspan=2)

lbl4_1 = Label(window, text = "Введите данные для 5 программы : \n(0 выведет результат) ", font=("Segoe script", 10))
lbl4_1.grid(column=0, row = 5)
txt4 = Entry(window, width = 15)
txt4.grid(column=1, row = 5)
btn4 = Button(window, text = "Выполнить программу №5(5)", font=("Impact", 10), command=d5)
btn4.grid(column=2, row = 5)
resultlbl4_1 = Label(window, text = "Результат программы: ", font=("Segoe script", 10))
resultlbl4_1.grid(column = 3, row = 5)
resultlbl4_2 = Label(window, text = "")
resultlbl4_2.grid(column=4, row = 5)


lbl5 = Label(window, text = "Введите данные для 6 программы : \n(0 выведет результат)", font=("Segoe script", 10))
lbl5.grid(column=0, row = 6)
txt5 = Entry(window, width = 15)
txt5.grid(column=1, row = 6)
btn5 = Button(window, text = "Выполнить программу №5(6)",font=("Impact", 10), command=d6)
btn5.grid(column=2, row = 6)
resultlbl5_1 = Label(window, text = "Результат программы: ", font=("Segoe script", 10))
resultlbl5_1.grid(column = 3, row = 6)
resultlbl5_2 = Label(window, text = "")
resultlbl5_2.grid(column=4, row = 6)


lbl6 = Label(window, text = "Введите данные для 7 программы : \n(0 выведет результат)", font=("Segoe script", 10))
lbl6.grid(column=0, row = 7)
txt6 = Entry(window, width = 15)
txt6.grid(column=1, row = 7)
btn6 = Button(window, text = "Выполнить программу №5(7)", font=("Impact", 10),command=d7)
btn6.grid(column=2, row = 7)
resultlbl6_1 = Label(window, text = "Результат программы: ", font=("Segoe script", 10))
resultlbl6_1.grid(column = 3, row = 7)
resultlbl6_2 = Label(window, text = "")
resultlbl6_2.grid(column=4, row = 7)

lbl7 = Label(window, text = "Введите данные для 8 программы : \n(0 выведет результат)", font=("Segoe script", 10))
lbl7.grid(column=0, row = 8)
txt7 = Entry(window, width = 15)
txt7.grid(column=1, row = 8)
btn7 = Button(window, text = "Выполнить программу №5(8)",font=("Impact", 10),command=d8)
btn7.grid(column=2, row = 8)
resultlbl7_1 = Label(window, text = "Результат программы: ", font=("Segoe script", 10))
resultlbl7_1.grid(column = 3, row = 8)
resultlbl7_2 = Label(window, text = "")
resultlbl7_2.grid(column=4, row = 8)

lbl8=Label(window , text="Вам понравилась моя программа?", font=("Impact", 10))
lbl8.grid(column=0, row = 9)
btnNo= Button (window, text="Нет", font="Arial 10 bold")
btnNo.grid(column=1, row = 9)
btnNo.bind("<Enter>", no)
btnYes= Button(window, text="Да", command=yes,font="Arial 10 bold")
btnYes.grid(column=2, row = 9)


window.mainloop()