import numpy as np

n, m = 3, 4
matrix_A = np.random.randint(-10, 10, size=(n, m))

print("Исходная матрица:")
print(matrix_A)

max_abs_element = np.max(np.abs(matrix_A))
matrix_B = matrix_A / max_abs_element

print("\nНовая матрица после деления на максимальный по модулю элемент:")
print(matrix_B)

# Вычисление дисперсии элементов новой матрицы
variance_np = np.var(matrix_B)
variance_custom = np.mean((matrix_B - np.mean(matrix_B))**2)

print("\nДисперсия элементов новой матрицы (через NumPy):", round(variance_np, 2))
print("Дисперсия элементов новой матрицы (программное вычисление):", round(variance_custom, 2))
