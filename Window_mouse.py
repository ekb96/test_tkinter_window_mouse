# Тест библиотеки tkinter и взаимодействия с клавиатурой\мышью

from tkinter import *

def b1(event):
    root.title("Левая кнопка")						# Меняем заголовок окна
def b2(event):
    root.title("Колесо")
def b3(event):
    root.title("Правая кнопка")
def b4(event):
    root.title("Двойное левой")
def move(event):
    root.title("Движение")
def ret(event):
    root.title("Enter")
def spc(event):
    root.title("Пробел")
def whl(event):
    root.title("Вращение")
def key(event):
    root.title("Нажата " + event.char)

root = Tk()											# Метод с параметрами окна
root.minsize(width=500, height=400)					# Задаем размеры окна
													# При действии вызываем соответствующую функцию
root.bind('<Button-1>', b1)                         # Левая кнопка
root.bind('<Button-2>', b2)                         # Средняя кнопка
root.bind('<Button-3>', b3)                         # Правая кнопка
root.bind('<Double-Button-1>', b4)                  # Двойное левой
root.bind('<Motion>', move)                         # Движение мыши
root.bind('<Return>', ret)                          # Клавиша Enter
root.bind('<space>', spc)                           # Клавиша Пробел
root.bind('<MouseWheel>', whl)                      # Вращение колеса
root.bind('<Key>', key)                             # Любая клавиша

root.mainloop()										# вызываем окно
