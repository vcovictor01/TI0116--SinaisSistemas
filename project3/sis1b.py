import numpy as np
import matplotlib.pyplot as plt

#Considere que utilizaremos 40 amostras no tempo discreto
N = np.linspace(-2,2,40)

#Define a primeira exponencial
#Para uma exponencial simples, tal qual pede o item A, definimos C = 1 e a > 0 (nesse caso: 1)
def funcaoExponencial(n):
    return np.e**n
    
#Define o sinal 1 como a exponencial discreta simples
sinal1 = funcaoExponencial(N)

#Plotagem do gŕafico e customização dos eixos para fins de melhor de visualização
plt.subplot(2,2,1)
plt.vlines(N, ymin=0, ymax=sinal1, colors="#669692")
plt.plot(N, sinal1,'o', color="#3d5b59", markersize=3)
plt.xticks([-2, 0, 2])
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.minorticks_on()
ax.grid(True, which='major', color='lightgray', linestyle='-', linewidth=1)
ax.grid(True, which='minor', color='lightgray', linestyle='-', linewidth=0.4)


#Definimos a segunda exponencial
"""Para um sinal complexo exponencial oscilatório podemos continuar com C = 1,
Visto que esse parâmetro apenas determina amplitude e fase inicial,
E separamos a em sua parte real e imaginária:
Re(a) modela o crescimento da curva e Im(a) o comportamento oscilatório
Como queremos apenas oscilatório: Re(a) = 0 e Im(a) = jw > 0 : w > 0
Escolhemos arbitrariamente w = 2*pi*1/4 para visualizarmos melhor a senoide (1 único período)
OBS: O fator np.pi*1j*1/2 corresponde a fase da onda, ajustada unicamente para
melhor visualização do gráfico.
"""
def funcaoExponencialComplexaOscilatoria(n):
    return (np.e**((1j*2*np.pi*1/4*n)+(np.pi*1j*1/2)))

sinal2 = funcaoExponencialComplexaOscilatoria(N)

plt.subplot(2,2,2)
plt.vlines(N, ymin=0, ymax=sinal2, colors="#669692")
plt.plot(N, sinal2,'o', color="#3d5b59", markersize=3)
plt.xticks([-2, 0, 2])
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.minorticks_on()
ax.grid(True, which='major', color='lightgray', linestyle='-', linewidth=1)
ax.grid(True, which='minor', color='lightgray', linestyle='-', linewidth=0.4)

#Definimos a terceira exponencial
"""Similar ao caso anterior, 
Porém, agora queremos atribuir caráter amortecido à exponencial, 
Para isso damos valor <0 para Re(a)"""

def funcaoExponencialComplexaOscilatoriaAmortecida(n):
    return (np.e**((1j*2*np.pi*n)+(np.pi*1j*1/2)))*(np.e**(-1*n))

sinal3 = funcaoExponencialComplexaOscilatoriaAmortecida(N)

#Essa parte diz respeito às tangentes exponenciais do gráfico amortecido
def funcaoExponencialTangenteSuperior(n):
    return (np.e**(-1*n)+(np.pi*1j*1/2))
sinal4 = funcaoExponencialTangenteSuperior(N)
def funcaoExponencialTangenteInferior(n):
    return (-1*np.e**(-1*n)+(np.pi*1j*1/2))
sinal5 = funcaoExponencialTangenteInferior(N)

plt.subplot(2,2,3)
plt.vlines(N, ymin=0, ymax=sinal3, colors="#669692")
plt.plot(N, sinal3,'o', color="#3d5b59", markersize=3)
plt.plot(N, sinal4, '--', color="#a07373")
plt.plot(N, sinal5, '--', color="#a07373")
plt.xticks([-2, 0, 2])
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.minorticks_on()
ax.grid(True, which='major', color='lightgray', linestyle='-', linewidth=1)
ax.grid(True, which='minor', color='lightgray', linestyle='-', linewidth=0.4)

plt.savefig("sis1bGrafico.png", dpi=300, bbox_inches='tight')
plt.show()