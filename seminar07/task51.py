# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

values = [0, 3, 12, 21]
def same_by(func, collection):
    return sum(filter(func, collection)) == 0
if same_by(lambda x: x % 3, values):
    print('same')
else:
    print('different')
