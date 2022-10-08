# Первое задание, в принципе всё равно какие числа, важна логика.

my_list = [1, 41, 2131, 12, 14, 22, 2, 411, 1]
k = []
for i in my_list:
    if i > 100:
        k.append(i)
for i in k:
    print(i)

# Второе задание.

my_list1 = [243, 1, 1, 32, 11, 12, 111, 222, 3]
my_results = []
for i in my_list1:
    if i > 100:
        my_results.append(i)
for i in my_results:
    print(i)

# Третье задание

my_list2 = [1, 12, 3, 123123, 13213, 123]
l = []
if len(my_list2) < 2:
    my_list2.append(0)
elif len(my_list2) >= 2:
    my_list2.append(my_list2[-1] + my_list2[-2])
print(my_list2)

# Четвёртое задание про удаление элемента из списка.

my_list3 = [13, 1141, 1, 1, 'k']
my_list3.pop()
# На самом деле pop() удаляет последний элемент, если в скобках не указан конкретный индекс,
# удаление конкретного элемента осуществляется с помощью .remove(-указание элемента-).
my_list3[3] = 'k'
print(my_list3)
my_list3.remove('k')
print(my_list3)

# Пятое задание. Сгенерируем список со случайными значениями.
from random import randint

my_list4 = [randint(1, 200) for j in range(10)]
print(my_list4)
my_list4.append(2)
my_list4.sort()
print(my_list4)
# Элементов будет 10, индексов 0-9. Это важно будет помнить, дабы перемещать элементы.
# Предположим, что какие-то элементы нужно поменять местами друг с другом.
my_list4[1], my_list4[2] = my_list4[2], my_list4[1]
print(my_list4)

# Шестое задание.

print(len(set(set(input().split())^set(input().split()))))
