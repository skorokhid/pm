import numpy as np
import matplotlib.pyplot as plt

def task_8_1_21():
    # Визначаємо функцію
    def f(x):
        return x * np.sqrt(4 - x**2)

    # Визначаємо межі
    x_values = np.linspace(0, 2, 100)
    y_values = f(x_values)

    # Побудова графіків
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='$y = x \sqrt{4 - x^2}$', color='blue')

    # Заливка області
    plt.fill_between(x_values, y_values, color='lightblue', alpha=0.5)

    # Лінія y=0
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Налаштування графіка
    plt.title('Графік функції з заливкою області')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 2)
    plt.ylim(-1, 3)
    plt.legend()
    plt.grid()
    plt.show()


def task_8_2_21():
    # Визначення полярних координат
    phi = np.linspace(0, 2 * np.pi, 100)
    rho = np.cos(phi)**2 + np.sin(phi)**2  # Вона завжди дорівнює 1

    # Побудова графіка
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, projection='polar')
    ax.plot(phi, rho, label=r'$\rho = \cos^2(\phi) + \sin^2(\phi)$', color='magenta')

    # Заливка області
    ax.fill(phi, rho, color='lightblue', alpha=0.5)

    # Налаштування графіка
    ax.set_title('Графік полярної функції')
    ax.set_yticks([])  # Приховати радіусні мітки
    ax.legend()

    plt.show()


def task_8_3_21():
    # Визначення параметр t
    t = np.linspace(0, 6 * np.pi, 1000)

    # Визначення параметричних рівнянь
    x = 8 * (t - np.sin(t))
    y = 8 * (1 - np.cos(t))

    # Фільтрація y за умовами
    y_filtered = y[y >= 12]
    x_filtered = x[y >= 12]

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r'$x(t) = 8(t - \sin(t)), y(t) = 8(1 - \cos(t))$', color='blue')
    plt.axhline(12, color='red', linestyle='--', label='y = 12')
    plt.xlim(0, 6 * np.pi)
    plt.ylim(0, np.max(y) + 10)
    plt.fill_between(x_filtered, y_filtered, 12, color='lightblue', alpha=0.5)

    # Налаштування графіка
    plt.title('Графік параметричних рівнянь')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid()
    plt.show()




def task_8_4_21():
     # Визначаємо діапазон x
    x = np.linspace(0, 15/16, 100)

    # Визначаємо функцію y
    y = np.arcsin(x) - np.sqrt(1 - x**2)

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r'$y = \arcsin(x) - \sqrt{1 - x^2}$', color='blue')

    # Заливка області під графіком
    plt.fill_between(x, y, color='lightblue', alpha=0.5)

    # Налаштування графіка
    plt.title(r'Графік функції  $y = \arcsin(x) - \sqrt{1 - x^2}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(0, 15/16)
    plt.ylim(np.min(y) - 1, np.max(y) + 1)
    plt.grid()
    plt.legend()
    plt.show()


def task_8_5_21():
    # Визначаємо діапазон t
    t = np.linspace(0, np.pi / 3, 100)

    # Визначаємо параметричні функції x і y
    x = 2 * np.cos(t) - np.cos(2 * t)
    y = 2 * np.sin(t) - np.sin(2 * t)

    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=r'$(x, y) = (2\cos(t) - \cos(2t), 2\sin(t) - \sin(2t))$', color='orange')

    # Заливка області
    plt.fill_between(x, y, color='lightcoral', alpha=0.5)

    # Налаштування графіка
    plt.title(r'Параметричний графік')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.xlim(np.min(x) - 1, np.max(x) + 1)
    plt.ylim(np.min(y) - 1, np.max(y) + 1)
    plt.legend()
    plt.show()


def menu():
    while True:
        print("\nОберіть задачу для виконання:")
        print("Завдання 1")
        print("Завдання 2")
        print("Завдання 3")
        print("Завдання 4")
        print("Завдання 5")
       
        
        print("6. Вийти")
        
        choice = input("Введіть номер задачі (1-5): ")

        match choice:
            case '1':   
                task_8_1_21()
            case '2':
                task_8_2_21()
            case '3':
                task_8_3_21()
            case '4':
                task_8_4_21()
            case '5':
                task_8_5_21()
            case '6':
                print("Вихід з програми.")
                break
            case None:
                print("Невірний вибір. Спробуйте ще раз.")

menu()