from monedas_dinamicas import monedas_dinamicas
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

#Numeros del 1 al 50 desordenados
monedas = [34, 7, 25, 2, 49, 16, 45, 12, 37, 1, 28, 20, 6, 31, 39, 46, 48, 23, 9, 11, 30, 36, 15, 14, 21, 38, 44, 5, 10, 32, 24, 50, 42, 13, 22, 3, 17, 18, 8, 4, 43, 26, 35, 33, 40, 19, 41, 29, 27, 47]
#Primero voy a ordenar y desordenar este array de forma diferente para ver como cambia el resultado

monedas_asc = sorted(monedas)
monedas_dec = sorted(monedas, reverse=True)

_, monedas_sophia_des, ganancia_des, _ = monedas_dinamicas(monedas)
_, monedas_sophia_asc, ganancia_asc, _ = monedas_dinamicas(monedas_asc)
_, monedas_sophia_dec, ganancia_dec, _ = monedas_dinamicas(monedas_dec)

print(ganancia_des) #752
print(ganancia_asc) #650
print(ganancia_dec) #650

#A diferencia de greedy, el algoritmo da mejores resultados cuando el array está desordenado.

def get_random_array():
    return random.sample(range(1,51), 50)

sns.set_theme()
x = np.linspace(1,30,30).astype(int)

random.seed(12345)
_, y1, g1, _ = monedas_dinamicas(get_random_array())

random.seed(54321)
_, y2, g2, _ = monedas_dinamicas(get_random_array())

ax: plt.axes
fig, ax = plt.subplots()
ax.plot(x, [sum(monedas_sophia_des[:i]) for i in x], label="Ganancia Desordenada 1", color="lime")
ax.plot(x, [sum(y1[:i]) for i in x], label="Ganancia Desordenada 2", color="dodgerblue")
ax.plot(x, [sum(y2[:i]) for i in x], label="Ganancia Desordenada 3", color="darkslateblue")
ax.plot(x, [sum(monedas_sophia_asc[:i]) for i in x], 'r--', label="Ganancia Ascendente")
#ax.plot(x, [sum(monedas_sophia_dec[:i]) for i in x], label="Ganancia Descendiente", color="pink")
#El gráfico dec es igual al asc. Me quedo con uno solo.

ax.set_title('Ganancia de Sophia por Cantidad de Monedas')
ax.set_xlabel('Cantidad de monedas')
ax.set_ylabel('Ganancia')
plt.legend()
plt.show()

#Ver como en este caso la ganancia de sophia es menor cuando el array está ordenado.
#Qué pasa si monedas = [1, 10, 5]?
#La ganancia de mateo va a ser 10, y al de sophia 6
#   -> Sophia puede perder dependiendo de como se distribuyan las monedas.