'''Дано дерево из К вершин. Сформировать все возможные варианты разметки данного дерева числами от 1 до К
1 часть: написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования:
алгоритмический и с помощью функций питона, сравнив по времени их выполнение'''

import timeit
import itertools

K = 5
Vertex = list(range(1, K+1))

def recurs(Vertex, PermutList):
    if len(PermutList) == len(Vertex):
        print(PermutList)
        return
    for i in range(len(Vertex)):
        if Vertex[i] not in PermutList:
            recurs(Vertex, PermutList + [Vertex[i]])

def recurs_run():
    recurs(Vertex, [])

def itertools_run():
    IterList = list(itertools.permutations(Vertex))
    for i in IterList:
        print(list(i))

AlgTime = timeit.timeit(recurs_run, number=1)
print(f"Алгоритмический метод: {AlgTime:.4f} секунд")

IterTime = timeit.timeit(itertools_run, number=1)
print(f"Время с использованием функций питона: {IterTime:.4f} секунд")
