'''Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих 
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
'''
import random
N = int(input("Введите число N - количество элементов в массиве: "))
list_1 = [random.randint(0, N) for x in range(N)]
X = int(input("Введите число X - искомое число в массиве: "))
print(*list_1)
if X in list_1: print(f"Искомое число {X} встречается в массиве {list_1.count(X)} раз(а)")

else:
    print(f"Искомого числа {X} в массиве нет")


