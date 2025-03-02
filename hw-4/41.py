from functools import reduce
import math

# Функция mean() для вычисления среднего значения массива
def mean(arr):
    return reduce(lambda x, y: x + y, arr) / len(arr)

# Функция covariance() для вычисления ковариации двух массивов
def covariance(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    return sum(map(lambda xi, yi: (xi - x_mean) * (yi - y_mean), x, y))

# Функция std_deviation() для вычисления стандартного отклонения массива
def std_deviation(arr):
    arr_mean = mean(arr)
    variance = sum(map(lambda xi: (xi - arr_mean) ** 2, arr))
    return math.sqrt(variance)

# Функция вычисления коэффициента корреляции Пирсона
def pearson_correlation(x, y):
    cov = covariance(x, y)
    std_x = std_deviation(x)
    std_y = std_deviation(y)
    correlation = cov / (std_x * std_y)
    print(f"коэффициент корреляции Пирсона : {correlation}")
    return correlation

# Реализация кода
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10, 12]

pearson_correlation_result = pearson_correlation(x, y)
pearson_correlation_result