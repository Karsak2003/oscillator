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

noise = lambda time, n=0, q=0.1: np.random.normal(n, q, time.shape[0])

amplitude = 1
phase = 0
w = 2*np.pi

star_time = 0
end_time = 1
dt = 0.01



time = np.arange(star_time, end_time, dt)
mas_x = [amplitude*np.sin(w * t + phase ) for t in time]

mas_x_noise = mas_x + noise(time= time)

ax = plt.subplot()
ax.plot(time, mas_x, label=f'{amplitude}sin({round(w, 3)}t+{phase})')
ax.plot(time, mas_x_noise, label=f'x(t) + noise(t)')
ax.set_xlabel('Время, с')
ax.set_ylabel('X, м')
ax.set_title("График горманических колебаний")

ax.legend()

plt.show()