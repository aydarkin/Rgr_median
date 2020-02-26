from random import randint
import copy


def main():
    number = input("Введите количество элементов в массиве: ")

    # заполняем случайными значениями
    arr = []
    for i in range(int(number)):
        arr.append(randint(0, 1000))

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
    arr.sort()
    print(f"Проверка:")
    for i, elem in enumerate(arr):
        if i == median_index:
            print(f"\033[46m{elem}\033[40m", end=" ")
        else:
            print(f"\033[40m{elem}", end=" ")


def find_sorted(arr, index):
    # создаем копию массива
    array = copy.copy(arr)

    # определяем границы области
    left = 0
    right = len(array) - 1

    # пока область не пуста
    while left < right:
        # опорное значение
        pivot = array[index]

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
        if j < index:
            left = i
        # если опорный элемент левее разбиения
        if i > index:
            right = j
    return array[index]


if __name__ == "__main__":
    main()
