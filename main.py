import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from phaseportrait import PhasePortrait2D


# Функция, которая описывает дифференциальное уравнение маятника
def pendulum(t, y, g, L):
    theta, omega = y
    dydt = [omega, -(g / L) * np.sin(theta)]
    return dydt


# Функция для решения дифференциального уравнения и построения графиков
def simulate_pendulum():
    g = float(g_entry.get())
    L = float(L_entry.get())

    # Отображение дифференциального уравнения
    diff_eq_label.config(text=f"Дифференциальное уравнение: d^2θ/dt^2 = -(g / L) * sin(θ)")

    # Время для решения уравнения
    t_span = (0, 10)

    # Начальные условия
    theta0 = np.pi / 4
    omega0 = 0
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

    # Создание третьего графика с использованием PhasePortrait2D
    def dFOscillator(x, y):
        return y, - np.sin(x)

    example3 = PhasePortrait2D(dFOscillator, [-3, 3], Title=r'Mathematical pendulum phase portrait', xlabel=r'$\phi$',
                               ylabel=r'$\dot{\phi}$')

    # Создание отдельного окна для третьего графика
    plt.figure(3)
    fig3, ax3 = example3.plot()

    # Отображение графиков
    plt.show()


# Создание графического интерфейса
app = tk.Tk()
app.title("Математический маятник")

frame = ttk.Frame(app)
frame.grid(row=0, column=0)

g_label = ttk.Label(frame, text="Ускорение свободного падения (g):")
g_label.grid(row=0, column=0)

g_entry = ttk.Entry(frame)
g_entry.grid(row=0, column=1)

L_label = ttk.Label(frame, text="Длина нити (L):")
L_label.grid(row=1, column=0)

L_entry = ttk.Entry(frame)
L_entry.grid(row=1, column=1)

diff_eq_label = ttk.Label(frame, text="Дифференциальное уравнение: d^2θ/dt^2 = -(g / L) * sin(θ)")
diff_eq_label.grid(row=2, column=0, columnspan=2)

simulate_button = ttk.Button(frame, text="Симулировать", command=simulate_pendulum)
simulate_button.grid(row=3, column=0, columnspan=2)

app.mainloop()
