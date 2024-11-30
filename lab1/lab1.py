import numpy as np

def task_a():
    a = np.array([[1, -5], [6, 2]])
    print("Matrix a:")
    print(a,'\t')
    func = np.dot(a, a)
    print("Square Matrix:")
    print(func,'\t')
    func1 = np.dot(func, a)
    print("func1:")
    print(func1,'\t')
    result = func1 * 3 + 4 * func - 2 * np.eye(a.shape[0])
    print("Result:")
    print(result)

def solve_system():
    A = np.array([[2, 3, 1], [3, 7, 2], [5, 4, 2]])
    B = np.array([10, 3, 3])
    X = np.linalg.solve(A.T, B)    
    print("Розв'язок X:", X)

def matrix_rank():
    A = np.array([[2, 2, 2, 2, 8],
                  [2, -1, 2, -1, 2],
                  [-3, 1, -2, 2, -2],
                  [1, 2, 2, 3, 8]])
    rank = np.linalg.matrix_rank(A)
    print("Ранг матриці A:", rank)

def matrix_method():
    A = np.array([[3, 1, -2], [1, 2, 3], [2, 3, 1]])
    B = np.array([-2, 7, 1])
    X = np.linalg.solve(A, B)
    print("Розв'язок системи (матричний метод):", X)

def cramer_method():
    A = np.array([[3, 1, -2], [1, 2, 3], [2, 3, 1]])
    B = np.array([-2, 7, 1])
    det_A = np.linalg.det(A)
    if det_A != 0:
        A1 = A.copy()
        A2 = A.copy()
        A3 = A.copy()
        A1[:, 0] = B
        A2[:, 1] = B
        A3[:, 2] = B
        det_A1 = np.linalg.det(A1)
        det_A2 = np.linalg.det(A2)
        det_A3 = np.linalg.det(A3)
        x1 = round(float(det_A1 / det_A), 2)
        x2 = round(float(det_A2 / det_A), 2)
        x3 = round(float(det_A3 / det_A), 2)
        

        print("Розв'язок системи (метод Крамера):", [x1, x2, x3])
    else:
        print("Система не має єдиного розв'язку, визначник матриці дорівнює 0.")


def vector_expression():
    magnitude_a = 3 * np.sqrt(3)
    magnitude_b = 1
    theta = np.pi / 6
    
    a = np.array([magnitude_a, 0, 0]) 
    b = np.array([magnitude_b * np.cos(theta), magnitude_b * np.sin(theta), 0])  
    
    expression1 = 2 * np.dot(a, a) - 5 * np.dot(a, b) + 3 * np.dot(b, b)
    print("Результат для виразу (2a - 3b)(a - b):", expression1)

    magnitude_result = np.sqrt((2 * magnitude_a)**2 + magnitude_b**2 - 2 * 2 * magnitude_a * magnitude_b * np.cos(theta))
    print("Результат для виразу |2a - b|:", magnitude_result)


def solve_vector_system():
    A = np.array([[5, 1, -2],
                  [2, 1, 0],
                  [1, -2, 5]])
    B = np.array([1, 3, -1])
    X = np.linalg.solve(A, B)
    print("Вектор X:", X)

def pyramid_volume():
        A = np.array([1, -5, -3])
        B = np.array([1, 3, 0])
        C = np.array([-1, 3, -4])
        D = np.array([3, -3, 2])    
        AB = B - A
        AC = C - A
        cross_product = np.cross(AB, AC)
        area_ABC = 0.5 * np.linalg.norm(cross_product)
        normal = cross_product / np.linalg.norm(cross_product)
        distance_D_to_plane = np.abs(np.dot(D - A, normal))
        volume_pyramid = (1 / 3) * area_ABC * distance_D_to_plane
        print("Площа грані ABC:", area_ABC)
        print("Об'єм піраміди ABCD:", volume_pyramid)

# Виклик функцій
task_a()
solve_system()
matrix_rank()
matrix_method()
cramer_method()
vector_expression()
solve_vector_system()
pyramid_volume()
