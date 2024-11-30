import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Завдання 1: Побудова простих геометричних фігур на площині
def task1():
    # Створення фігури та осей для малювання
    fig, ax = plt.subplots(figsize=(8, 8))

    # Створення прямокутника
    rectangle = patches.Rectangle((-15, -18), 6, 6, facecolor='red', linewidth=2)
    ax.add_patch(rectangle)

    # Створення півкола
    semicircle = patches.Arc((-5, 10), 8, 8, theta1=0, theta2=180, color='blue', linewidth=2)
    ax.add_patch(semicircle)

    # Створення сектора (чверть кола)
    sector = patches.Wedge(center=(5, -10), r=8, theta1=0, theta2=90, color='brown', linewidth=2)
    ax.add_patch(sector)

    # Створення стрілки
    arrow = patches.Arrow(-15, 15, 10, 5, width=1, color='green')
    ax.add_patch(arrow)

    # Створення трикутника
    triangle = patches.Polygon([(-15, -5), (-10, 5), (-20, 5)], closed=True, facecolor='pink', linewidth=2)
    ax.add_patch(triangle)

    # Створення ромба
    rhombus = patches.Polygon([[12, 18], [16, 14], [12, 10], [8, 14]], closed=True, facecolor='orange', linewidth=2)
    ax.add_patch(rhombus)

    # Налаштування діапазонів осей та зовнішнього вигляду графіка
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Додавання заголовка та відображення графіка
    plt.title('Півколо, стрілка, трикутник, сектор, ромб та прямокутник')
    plt.grid(True)
    plt.show() 

# Завдання 2: Побудова кола зі стрілками між точками


########################################################
def task2():
    n = 21  # Кількість вершин багатокутника (N-варіант)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)  # Кути для вершин багатокутника
    x = np.cos(angles) * 5  # Координати x
    y = np.sin(angles) * 5  # Координати y
    fig, ax = plt.subplots(figsize=(8, 8))

    # Малювання стрілок між вершинами багатокутника
    for i in range(n):
        ax.add_patch(patches.Arrow(x[i], y[i], x[(i+1) % n] - x[i], y[(i+1) % n] - y[i], 
                                   width=0.3, color='blue'))

    # Додавання фігури N багатокутника (заливка)
    ax.fill(x, y, color='lightgreen', alpha=0.6)

    # Обчислення координат центру багатокутника
    center_x = np.mean(x)
    center_y = np.mean(y)

    # Додавання тексту в центрі
    ax.text(center_x, center_y, f'N={n}', fontsize=20, color='black', ha='center', va='center')

    # Налаштування осей та відображення графіка
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    plt.title(f'{n}-кутник зі стрілками по контуру')
    plt.grid(True)
    plt.show()




# Завдання 3: Побудова еліптичного параболоїда та його перетину площиною
def task3():
    x = np.linspace(-5, 5, 400)  # Координати x
    y = np.linspace(-5, 5, 400)  # Координати y
    X, Y = np.meshgrid(x, y)  # Сітка значень

    Z = X**2 + Y**2  # Формула еліптичного параболоїда

    # Побудова графіка
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Побудова поверхні еліптичного параболоїда
    ax.plot_surface(X, Y, Z, color='blue', alpha=0.6)

    # Побудова площини x = 2 та її перетину з параболоїдом
    X_plane = 2
    Z_plane = X_plane**2 + y**2
    Y_plane, Z_plane = np.meshgrid(y, Z_plane)
    ax.plot_surface(X_plane * np.ones_like(Y_plane), Y_plane, Z_plane, color='red', alpha=0.7)

    # Налаштування осей та заголовку
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Еліптичний параболоїд, перетнутий площиною x = 2')

    plt.show()

# Завдання 4: Побудова поверхні рівняння
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def task4():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)

    # Обчислення z згідно з рівнянням
    z = np.sqrt(x**2 + (y**2 / 4) - 4*x - (y / 2) + 21 / 4)

    # Побудова поверхні
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    graph = ax.plot_surface(x, y, z, color='pink')

    # Додавання стрілок у трьох напрямках
    ax.quiver(0, 0, 0, 1, 0, 0, color='red', length=5, arrow_length_ratio=0.2)  # вздовж осі x
    ax.quiver(0, 0, 0, 0, 1, 0, color='green', length=5, arrow_length_ratio=0.2)  # вздовж осі y
    ax.quiver(0, 0, 0, 0, 0, 1, color='blue', length=5, arrow_length_ratio=0.2)  # вздовж осі z

    # Налаштування осей
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Поверхня 4x^2 + y^2 - 4z^2 - 16x - 2y + 21 = 0')

    plt.show()


# Завдання 5: Побудова трьох просторових діаграм
def task5():
    num_columns = 25  # Кількість стовпців

    # Випадкові значення висоти для стовпців
    heights_1 = np.random.rand(num_columns)
    heights_2 = np.random.rand(num_columns)
    heights_3 = np.linspace(0.05, 1, num_columns)

    # Створення графіка
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Малювання трьох наборів стовпців у різних площинах y
    ax.bar(np.arange(num_columns), heights_1, zs=1, zdir='y', color='red', alpha=0.8)
    ax.bar(np.arange(num_columns), heights_2, zs=2, zdir='y', color='green', alpha=0.8)
    ax.bar(np.arange(num_columns), heights_3, zs=0, zdir='y', color='blue', alpha=0.8)

    # Налаштування осей
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Просторові діаграми')

    plt.tight_layout()
    plt.show()

# Завдання 6: Створення трьох графіків в одному вікні
def task6():
    fig = plt.figure(figsize=(18, 6))

    # Перший графік: Еліптичний параболоїд
    ax1 = fig.add_subplot(131, projection='3d')
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = x**2 + y**2
    ax1.plot_surface(x, y, z, color='lightgreen', alpha=0.6)
    ax1.set_title('Еліптичний параболоїд')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')

    # Другий графік: Поверхня з рівнянням 4x^2 + y^2 - 4z^2 - 16x - 2y + 21 = 0
    ax2 = fig.add_subplot(132, projection='3d')
    z = np.sqrt(x**2 + (y**2 / 4) - 4*x - (y / 2) + 21 / 4)
    ax2.plot_surface(x, y, z, color='pink')
    ax2.set_title('$4x^2 + y^2 - 4z^2 - 16x - 2y + 21 = 0$')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('z')

    # Третій графік: Полярний графік
    ax3 = fig.add_subplot(133, polar=True)
    phi = np.linspace(0, 2 * np.pi, 100)
    r = 3 * np.cos(4 * phi)
    ax3.plot(phi, r, color='black')
    ax3.fill(phi, r, 'b', alpha=0.3)
    ax3.set_title('$r=3cos(4phi)$')

    # Відображення всіх графіків
    plt.tight_layout()
    plt.show()

#Меню для вибору завдань
def menu():
    while True:
        print("\nОберіть задачу для виконання:")
        print("Завдання 1")
        print("Завдання 2")
        print("Завдання 3")
        print("Завдання 4")
        print("Завдання 5")
        print("Завдання 6")
        print("7. Вийти")
        
        choice = input("Введіть номер задачі (1-6): ")

        # Використання оператора match для виконання відповідного завдання
        match choice:
            case '1':
                task1()
            case '2':
                task2()
            case '3':
                task3()
            case '4':
                task4()
            case '5':
                task5()
            case '6':
                task6()
            case '7':
                print("Вихід з програми.")
                break
            case None:
                print("Невірний вибір. Спробуйте ще раз.")

# Виклик меню
menu()
