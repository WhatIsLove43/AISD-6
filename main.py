import itertools
import time


def is_even(n):
    return n % 2 == 0

def get_tree_leaf_indices(K):
    #Возвращает индексы листьев для дерева с K вершинами.
    #Пример: фиксируем, что листья — это последние K//2 вершин.

    return list(range(K // 2, K))

def find_optimal_labeling(K):
    #Находит оптимальную разметку с ограничением: листья — четные числа.
    #Целевая функция: минимизация суммы чисел на листьях.

    if K <= 0:
        print("Количество вершин должно быть положительным числом.")
        return

    vertices = list(range(1, K + 1))
    leaf_indices = get_tree_leaf_indices(K)

    optimal_labeling = None
    min_leaf_sum = float('inf')

    # Перебираем все возможные разметки
    for labeling in itertools.permutations(vertices):
        leaf_values = [labeling[i] for i in leaf_indices]

        # Проверка на четность чисел листьев
        if all(is_even(value) for value in leaf_values):
            leaf_sum = sum(leaf_values)
            if leaf_sum < min_leaf_sum:
                min_leaf_sum = leaf_sum
                optimal_labeling = labeling

    # Выводим оптимальную разметку
    if optimal_labeling:
        print(f"Оптимальная разметка: {optimal_labeling}")
        print(f"Минимальная сумма чисел на листьях: {min_leaf_sum}")
    else:
        print("Не найдено разметок, удовлетворяющих условиям.")

# Ввод количества вершин
K = int(input("Введите количество вершин K: "))
find_optimal_labeling(K)
