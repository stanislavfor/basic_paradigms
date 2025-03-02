def sort_list_imperative(numbers):
    n = len(numbers)
    # Императивный код здесь
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                #  Алгоритм для сортировки пузырьком
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# Реализация кода
numbers = [64, 34, 25, 12, 22, 11, 90, 23]
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers)
