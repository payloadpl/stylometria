# https://www.youtube.com/watch?v=Iu-HLy9hICg, 29:48
# podobieństwo (statystyczne własności) - podobieństwo i podobieństwo cosinusowe, demo

import math

def ValSim(x, y):
	return (2*x*y)/(x**2+y**2)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes()
ax.arrow(0.0, 0.0, 8.0, 6.0, head_width=0.2, head_length=0.5, fc='black', ec='black')
ax.arrow(0.0, 0.0, 4.0, 4.0, head_width=0.2, head_length=0.5, fc='red', ec='red')

plt.grid()
plt.xlim(0,9)
plt.xlabel('czas')
plt.ylim(0,8)
plt.ylabel('droga')
plt.title('Stosunek drog do czasu, czyli prędkość v', fontsize=10)
plt.savefig('test.png', format='png')
plt.close()

# w oryginale zamiast savefig() jest show() w celu pokazania obrazka bezpośrednio w Jupyter Notebooku,
# tutaj jest on zapisywany do osobnego pliku PNG

# na podstawie tego dema prezentujący aż do 31:50 tłumaczy, czym jest odległość cosinusowa między dwoma wektorami
