import random
import matplotlib.pyplot as plt
import timeit

def bubble_sort(arr):
    n=len(arr)
    for i in range(n): # определяем длину списка
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: # если первый больше второго то меняем их местами
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr # возвращаем отсортированный список

def selected_sort(arr):
    n = len (arr)
    for i in range(n):
        min_index = i # создаем минимальное
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

bubble_times = []
selected_times = []
list_sizes = [10, 100, 500, 1000, 2000] # Размеры списков для тестирования

def bubble_time(arr):
    bubble_sort(arr.copy())  # Сортирую копию, чтобы не изменять исходный список

def selected_time(arr):
    selected_sort(arr.copy())  # Сортирую копию, чтобы не изменять исходный список

for range_list in list_sizes:
    arr = [random.randint(0, 5000) for _ in range(range_list)] # создаю список случайных чисел
    print(arr)
    bubble_time_take = timeit.timeit(stmt = lambda: bubble_time(arr), number=100) # Измеряем время выполнения линейного поиска
    selected_time_take = timeit.timeit(stmt = lambda: selected_time(arr), number=100) # Измеряем время выполнения бинарного поиска

    bubble_times.append(bubble_time_take) # заношу значения в список для графика
    selected_times.append(selected_time_take) # заношу значения в список для графика



# Строю график
plt.plot(list_sizes, bubble_times, label="Пузырьковый метод")
plt.plot(list_sizes, selected_times, label="Сортировка выбором")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.title("Сравнение времени выполнения различных методов сортировки")
plt.legend()
plt.grid(True)
plt.show()