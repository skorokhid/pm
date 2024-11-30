

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
def task1():
    # Оголошуємо змінні
    x = sp.Symbol('x')
    y = sp.Function('y')

    # Оголошуємо диференціальне рівняння
    diff_eq = sp.Eq(y(x).diff(x, x) - 2*y(x).diff(x) + y(x), sp.exp(x))

    # Розв'язуємо диференціальне рівняння
    solution = sp.dsolve(diff_eq, y(x))

    # Виводимо розв'язок
    print(solution)

def task2():

    # Оголошуємо змінні
    x = sp.Symbol('x')
    y = sp.Function('y')

    # Диференціальне рівняння
    diff_eq = sp.Eq(y(x).diff(x, x) - 3*y(x).diff(x) + 2*y(x), sp.exp(2*x))

    # Функція для знаходження загального розв'язку
    def general_solution():
        solution = sp.dsolve(diff_eq, y(x))
        sp.pprint(solution, use_unicode=True)

    # Функція для знаходження часткового розв'язку
    def particular_solution():
        initial_conditions = {y(0): 1, y(x).diff(x).subs(x, 0): 0}
        solution = sp.dsolve(diff_eq, y(x), ics=initial_conditions)
        sp.pprint(solution, use_unicode=True)
        return solution

    # Функція для побудови графіка часткового розв'язку
    def plot_solution():
        solution = particular_solution()
        f = sp.lambdify(x, solution.rhs, "numpy")
        x_values = np.linspace(0, 5, 100)
        y_values = f(x_values)

        plt.plot(x_values, y_values, label="Частковий розв'язок")
        plt.title("Частковий розв'язок для $y'' - 3y' + 2y = e^{2x}$")
        plt.xlabel('x')
        plt.ylabel('y(x)')
        plt.grid(True)
        plt.legend()
        plt.show()

    # Вибір підзавдання
    def solve_task():
        while True:
            print("\nВиберіть підзавдання:")
            print("a: Знайти загальний розв'язок")
            print("b: Знайти частковий розв'язок")
            print("c: Побудувати графік часткового розв'язку")
            print("q: Вийти з програми")
            task = input("Введіть ваш вибір (a, b, c, q): ").lower()

            if task == 'a':
                general_solution()
            elif task == 'b':
                particular_solution()
            elif task == 'c':
                plot_solution()
            elif task == 'q':
                print("Вихід з програми.")
                break
            else:
                print("Неправильний вибір. Спробуйте знову.")

    solve_task()


def task3():
    
    # Оголошуємо змінні
    t = sp.Symbol('t')
    x = sp.Function('x')(t)
    y = sp.Function('y')(t)
    
    # Задаємо систему диференціальних рівнянь
    eq1 = sp.Eq(x.diff(t), x - y - t - 2)
    eq2 = sp.Eq(y.diff(t), 2*x + 3*y + 2*t)
    
    # Символьне розв'язання системи
    solution = sp.dsolve([eq1, eq2])
    
    # Виводимо загальний розв'язок
    sp.pprint(solution, use_unicode=True)
    
def menu():
    while True:
        print("\nОберіть задачу для виконання:")
        print("Завдання 1")
        print("Завдання 2")
        print("Завдання 3")
       
        
        print("4. Вийти")
        
        choice = input("Введіть номер задачі (1-5): ")

        match choice:
            case '1':
                task1()
            case '2':
                task2()
            case '3':
                task3()
            case '4':
                print("Вихід з програми.")
                break
            case None:
                print("Невірний вибір. Спробуйте ще раз.")

menu()

