from monedas_greedy import monedas_greedy

from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from util import time_algorithm


def get_random_array(size: int):
    return list(np.random.randint(0, 100000, size))

if __name__ == '__main__':  #Este bloque es para que no explote time_algorithm
    seed(12345)
    np.random.seed(12345)

    sns.set_theme()

    x = np.linspace(1,100000,20).astype(int)
    results = time_algorithm(monedas_greedy, x, lambda s: [get_random_array(s)])

    ax: plt.axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución de greedy')
    ax.set_xlabel('Cantidad de monedas')
    ax.set_ylabel('Tiempo de ejecución [s]')
    plt.legend()
    plt.show()