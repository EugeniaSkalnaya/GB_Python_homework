# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import randint
N = int(input('Введите размер списка: '))
x = int(input("Введите искомое число от 1 до 10 - ")) #так, чтобы наверняка попало нужное число
count = 0
list = []
for i in range(N):
    list.append(randint(0, 10))
print(list)
for i in range(len(list)):
    if list[i] == x: count +=1
print(f"Число {x} встречается в списке {count} раз")