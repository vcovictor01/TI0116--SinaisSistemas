import numpy as np
import matplotlib.pyplot as plt

#define as amostras de tempo discreto
P = [3, 5, 10, 60]

def funcaoTempo(A):
    return np.linspace(0, 1/120, A)

#define a senoide
def funcaoSenoidal(t):
    return np.sin(240*np.pi*t)

for i in range(4):
    sinal = funcaoSenoidal(funcaoTempo(P[i]))
    plt.subplot(2,2,i+1)
    plt.vlines(funcaoTempo(P[i]), ymin=0, ymax=sinal, colors="#669692")
    plt.plot(funcaoTempo(P[i]), sinal,'o', color="#3d5b59", markersize=3)
    plt.xticks([0, 0.008])
    plt.yticks([-1, 0, 1])
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.minorticks_on()
    ax.grid(True, which='major', color='lightgray', linestyle='-', linewidth=1)
    ax.grid(True, which='minor', color='lightgray', linestyle='-', linewidth=0.4)

plt.savefig("sis1aGrafico.png", dpi=300, bbox_inches='tight')
plt.show()