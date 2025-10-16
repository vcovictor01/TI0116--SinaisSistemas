import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Samples.csv pela biblioteca pandas
dados = pd.read_csv("/home/victor/github/TI0116--SinaisSistemas/project3/samples.csv")  # o nome do arquivo que você mostrou
tn = dados["t_n"].values
xn = dados["x_n"].values
N = len(xn)

# Definindo M arbitrariamente
M = 50

# Implementação do sinal y[n]
y = np.zeros(N)

for n in range(N):
    total = 0
    for k in range(-M, M):
        if 0 <= n-k < N:
            total += xn[n-k]
 
    y[n] = (total/((2*M)+1))


#Plotando o gráfico
plt.plot(tn, xn, label='x[n]', alpha=0.6, color="#2b615d")
plt.plot(tn, y, label='y[n] (média móvel)', linewidth=2, color="#993636")
plt.xlabel('tempo (segundos)')
plt.ylabel('retorno da funação x[n] e y[n]')

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.minorticks_on()
ax.grid(True, which='major', color='lightgray', linestyle='-', linewidth=1)
ax.grid(True, which='minor', color='lightgray', linestyle='-', linewidth=0.4)

plt.show()