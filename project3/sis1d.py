import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Samples.csv pela biblioteca pandas
dados = pd.read_csv("/home/victor/github/TI0116--SinaisSistemas/project3/samples.csv")  # o nome do arquivo que você mostrou
tn = dados["t_n"].values
xn = dados["x_n"].values
N = len(xn)

# Definindo M arbitrariamente
M = 5

# Implementação do sinal y[n]
y = np.zeros(N)

for n in range(N):
    total = 0
    for k in range(-M, M):
        if 0 <= n-k < N:
            total += xn[n-k]
 
    y[n] = (total/((2*M)+1))

plt.plot(tn, xn, label='x[n]', alpha=0.6)
plt.plot(tn, y, label='y[n] (média móvel)', linewidth=2)
plt.xlabel('t (s)')
plt.grid(True)
plt.show()