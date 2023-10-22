import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pendulum(u, t, mu=0.5):
    x = u[0]
    v = u[1]
    dx = v
    dv = -np.sin(x)
    return [dx, dv]


if __name__ == "__main__":
    fig1 = plt.figure(figsize=(5.5, 3))
    ax1 = fig1.add_subplot(211)
    x = np.linspace(-3 * np.pi, 3 * np.pi, 100)
    ax1.plot(x, -np.cos(x), 'b', lw=1.5)
    ax1.grid(True, which='major')
    ax1.minorticks_on()
    ax1.axis('tight')
    ax1.axis([-3 * np.pi, 3 * np.pi, -1, 1])
    ax1.set_xticks(np.arange(-3 * np.pi, 3.1 * np.pi, np.pi))
    ax1.set_xticklabels([r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$'])
    ax1.set_xlabel(r'$\theta$')
    ax1.set_ylabel(r'$V(\theta)$')

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    t = np.linspace(0, 50, 200)
    for m in range(0, 60, 5):
        u = odeint(pendulum, [m / 10., 0.], t)
        ax2.plot(u[:, 0], u[:, 1], 'b', lw=1)
        ax2.plot(-u[:, 0], u[:, 1], 'b', lw=1)
        u = odeint(pendulum, [0, m / 10.], t)
        x_masked = np.ma.masked_outside(u[:, 0], -3 * np.pi, 3 * np.pi)
        y_masked = np.ma.masked_outside(u[:, 1], -3, 4)
        ax2.plot(x_masked, y_masked, 'b', lw=1)
        ax2.plot(-x_masked, y_masked, 'b', lw=1)
        ax2.plot(x_masked, -y_masked, 'b', lw=1)
        ax2.plot(-x_masked, -y_masked, 'b', lw=1)

    x = np.linspace(-3 * np.pi, 3 * np.pi, 20)
    y = np.linspace(-7, 7, 15)  # Обновленный интервал от -7 до 7
    x, y = np.meshgrid(x, y)
    X, Y = pendulum([x, y], 0)  # 0 is used as a dummy time value
    M = np.hypot(X, Y)
    M[M == 0] = 1.0
    X, Y = X / M, Y / M
    ax2.quiver(x, y, np.ma.masked_outside(X, -3 * np.pi + 0.1, 3 * np.pi - 0.1), Y, M, pivot='mid', color='r')
    ax2.minorticks_on()
    ax2.axis('scaled')
    ax2.axis([-3 * np.pi, 3 * np.pi, -7, 7])  # Обновленный интервал от -3pi до 3pi и от -7 до 7
    ax2.set_yticks(np.arange(-7, 7.1, 1))  # Обновленные метки на оси y
    ax2.set_xticks(np.arange(-3 * np.pi, 3.1 * np.pi, np.pi))
    ax2.set_xticklabels([r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$'])
    ax2.set_xlabel(r'$\theta$')
    ax2.set_ylabel(r'$\frac{\mathrm{d}\theta}{\mathrm{d}t}$')
    ax2.grid(True)

    plt.subplots_adjust(wspace=0.1, hspace=-0.1)
    plt.show()
