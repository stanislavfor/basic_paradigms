def binary_search(arr, target):
    # Бинарный поиск в императивной парадигме

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Реализация кода
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
index = binary_search(sorted_array, target)
print(f"индекс элемента {target} => {index}")
