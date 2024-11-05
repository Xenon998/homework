def get_matrix(n, m, value):
    matrix = []

    for _ in range(n):
        matrix.append([])

        for _ in range(m):
            matrix[-1].append(value)

    return matrix


result1 = get_matrix(3, 4, 8)
result2 = get_matrix(5, 3, 9)
result3 = get_matrix(2, 4, 7)

print("Результат 1:")
print(result1)
print("Результат 2:")
print(result2)
print("Результат 3:")
print(result3)
