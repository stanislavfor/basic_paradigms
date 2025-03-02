def sort_list_declarative(numbers):
    # Декларативный код здесь
    # Функция sorted() возвращает новый отсортированный список
    return sorted(numbers, reverse=True)

# Реализация кода
numbers = [64, 34, 25, 12, 22, 11, 90, 23]
sorted_numbers = sort_list_declarative(numbers)
print(sorted_numbers)
