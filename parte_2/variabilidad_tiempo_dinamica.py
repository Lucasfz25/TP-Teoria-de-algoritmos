from monedas_dinamicas import monedas_dinamicas

from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

from util import time_algorithm


def get_random_array(size: int):
    return list(np.random.randint(0, 1000, size))

if __name__ == '__main__':  #Este bloque es para que no explote time_algorithm
    
    sns.set_theme()

    x = np.linspace(5,100,20).astype(int)

    seed(12345)
    np.random.seed(12345)
    results = time_algorithm(monedas_dinamicas, x, lambda s: [get_random_array(s)])
    r_ordenado = time_algorithm(monedas_dinamicas, x, lambda s: [sorted(get_random_array(s))])

    np.random.seed(2)
    r1 = time_algorithm(monedas_dinamicas, x, lambda s: [get_random_array(s)])
    np.random.seed(3)
    r2 = time_algorithm(monedas_dinamicas, x, lambda s: [get_random_array(s)])
    np.random.seed(54321)
    r3 = time_algorithm(monedas_dinamicas, x, lambda s: [get_random_array(s)])
    
    ax: plt.axes
    fig, ax = plt.subplots()
    
    ax.plot(x, [r1[i] for i in x], label="Lista 1", color="lime")
    ax.plot(x, [r2[i] for i in x], label="Lista 2", color="darkslateblue")
    ax.plot(x, [r3[i] for i in x], label="Lista 3", color="dodgerblue")
    ax.plot(x, [r_ordenado[i] for i in x], "r--", label="Lista Ordenada")
    
    ax.set_title('Tiempo de Ejecución para Distintos Valores')
    ax.set_xlabel('Cantidad de monedas')
    ax.set_ylabel('Tiempo de ejecución [s]')
    plt.legend()
    plt.show()