import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import os

# Створюємо папку для збереження GIF-файлів
output_folder = "animations"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def task1():
    fig, ax = plt.subplots()
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

    def update(frame):
        ax.clear()

        # Параметр t
        t = np.linspace(0.1, 5, 100)

        # Перший графік: оригінальна функція
        y1 = t - np.arctan(t)
        x1 = np.log(1 / np.tan(t)) + (30 - frame % 30 if frame >= 30 else frame) / 3
        ax.plot(x1, y1, color=colors[frame % len(colors)], label='y = t - arctan(t)')

        # Другий графік: графік на основі арксинуса та арккосинуса
        x2 = np.arcsin(t / (1 + t**2))
        y2 = np.arccos(1 / np.sqrt(1 + t**2))
        ax.plot(x2, y2, color='black', linestyle='--', label='y = arccos(1 / sqrt(1 + t^2))')

        # Додавання меж і титулу
        plt.title(f'Frame {frame}')
        ax.set_xlim(0, 10.5)
        ax.set_aspect("equal")

        # Додавання легенди
        ax.legend()

    # Анімація
    animation = FuncAnimation(fig, update, frames=60, interval=100)

    # Збереження анімації у форматі GIF
    animation.save(os.path.join(output_folder, "LR4_task1.gif"), writer='pillow')
    plt.show()

def task2():
    # Створення фігури
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')  

    # Ініціалізація сітки для осей X та Y
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)

    # Формула для еліптичного параболоїда
    Z = X**2 + Y**2

    # Створення порожнього списку для зберігання поверхонь
    surface = [ax.plot_surface(X, Y, Z, color='blue', alpha=0.6)]

    # Функція оновлення для анімації
    def update(frame):
        ax.clear()

        # Оновлення поверхні еліптичного параболоїда
        Z = X**2 + Y**2
        surface[0] = ax.plot_surface(X, Y, Z, color='blue', alpha=0.6)

        # Оновлення положення площини x = 2 + зміна кожного кадру
        X_plane = 2 + frame * 0.05  # Зміщення площини з кожним кадром
        Z_plane = X_plane**2 + y**2  # z = x^2 + y^2 при новому X_plane

        # Побудова перетину площиною
        Y_plane, Z_plane = np.meshgrid(y, Z_plane)
        ax.plot_surface(X_plane * np.ones_like(Y_plane), Y_plane, Z_plane, color='red', alpha=0.7)

        # Налаштування осей та титулу
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Еліптичний параболоїд, площина x = {X_plane:.2f}')

    # Створення анімації
    animation = FuncAnimation(fig, update, frames=50, interval=100)

    # Збереження анімації у форматі GIF
    animation.save(os.path.join(output_folder, "LR4_task2_paraboloid.gif"), writer='pillow')
    plt.show()

def task3():
    # Створення фігури для полярної системи координат
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Функція оновлення для анімації
    def update(frame):
        ax.clear()

        # Задаємо кут theta (phi) від 0 до 2pi
        theta = np.linspace(0, 2 * np.pi, 1000)

        # Задаємо радіус r для рівняння r = 3 * cos(4 * phi)
        r = 3 * np.cos(4 * theta + (frame * np.pi / 50))  # Анімація з обертанням

        # Побудова графіка
        line, = ax.plot(theta, r, color='purple')

        # Налаштування радіусів
        ax.set_rmax(3)
        ax.set_rmin(-3)

        # Додаємо заголовок
        ax.set_title(f'r=3cos(4*phi)')

        return line,

    # Створення анімації
    animation = FuncAnimation(fig, update, frames=100, interval=100)

    # Збереження анімації у форматі GIF
    animation.save(os.path.join(output_folder, "LR4_task3_cos4phi.gif"), writer='pillow')
    plt.show()



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