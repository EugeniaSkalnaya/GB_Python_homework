# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10в5
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает). 300 220 284

def divider_sum(x):
    sum_ = 0
    for i in range(1, x):
        if x % i == 0:
            sum_ += i
    return sum_

N = int(input("Введите число меньше 10 в 5 степени "))

result = []
for i in range(1, N):
    if i not in result:
        temp = divider_sum(i)
        if divider_sum(temp) == i and i != temp:
            result.append(i)
            result.append(temp)
for k in range(0, len(result)-1, 2):
    print(result[k], result[k+1])