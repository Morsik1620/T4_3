import random


def bubble_sort(arr):
    n=len(arr)
    for i in range(n): # определяем длину списка
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: # если первый больше второго то меняем их местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr # возвращаем отсортированный список

arr = []
arr = [random.randint(0, 50) for _ in range(10)] # создаю список случайных чисел
print("Список случайных чисел:", arr)
print ("Отсортированный список:", bubble_sort(arr))

