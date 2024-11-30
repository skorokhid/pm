import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle 
from scipy.optimize import fsolve
                                                                # Перше завдання 
def task1():
    # Параметр t
    t = np.linspace(-10, 10, 400)

    # Параметрично задані рівняння
    x = np.arcsin(t / (1 + t**2))
    y = np.arccos(1 / np.sqrt(1 + t**2))

    # Створення графіка
    plt.plot(x, y, label=r'$y = \arccos\left(\frac{1}{\sqrt{1+t^2}}\right)$' + '\n' + r'$x = \arcsin\left(\frac{t}{1+t^2}\right)$', color='g')

    # Підписи до графіка
    plt.title("Параметрично задана крива")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    # Відображення графіка
    plt.grid(True)
    plt.show()

#                                                                 # Друге завдання 
def task2():
    # Задані параметри
    a = 3
    b = -3

    # Функція f(φ)
    def f(phi):
        return np.cos(phi)

    # Функція для обчислення ρ(φ)
    def rho(phi, a, b):
        return a / (1 + b * f(phi))

    # Генеруємо значення φ від 0 до 2π
    phi = np.linspace(0, 2 * np.pi, 1000)

    # Обчислюємо ρ для кожного значення φ
    rho_values = rho(phi, a, b)

    # Створюємо графік у полярній системі координат
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, projection='polar')

    # Додаємо криву з підписом
    ax.plot(phi, rho_values, label=r'$\rho = \frac{a}{1 + b \cdot \cos(\phi)}$')

    # Налаштовуємо заголовок
    ax.set_title(r'Polar plot with $a = 3, b = -3$', va='bottom')

    # Додаємо легенду для підпису кривої
    ax.legend(loc='upper right')

    # Відображаємо графік
    plt.show()
#                                                             # Третє завдання


def task3():
    t = np.linspace(-10, 10, 400)
    x, y = np.meshgrid(t, t)

    # Формула для кривої
    curve = 9*x**2 + 6*x*y + y**2 - 3*np.sqrt(np.abs(10*x)) - 9*np.sqrt(np.abs(10*y)) - 90

    plt.figure(figsize=(8, 6))  # Збільшимо розмір фігури для кращої видимості

    # Побудова контуру кривої
    contours = plt.contour(x, y, curve, levels=[0], colors='blue', linewidths=2)

    # Додаємо обертання тексту на 30 градусів
    plt.text(-8, 8, r'$9x^2 + 6xy + y^2 - 3\sqrt{10x} - 9\sqrt{10y} - 90$', 
             fontsize=12, color='black', rotation=30, rotation_mode='anchor')

    # Налаштування осей
    plt.xlabel('x')
    plt.ylabel('y')

    # Назва графіка
    plt.title('Кольорова задана крива (зміщений підпис під кутом 30 градусів)')

    # Увімкнемо сітку
    plt.grid(True)

    # Встановимо межі осей для кращої видимості
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.show()


# Виклик функції


                                                      # Четверте завдання    
def task4_1():
 
    # перший графік 
    x = np.linspace(-2*np.pi, 2*np.pi,400)

    y1 = x**3 -1
    y2 = np.sin(x-3)

    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.plot(x, y1, label=r'$y = x^3 - 1$', color='brown')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Графік y = x^3 -1')
    plt.grid(True)
    plt.legend()
    # другий графік

    plt.subplot(1,2,2)
    plt.plot(x,y2,label = 'y = sin(x-3)',color = 'red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Графік y = sin(x-3)')
    plt.grid(True)
    plt.legend(loc = 'upper right')

    plt.tight_layout()

    plt.show()
#######################################

def task4_2():
    x = np.linspace(-3, 3, 100)

    f_x = x**3 - 1
    g_x = np.sin(x - 3)

    plt.figure(figsize=(8, 6))

    plt.plot(x, f_x, label='$f(x) = x^3 - 1$', color='brown', linewidth=2.5)
    plt.plot(x, g_x, label='$g(x) = \sin(x - 3)$', color='red', linewidth=1.5)

    plt.axhline(0, color='black', linewidth=0.5)  # Ось y
    plt.axvline(0, color='black', linewidth=0.5)  # Ось x

    plt.xlabel('x')
    plt.ylabel('y') 
    plt.title('Графіки функцій f(x) та g(x)')
    plt.legend()
    plt.grid(True)

    # Функція для знаходження різниці між f(x) та g(x)
    def intersection_func(x):
        return x**3 - 1 - np.sin(x - 3)

    # Використовуємо fsolve для знаходження коренів
    intersection_x = fsolve(intersection_func, 0)[0]  # Використовуємо перше значення
    intersection_y = intersection_x**3 - 1  # Знаходимо y для точки перетину

    # Відзначаємо точку перетину на графіку
    plt.plot(intersection_x, intersection_y, 'go', label='Точка перетину')
    
    # Додаємо текст з координатами
    plt.text(intersection_x, intersection_y, f'({intersection_x:.2f}, {intersection_y:.2f})', 
             fontsize=10, ha='right', color='green')

    plt.legend()
    plt.show()





                                                    # Пяте завдання


