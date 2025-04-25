import random

def selected_sort(arr):
    n = len (arr)
    for i in range(n):
        min_index = i # создаем минимальное
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = []
arr = [random.randint(0, 50) for _ in range(10)] # создаю список случайных чисел
print("Список случайных чисел:", arr)
print ("Отсортированный список:", selected_sort(arr))