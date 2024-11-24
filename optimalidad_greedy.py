from monedas_greedy import monedas_greedy
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

#Numeros del 1 al 50 desordenados
monedas = [34, 7, 25, 2, 49, 16, 45, 12, 37, 1, 28, 20, 6, 31, 39, 46, 48, 23, 9, 11, 30, 36, 15, 14, 21, 38, 44, 5, 10, 32, 24, 50, 42, 13, 22, 3, 17, 18, 8, 4, 43, 26, 35, 33, 40, 19, 41, 29, 27, 47]
#Primero voy a ordenar y desordenar este array de forma diferente para ver como cambia el resultado
#El algoritmo siempre va a ser óptimo (siempre va a ganar Sophia), pero puede que la ganancia de Sophia dependa de como esté ordenado el array

monedas_asc = sorted(monedas)
monedas_dec = sorted(monedas, reverse=True)

decisiones_des, monedas_sophia_des, monedas_mateo_des = monedas_greedy(monedas)
decisiones_asc, monedas_sophia_asc, monedas_mateo_asc = monedas_greedy(monedas_asc)
decisiones_dec, monedas_sophia_dec, monedas_mateo_dec = monedas_greedy(monedas_dec)

ganancia_des = sum(monedas_sophia_des)
ganancia_asc = sum(monedas_sophia_asc)
ganancia_dec = sum(monedas_sophia_dec)

print(ganancia_des) #913
print(ganancia_asc) #950
print(ganancia_dec) #950

#Como veo que es igual de optimo si ordeno ascendente o descendente, voy a ver si cambia mucho entre diferentes arrays desordenados

#No uso random.randint porque me genera duplicados
def get_random_array():
    return random.sample(range(1,51), 50)


sns.set_theme()
x = np.linspace(1,25,25).astype(int)

random.seed(12345)
res1, y1, mateo1 = monedas_greedy(get_random_array())

random.seed(54321)
res2, y2, mateo2 = monedas_greedy(get_random_array())

#Ajuste por cuadrados mínimos
ax: plt.axes
fig, ax = plt.subplots()
ax.plot(x, [sum(monedas_sophia_des[:i]) for i in x], label="Ganancia Desordenada 1", color="lime")
ax.plot(x, [sum(y1[:i]) for i in x], label="Ganancia Desordenada 2", color="dodgerblue")
ax.plot(x, [sum(y2[:i]) for i in x], label="Ganancia Desordenada 3", color="darkslateblue")
ax.plot(x, [sum(monedas_sophia_asc[:i]) for i in x], 'r--', label="Ganancia Ascendente")
#ax.plot(x, [sum(monedas_sophia_dec[:i]) for i in x], label="Ganancia Descendiente", color="pink")
#El grafico de los arrays ascendente y descendente son iguales. Me quedo con uno solo

ax.set_title('Ganancia de Sophia por Tamaño de Array')
ax.set_xlabel('Cantidad de monedas')
ax.set_ylabel('Ganancia')
plt.legend()
plt.show()

#Ver que hay una leve variación en la ganancia final dependiendo de como están ordenadas las monedas, pero no es significativo.
#Parece ser que la ganancia máxima se alcanza cuando el array está ordenado ascendente o descendentemente, el resultado de cualquier otro ordenamiento va a ser menos óptimo (pero óptimo al fin).