import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  
b = 2  


for N in [100, 1000, 10000, 20000]:
    points = [(random.uniform(a, b), random.uniform(0, b**2)) for _ in range(N)]
    inside_points = [point for point in points if point[1] <= f(point[0])]

    M = len(inside_points)

    # Площа, обчислена методом Монте-Карло
    Sm = (M / N) * (b - a) * (b ** 2)


    print(f"Площа, обчислена методом Монте-Карло при кількості точок {N}: {Sm}")


    # Графік
    x = np.linspace(a, b, 400)
    y = f(x)


    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    inside_x, inside_y = zip(*inside_points)
    outside_points = [point for point in points if point not in inside_points]
    outside_x, outside_y = zip(*outside_points)

    ax.scatter(inside_x, inside_y, color='blue', s=1, label='Inside Points')
    ax.scatter(outside_x, outside_y, color='green', s=1, label='Outside Points')

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}. Кількість точок {N}')
    ax.legend()
    plt.grid()
    plt.show()

# Обчислення інтегралу за допомогою scipy
result, error = spi.quad(f, a, b)



print(f"Інтеграл: {result}")
