import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

def monte_carlo(a, b, h, fx):
    """Calculate integral using Monte-Carlo method"""
    rez = 0;

    return

# Визначення функції та межі інтегрування
def f(x):
    return x**2 - (x**3)/2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(a-0.5, b+0.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b, 400)
iy = f(ix)
iS = sum(iy)*(ix[1]-ix[0]) # sum(iY)*deltaX
ax.fill_between(ix, iy, color='gray', alpha=0.3)

h = max(iy) + 0.01
ax.axhline(h, a, b, color='blue')

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) =x^2 - x^3/2 від ' + str(a) + ' до ' + str(b))

plt.grid()
plt.show()

fig, ax = plt.subplots()
ax.axhline(h, a, b, color='blue')
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) =x^2 - x^3/2 від ' + str(a) + ' до ' + str(b) + " методом Монте-Карло")


# Обчислення інтеграла
result, error = spi.quad(f, a, b)
print("SPI.Quad, інтеграл: ", result)

def F(x):
    """Похідна від f(x)"""
    return (x**3)/3 - (x**4)/(2*4)

print("Аналітичний метод, інтеграл: ", F(b) - F(a))
print("Прямокутники на 400 відрізків, інтеграл: ", iS)

# Monte-Carlo method
# Генерація випадкових точок
points = np.array([(random.uniform(a, b), random.uniform(0, h)) for _ in range(25000)])
ax.plot(points[:,0], points[:,1], '.', color='magenta')

# Відбір точок, що знаходяться всередині трикутника
inside_points = np.array([point for point in points if point[1] <= f(point[0])])
ax.plot(inside_points[:,0], inside_points[:,1], '.', color='blue')

# Кількість усіх точок та точок всередині
N = len(points)
M = len(inside_points)
S = (M / N) * (h * (b-a))
print("Monte-Carlo на 25k точек, інтеграл", S)

ax.plot(x, y, 'r', linewidth=2)
plt.grid()
plt.show()