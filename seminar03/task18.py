# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint
N = int(input('Введите размер списка: '))
X = int(input("Введите число для сравнения - "))
list = []
for i in range(N):
    list.append(randint(0, 20))
print(list)
min = abs(X - list[0])
index = 0
for i in range(1, N):
    count = abs(X-list[i])
    if count <= min: 
        min = count 
        index = i
print(list[index])