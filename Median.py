from random import randint
import copy


def main():
    n = int(input("Введите количество элементов в массиве: "))

    # заполняем случайными значениями
    arr = []
    for i in range(n):
        arr.append(randint(0, 1000))

    # создаем копию массива
    arr_test = copy.copy(arr)

    # выводим на экран исходный массив
    for elem in arr:
        print(elem, end=" ")
    print()

    # номер середины отсортированного массива (медианы)
    median_index = len(arr) // 2

    # получаем результат
    result = find_sorted(arr, median_index)
    print(f"Медиана: {result}")

    # проверяем результат на отсортированном массиве
    arr_test.sort()
    print(f"Проверка:")
    for i, elem in enumerate(arr_test):
        if i == median_index:
            print(f"\033[46m{elem}\033[47m", end=" ")
        else:
            print(f"\033[47m{elem}", end=" ")


def find_sorted(array, k):
    """
    Алгоритм выбора
    :param array: массив (будет изменен!)
    :param k: номер по величине элемента в массиве
    :return: значение номера по величине элемента в массиве
    """
    # определяем границы области
    left = 0
    right = len(array) - 1

    # пока область не пуста
    while left < right:
        # опорное значение
        pivot = array[k]

        i = left
        j = right

        while i <= j:
            # ищем индекс значения больше опорного от левого края
            while array[i] < pivot:
                i += 1
            # ищем индекс значения меньше опорного от правого края
            while array[j] > pivot:
                j -= 1
            if i <= j:
                # меняем местами эти значения
                array[i], array[j] = array[j], array[i]
                # продолжаем просмотр
                i += 1
                j -= 1

        # если опорный элемент правее разбиения
        if j < k:
            left = i
        # если опорный элемент левее разбиения
        if i > k:
            right = j
    return array[k]


if __name__ == "__main__":
    main()
