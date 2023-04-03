# Написал студент
# группы ЭВТ-20-1б  
# Каримов Рустам Тависович 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

'''
x(t) = A sin (wt + φ)

φ - фаза (радиан/градус)
A - амплитуда колибаний ([м] - метр)
w - частота колибаний ([Гц] - Герц)
t - время ([с] - секунда)
'''

def f_SNR(a, axis=0 , ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)

    return np.where(sd == 0, 0, m/sd)
def f_CV(a, ddof=0):
    n = a.mean()
    q = a.std(ddof=ddof)

    return q/n * 100 
def f_moving_average(a, n=3):
    e = np.cumsum(a, dtype=float)
    e[n:] = e[n:] - e[:-n]
    return e[n-1:]/n
def f_SNR_v2(a, ddof=0):
    n = a.mean()
    q = a.std(ddof=ddof)
    return n/q
noise = lambda time, n=0, q=0.1: np.random.normal(n, q, time.shape[0])

amplitude = 1
phase = 0
w = 2*np.pi

star_time = 0
end_time = 1
dt = 0.01

c_a = 0.25

time = np.arange(star_time, end_time, dt)
mas_x = [amplitude*np.sin(w * t + phase ) for t in time]
mas_x_noise = mas_x + noise(time= time)
mas_x_noise_add_cost = mas_x_noise + c_a

print(f'SNR(XN(t)) = {f_SNR(mas_x_noise)}')
print(f'SNR(XNaddC(t)) = {f_SNR(mas_x_noise_add_cost)}')
print(f'CV(XN(t)) = {f_CV(mas_x_noise)}')
print(f'CV(XNaddC(t)) = {f_CV(mas_x_noise_add_cost)}')

fg, ax = plt.subplots(figsize=(7.5, 3.5), layout='constrained')
ax.plot(time, mas_x, label=f'X(t) = {amplitude}sin({round(w, 3)}t+{phase})')
ax.plot(time, mas_x_noise, label=f'XN(t) = X(t) + noise(t)')
ax.plot(time, mas_x_noise_add_cost, label=f'XNaddC(t) = x(t) + noise(t) + {c_a}')
ax.set_xlabel('Время, с')
ax.set_ylabel('X, м')
ax.set_title("График горманических колебаний")

ax.legend()

fg_1, ax_1 = plt.subplots(figsize=(7.5, 3.5), layout='constrained')
for K in sorted([2, 5, 10] + list(set(np.random.randint(5, 50, size=10)))):
    S = f_moving_average(mas_x_noise_add_cost, n=K)
    k = np.linspace(-1, 1, len(S))
    SNR, CV = f_SNR_v2(S), f_CV(S)
    ax_1.plot(k, S, label=f'K={K}, SNR={round(SNR, 2)}, CV={round(CV, 2)}')
ax_1.set_title("Скользащее среднее с различным K")
ax_1.legend()

plt.show()