def task5_1():
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)

    ellipse = (27 * X**2) / 28 + (9 * Y**2) / 7 - 1

    line = 3 * X - Y + 5

    plt.figure(figsize=(8, 6))

    plt.contour(X, Y, ellipse, levels=[0], colors='blue', linewidths=2)
    
    plt.contour(X, Y, line, levels=[0], colors='red', linewidths=2)

    plt.text(4, 0, r'$\frac{27x^2}{28} + \frac{9y^2}{7} = 1$', fontsize=12, color='blue', rotation=30)
    plt.text(2, 4, r'$3x - y + 5 = 0$', fontsize=12, color='red', rotation=-15)

    plt.legend([r'$\frac{27x^2}{28} + \frac{9y^2}{7} = 1$', r'$3x - y + 5 = 0$'])

    plt.xlabel('x')
    plt.ylabel('y')

    plt.title('Графіки функцій')

    plt.grid(True)

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.show()


# 5.2
def task5_2():
    x = np.linspace(-10,10,400)

    y1 = np.sqrt((7/9)*(1 - (27*x**2)/28))

    y2 = 3*x+5

    fig, (ax1,ax2) = plt.subplots(1,2,figsize = (12,6))

    ax1.plot(x,y1,label=r'$\frac{27x^2}{28} + \frac{9y^2}{7} = 1$',color = 'blue',linestyle = '-',linewidth = 2)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title(r'Графік рівняння $\frac{27x^2}{28} + \frac{9y^2}{7} = 1$')
    ax1.grid(True)

    ax2.plot(x,y2,label=r'$3x - y + 5 = 0$',color = 'red',linestyle = '--',linewidth = 2)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title(r'Графік рівняння $3x - y + 5 = 0$')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

                                                                            # Шосте завдання

def task6_1():
    num_columns = 26
    data = np.random.rand(num_columns)
    column_names = [f'Стовпчик {i+1}' for i in range(num_columns)]
    colors = ['r', 'g', 'b', 'c']  # Чотири кольори для стовпчиків
    plt.figure(figsize=(12, 6))
    bar_width = 0.5  
    for i in range(num_columns):
        heights = [data[i] / 4] * 4
        cumulative_height = 0  

        for j, color in enumerate(colors):
            plt.bar(i, heights[j], color=color, bottom=cumulative_height, width=bar_width)
            cumulative_height += heights[j]  # Оновлюємо сумарну висоту
    plt.xlabel('Стовпці')
    plt.ylabel('Значення')
    plt.title('Різнокольорова стовпчаста діаграма з 4 кольорами (вертикально)')
    plt.xticks(np.arange(num_columns), column_names, rotation=45, ha='right') 
    plt.tight_layout()
    plt.show()

def task6_2():
    data = [10,15,20,25,30,35,40,45,50,55]

    num_bins = 20
    bin_edges = [0,20,40,60]

    plt.figure(figsize=(8,6))
    plt.hist(data,bins=bin_edges,edgecolor = 'k',alpha = 0.7)
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.title('Гістограма з угрупованням')
    plt.show()

def task6_3():
    sizes = [30,15,10,20,25,12]

    labels = ['Сектор 1','Сектор 2','Сектор 3','Сектор 4','Сектор 5','Сектор 6']
    colors = ['red','green','blue','orange','purple','pink']

    explode = (0,0,0,0,0,0.2)

    plt.figure(figsize=(6,6))
    plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.1f%%',startangle=90)
    plt.title('Кругова діаграма з вийнятими секторами')
    plt.show()

def task6_4(): 
    num_points = 30

    x = [np.random.uniform(1, 10) for _ in range(num_points)]
    y = [np.random.uniform(1, 10) for _ in range(num_points)]
    categories = [np.random.choice(['A', 'B', 'C', 'D', 'E']) for _ in range(num_points)]
    plt.figure()
    markers = ['s', 'D', 'o', '^', 'X']
    colors = ['red', 'blue', 'green', 'orange', 'purple']

    for marker, color in zip(markers, colors):
        plt.scatter([np.random.uniform(1, 10) for _ in range(num_points)], 
                    [np.random.uniform(1, 10) for _ in range(num_points)], 
                    marker=marker, color=color)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Діаграма розсіювання зі спеціальними позначеннями')
    plt.show()
                                                                                # Меню
def menu():
    while True:
        print("\nОберіть задачу для виконання:")
        print("1. Параметрично задана крива")
        print("2. Полярний графік")
        print("3. Кольорова задана крива")
        print("4. Графіки функцій")
        print("5. Кольорові графіки")
        print("6.Діаграми")
        
        print("7. Вийти")
        
        choice = input("Введіть номер задачі (1-5): ")

        match choice:
            case '1':
                task1()
            case '2':
                task2()
            case '3':
                task3()
            case '4':
                task4_1()
                task4_2()
            case '5':
                task5_1()
                task5_2()
            case '6': 
                task6_1()
                task6_2()
                task6_3()
                task6_4()
            case '7':
                print("Вихід з програми.")
                break
            case None:
                print("Невірний вибір. Спробуйте ще раз.")

menu()


