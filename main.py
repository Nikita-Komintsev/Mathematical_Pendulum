import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Функция, которая описывает дифференциальное уравнение маятника
def pendulum(t, y, g, L):
    theta, omega = y
    dydt = [omega, -(g / L) * np.sin(theta)]
    return dydt

# Функция для решения дифференциального уравнения и построения графиков
def simulate_pendulum():
    theta0 = float(theta0_entry.get())
    omega0 = float(omega0_entry.get())
    g = 9.81  # Ускорение свободного падения (постоянное)
    L = 1.0   # Длина нити (постоянная)

    # Отображение дифференциального уравнения
    diff_eq_label.config(text=f"Дифференциальное уравнение: d^2θ/dt^2 = -(g / L) * sin(θ)")

    # Время для решения уравнения
    t_span = (0, 10)

    # Начальные условия
    y0 = [theta0, omega0]

    # Решение дифференциального уравнения
    sol = solve_ivp(pendulum, t_span, y0, args=(g, L), t_eval=np.linspace(0, 10, 1000))

    # Извлечение решения
    t = sol.t
    theta = sol.y[0]

    # Построение графика x(t)
    plt.figure(1)
    plt.plot(t, L * np.sin(theta))
    plt.xlabel('Время (сек)')
    plt.ylabel('x (м)')

    # Построение фазового портрета
    plt.figure(2)
    plt.plot(theta, L * sol.y[1])
    plt.xlabel('Угол (рад)')
    plt.ylabel('Угловая скорость (рад/с)')

    # Отображение графиков
    plt.show()

# Создание графического интерфейса
app = tk.Tk()
app.title("Математический маятник")

frame = ttk.Frame(app)
frame.grid(row=0, column=0)

theta0_label = ttk.Label(frame, text="Начальный угол (радианы):")
theta0_label.grid(row=0, column=0)

theta0_entry = ttk.Entry(frame)
theta0_entry.grid(row=0, column=1)
theta0_entry.insert(0, "0.785")  # Значение по умолчанию (45 градусов)

omega0_label = ttk.Label(frame, text="Начальная угловая скорость (рад/с):")
omega0_label.grid(row=1, column=0)

omega0_entry = ttk.Entry(frame)
omega0_entry.grid(row=1, column=1)
omega0_entry.insert(0, "0.0")  # Значение по умолчанию

diff_eq_label = ttk.Label(frame, text="Дифференциальное уравнение: d^2θ/dt^2 = -(g / L) * sin(θ)")
diff_eq_label.grid(row=3, column=0, columnspan=2)

simulate_button = ttk.Button(frame, text="Симулировать", command=simulate_pendulum)
simulate_button.grid(row=4, column=0, columnspan=2)

app.mainloop()
