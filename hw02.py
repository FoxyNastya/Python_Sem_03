'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5

'''
import random
N = int(input("Введите число N - количество элементов в массиве: "))
A = [random.randint(0, N) for x in range(N)]
print(*A)
X = int(input("Введите число X: "))

if X in A: 
    print(X)
    exit
else:
    for i in range(len(A)):
        if A[i] - 1 == X or A[i] + 1 == X:
            print(A[i])
            i += 1
        