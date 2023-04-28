# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n= a1+ (n-1) * d.
# Каждое число вводится с новой строки.
list_ =[]
first = int(input("Введите первый элемент прогрессии "))
step = int(input("введите разность "))
quantity = int(input("введите количество элементов "))
for i in range(quantity):
    list_.append(first+i*step)
print(list_)
# а можно и так
#  for i in range(first, first + quantity*step ,step):
#     list_.append(i)
# print(list_)