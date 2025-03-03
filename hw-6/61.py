def binary_search(arr, target):
    # Бинарный поиск в декларативной парадигме

    def search(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return search(mid + 1, high)
        else:
            return search(low, mid - 1)
    return search(0, len(arr) - 1)


# Реализация кода
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
index = binary_search(sorted_array, target)
print(f"индекс элемента {target} => {index}")
