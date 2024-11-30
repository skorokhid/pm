import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Матан
def task_2_4_21_a():
    # Оголошуємо змінну x
    x = sp.symbols('x')

    # Функція, границю якої потрібно знайти
    numerator = 3 * sp.tan(x) - 2 * x**2 + x**4
    denominator = sp.asin(6 * x)

    # Обчислюємо границю при x -> 0
    limit_result = sp.limit(numerator / denominator, x, 0)
    
    print(limit_result)
    print('\n')
def task_2_4_21_b():
    # Оголошуємо змінну x
    x = sp.symbols('x')

    # Чисельник та знаменник
    numerator = 2**(sp.cos(x)**2) - 1
    denominator = sp.ln(sp.sin(x))

    # Обчислюємо границю при x -> π/2
    limit_result = sp.limit(numerator / denominator, x, sp.pi / 2)

    sp.pprint(limit_result)
    print('\n')
def task_4_3_21():
    # Оголошуємо змінну t
    t = sp.symbols('t')

    # Параметричні рівняння
    y = sp.asin(t - 1)
    x = sp.sqrt(2*t - t**2)

    # Знаходимо похідні
    dy_dt = sp.diff(y, t)
    dx_dt = sp.diff(x, t)

    # Обчислюємо похідну dy/dx
    dydx1 = dy_dt / dx_dt

    # Знаходимо другу похідну d^2y/dx^2
    d2ydx2 = sp.diff(dydx1, t) / dx_dt

    print(dydx1.simplify())    
    print('\n')
    print(d2ydx2.simplify())    
    print('\n')
def task_2_1_21():
    # Оголошуємо змінну
    x = sp.symbols('x')

    # Записуємо многочлен
    P = x**3 + 3*x**2 - 2*x - 8

    # Розкладаємо многочлен на множники
    factors = sp.factor(P)

    # Виводимо результат
    print(factors)
    print('\n')
def task_3_1_21_matan():

    # Оголошуємо змінну
    x = sp.symbols('x')

    # Підінтегральний вираз
    expr = 1 / (x**2 - 6*x + 11)

    # Виділення повного квадрата
    # Вираз у знаменнику x^2 - 6x + 11 = (x - 3)^2 + 2
    complete_square = (x - 3)**2 + 2

    # Змінимо вираз, щоб використовувати повний квадрат
    integral_expr = 1 / complete_square

    # Інтегруємо
    integral = sp.integrate(integral_expr, x)

    # Виводимо результат
    print(integral.simplify())
    print('\n')
def task_3_2_21():

    # Оголошуємо змінні
    x, y, z = sp.symbols('x y z')

    # Визначаємо функцію u
    u = x**2 + x*y + y*z + x*z

    # Обчислюємо градієнт функції u
    grad_u = [sp.diff(u, var) for var in (x, y, z)]

    # Задаємо вектор a
    a = [5, 3, 2]

    # Вирішуємо систему рівнянь grad(u) = a
    equations = [sp.Eq(grad_u[i], a[i]) for i in range(3)]

    # Вирішуємо систему рівнянь
    solutions = sp.solve(equations, (x, y, z))

    # Виводимо розв'язки
    sp.pprint(solutions)
    print('\n')
def task_3_3_21():
    # Оголошуємо змінні
    x, y = sp.symbols('x y')

    # Визначаємо функцію z
    z = 2 * sp.atan(x) + 2 * sp.atan(y) - sp.log((x**2 + 1) * (y**2 + 1))

    # Обчислюємо часткові похідні
    dz_dx = sp.diff(z, x)
    dz_dy = sp.diff(z, y)

    # Задаємо систему рівнянь
    equations = [sp.Eq(dz_dx, 0), sp.Eq(dz_dy, 0)]

    # Вирішуємо систему рівнянь
    critical_points = sp.solve(equations, (x, y))

    # Виводимо критичні точки
    sp.pprint(critical_points)
    print('\n')
# Комплексні змінні
def task_1_3_21():
    # Задане число
    number = 4096

    # Знаходимо шостий корінь
    root = number ** (1/6)

    # Знаходимо всі шості корені
    n = 6
    angles = [(2 * np.pi * k) / n for k in range(n)]
    roots = [root * (np.cos(angle) + 1j * np.sin(angle)) for angle in angles]

    # Виводимо результати
    for k, z in enumerate(roots):
        print(f"z_{k} = {z}")
# Графічні можливості SymPy
def task_1_1_21():
    # Задаємо змінну n
    n = sp.symbols('n')

    # Визначаємо загальний член ряду
    S_n = 1 / (40 * 2 * n + 3 * 41 * (40 * 2 * n + 5 * 41))

    # Обчислюємо суму ряду
    S = sp.Sum(S_n, (n, 1, sp.oo)).doit()

    # Виводимо результат
    print(S)
