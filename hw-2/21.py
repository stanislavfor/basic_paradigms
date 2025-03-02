def print_structured(n):
    print("structured")
    for i in range(1, n + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print()

# Реализация кода
print_structured(2)


def multiply(a, b):
    return a * b

def print_procedural(n):
    print("procedural")
    def print_row(i):
        for j in range(1, 10):
            print(f"{i} * {j} = {multiply(i, j)}")
        print()

    for i in range(1, n + 1):
        print_row(i)

# Реализация кода
print_procedural(2)

def print_imperative(n):
    i = 1
    print("imperative")
    while i <= n:
        j = 1
        while j < 10:
            result = i * j
            print(f"{i} * {j} = {result}")
            j += 1
        print()
        i += 1

# Реализация кода
print_imperative(2)

