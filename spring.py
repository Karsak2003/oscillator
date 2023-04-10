# Написал студент
# группы ЭВТ-20-1б  
# Каримов Рустам Тависович 
import numpy as np
from numpy import cos
from numpy import pi as π
import matplotlib.pyplot as plt

'''
Имеется груз, подвешанный на упругой пружине.
на него действует сила тяжести и сила упругости.
В начальный момент времени тело покоиться.

Используя numpy описать повидение системы до, после и в момент нарушения равновесия.

Считать, что пружина абсолютно упругая, сопротивление воздуха не учитовать.
'''



#Ускарение свободного подения, м/с
g = 9.81
#Масса материальной точки, кг
m = 1
#Коэффициент упругости пружины:
k = 0.981
#Точка пакоя:
x0 = m*g/k 
#Круговая частота
ω = (k/m)**0.5
#Амплитуда
xm = 1
#Начальная Фаза
φ0 = 0
#Момент времени нарушения равновесия
t_distr = 2.5

fx = lambda t, A = xm, w0 =ω, fi0 = φ0: A * cos(w0*t + fi0)


start_time = 0
end_time = 10
dt = 0.001

time = list(np.arange(start_time, end_time, dt))
mas_x = []

for t in time:
    if t < (start_time + t_distr):
        mas_x.append(x0)
    else:
        mas_x.append(x0 + fx(t))

fg, ax = plt.subplots(figsize=(7.5, 3.5), layout='constrained')

ax.plot(time, mas_x, label=f'x')
ax.set_xlabel('Время, с')
ax.set_ylabel('X, м')
ax.set_title("График горманических колебаний пружиного маятника")
ax.grid()

plt.show()