def task_3_1_21_graph():

    # Визначаємо функцію f(x)
    def f(x):
        if -np.pi <= x < 0:
            return 0
        elif 0 <= x <= np.pi:
            return (np.pi / 4) - x
        else:
            return 0

    # Визначаємо періодичну функцію
    def f_periodic(x):
        return f(x % (2 * np.pi))

    # Обчислення коефіцієнтів Фур'є
    def a0():
        integral = (1/(2 * np.pi)) * (0 + np.trapz([(np.pi / 4) - x for x in np.linspace(0, np.pi, 1000)], np.linspace(0, np.pi, 1000)))
        return integral

    def an(n):
        integral = (1/np.pi) * np.trapz([(f_periodic(x) * np.cos(n * x)) for x in np.linspace(-np.pi, np.pi, 1000)], np.linspace(-np.pi, np.pi, 1000))
        return integral

    def bn(n):
        integral = (1/np.pi) * np.trapz([(f_periodic(x) * np.sin(n * x)) for x in np.linspace(-np.pi, np.pi, 1000)], np.linspace(-np.pi, np.pi, 1000))
        return integral

    # Коефіцієнти Фур'є
    a0_value = a0()
    n_terms = 10  # Кількість членів ряду Фур'є
    x_values = np.linspace(-np.pi, np.pi, 1000)
    fourier_sum = a0_value

    for n in range(1, n_terms + 1):
        fourier_sum += an(n) * np.cos(n * x_values) + bn(n) * np.sin(n * x_values)

    # Графік
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, [f_periodic(x) for x in x_values], label='f(x)', color='blue')
    plt.plot(x_values, fourier_sum, label='Fourier Series', color='red', linestyle='--')
    plt.title('Fourier Series Approximation')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.legend()
    plt.grid()
    plt.show()
def task_6_3_21():

    # Створюємо x-значення, уникнувши точки x = 1, де буде розрив функції
    x_values = np.linspace(-10, 10, 1000)
    x_values = x_values[x_values != 1]

    # Обчислюємо y-значення
    y_values = (x_values**2 - 4) / (x_values - 1)

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label=r'$y = \frac{x^2 - 4}{x - 1}$', color='red')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)

    # Додаємо назви та легенду
    plt.title('Графік функції $y = \\frac{x^2 - 4}{x - 1}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()
def task_3curve():
    # Створюємо значення для параметра t
    t_values = np.linspace(0, 2 * np.pi, 1000)

    # Обчислюємо значення x і y
    x_values = np.sin(2 * t_values)
    y_values = 2 * (np.sin(t_values) ** 2)

    # Побудова графіка
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=r'$x = \sin(2t), y = 2\sin^2(t)$', color='blue')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)

    # Додаємо назви та легенду
    plt.title('Параметричний графік')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()
def task_3_32_21():
    # Створюємо сітку значень для x та y
    x_values = np.linspace(-10, 10, 1000)
    y_values = np.linspace(-10, 10, 1000)
    X, Y = np.meshgrid(x_values, y_values)

    # Перша крива: 9x^2 - 4y^2 - 36 = 0 (Гіпербола)
    Z1 = 9 * X**2 - 4 * Y**2 - 36

    # Друга крива: x - 2 = -5/7 sqrt(49 + y^2)
    Z2 = X - 2 + (5 / 7) * np.sqrt(49 + Y**2)

    # Побудова графіка
    plt.figure(figsize=(8, 8))

    # Графік першої кривої (Гіпербола)
    plt.contour(X, Y, Z1, levels=[0], colors='blue')
    plt.text(6, 5, r'$9x^2 - 4y^2 - 36 = 0$', color='blue', fontsize=12)

    # Графік другої кривої (Еліпс)
    plt.contour(X, Y, Z2, levels=[0], colors='red')
    plt.text(-8, -8, r'$x - 2 = -\frac{5}{7}\sqrt{49 + y^2}$', color='red', fontsize=12)

    # Додаємо легенду, вісь і сітку
    plt.title('Криві, задані неявно')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
def task_surface():
    # Створюємо сітку значень для x та y
    x_values = np.linspace(-5, 5, 400)
    y_values = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x_values, y_values)

    # Обчислюємо z за допомогою рівняння 4x^2 + y^2 - 4z^2 - 16x - 2y + 21 = 0
    # Рівняння для z: 4z^2 = 4x^2 + y^2 - 16x - 2y + 21
    Z = np.sqrt((4*X**2 + Y**2 - 16*X - 2*Y + 21) / 4)

    # Побудова графіка
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Малюємо дві частини поверхні (z і -z)
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.plot_surface(X, Y, -Z, cmap='viridis', alpha=0.7)

    # Налаштування осей
    ax.set_title("Поверхня: $4x^2 + y^2 - 4z^2 - 16x - 2y + 21 = 0$")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
def menu():
    while True:
        print("\nОберіть задачу для виконання:")
        print("1 - Початок мат аналізу")
        print("2 - Комплексні змінні")
        print("3 - Графіка завдяки NumPy")
        print("4 - Вийти")
        
        choice = input("Введіть номер задачі (1-4): ")

        match choice:
            case '1':
                print("1 - Завдання 2.4.21a")
                task_2_4_21_a()
                print("1 - Завдання 2.4.21b")
                task_2_4_21_b()
                print("1 - Завдання 4.3.21")
                task_4_3_21()
                print("1 - Завдання 2.1.21")
                task_2_1_21()
                print("1 - Завдання 3.1.21 (матаналіз)")
                task_3_1_21_matan()
                print("1 - Завдання 3.2.21")
                task_3_2_21()
                print("1 - Завдання 3.3.21")
                task_3_3_21()
            case '2':
                print("2 - Завдання 1.3.21")
                task_1_3_21()
            case '3':
                print("3 - Завдання 3.1.21 (графіка)")
                task_3_1_21_graph()
                print("3 - Завдання 1.1.21")
                task_1_1_21()
                print("3 - Завдання 6.3.21")
                task_6_3_21()
                print("3 - Завдання 3curve")
                task_3curve()
                print("3 - Завдання 3.32.21")
                task_3_32_21()
                print("3 - Завдання surface")
                task_surface()
            case '4':
                print("Вихід з програми.")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")

menu()
