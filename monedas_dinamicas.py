

def elegir_izq(monedas, matriz, inicio):
    valor_izq = monedas[0]
    if len(monedas) <= 2:
        return valor_izq
    else:
        if monedas[1] < monedas[-1]:
            return valor_izq + matriz[len(monedas) - 2][inicio + 1]
        else:
            return valor_izq + matriz[len(monedas) - 2][inicio + 2]


def elegir_der(monedas, matriz, inicio):
    valor_der = monedas[-1]
    if len(monedas) <= 2:
        return valor_der
    else:
        if monedas[0] < monedas[-2]:
            return valor_der + matriz[len(monedas) - 2][inicio]
        else:
            return valor_der + matriz[len(monedas) - 2][inicio + 1]


def monedas_dinamicas(monedas):
    arr = [0] * (len(monedas) + 1)
    matriz = []
    for i in range(len(monedas) + 1):
        matriz.append(arr.copy())

    for largo in range(1, len(monedas) + 1):
        for comienzo in range(0, len(monedas)):
            if largo + comienzo > len(monedas):
                continue
            max_izq = elegir_izq(monedas[comienzo:comienzo + largo], matriz, comienzo)
            max_der = elegir_der(monedas[comienzo:comienzo + largo], matriz, comienzo)
            matriz[largo][comienzo] = max(max_der, max_izq)
    return matriz[len(monedas)][0]
