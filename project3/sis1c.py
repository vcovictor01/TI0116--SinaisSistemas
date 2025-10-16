import numpy as np
import matplotlib.pyplot as plt

#Definindo diferentes frequência em ordem crescente com incremento de 1pi/2;
WO = [0, 1/2*np.pi, np.pi, 3/2*np.pi, 2*np.pi,
      5/2*np.pi, 3*np.pi, 7/2*np.pi, 4*np.pi]

#Defininfo à região de atuação de cada frequência no gráfico
N = [np.linspace(-2,0,3), np.linspace(0,2,3), 
     np.linspace(2,4,3), np.linspace(4,6,3),
     np.linspace(6,8,3), np.linspace(8,10,3), 
     np.linspace(10,12,3), np.linspace(12,14,3)]

#Definindo a função de onda - teta é a fase
def funcaoExponencial(wo, n,teta):
    return np.e**((wo*n*1j)+(teta*1j))

fase = 0 #Fase para sincronizar as funções
sinal = [] #Criando uma lista vazia de sinais

for i in range(8):
    #Criando os sinais para diferentes frequências e adicionando-os à lista
    sinal.append(funcaoExponencial(WO[i], N[i], fase))

    #Plotando o gráfico
    plt.plot(N[i], sinal[i], '--', color="#4F777392", linewidth = 1)
    plt.vlines(N[i], ymin=0, ymax=sinal[i], colors="#669692")
    plt.plot(N[i], sinal[i],'o', color="#3d5b59", markersize=3)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.minorticks_on()
    ax.grid(True, which='major', color='lightgray', linestyle='-', linewidth=1)
    ax.grid(True, which='minor', color='lightgray', linestyle='-', linewidth=0.4)

    #Ajustando a fase do próximo sinal para sincronizar todas as ondas
    fase += WO[i]*(N[i][-1] - N[i][0])

#Nomeando cada região do gráfico com sua respectiva frequência Wo
plt.text(-1.5, -0.75, 'wo = 0', fontsize=11, color="#202B2ACA")
plt.text(0.5, -0.75, 'wo = pi/2', fontsize=11, color="#202B2ACA")
plt.text(2.5, -0.75, 'wo = pi', fontsize=11, color="#202B2ACA")
plt.text(4.5, -0.75, 'wo = 3pi/2', fontsize=11, color="#202B2ACA")
plt.text(6.5, -0.75, 'wo = 2pi', fontsize=11, color="#202B2ACA")
plt.text(8.5, -0.75, 'wo = 5pi/2', fontsize=11, color="#202B2ACA")
plt.text(10.5, -0.75, 'wo = 4pi', fontsize=11, color="#202B2ACA")
plt.text(12.5, -0.75, 'wo = 7pi/2', fontsize=11, color="#202B2ACA")

plt.savefig("sis1cGrafico.png", dpi=300, bbox_inches='tight')
plt.show()