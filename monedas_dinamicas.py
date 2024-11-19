

def reconstruccion(monedas, matriz):
    i, k = 0, len(monedas)
    instucciones = []
    while k > 0:
        if matriz[k][i] == matriz[k - 2][i + 1] + monedas[i]:
            instucciones.append(f"Sophia debe agarrar la primera ({monedas[i]})")
            i += 1
        elif (matriz[k][i] == matriz[k - 2][i + 2] + monedas[i]
              and (matriz[k][i] != matriz[k - 2][i] + monedas[k + i - 1]
                   or monedas[i + 1] <= (monedas[k + i - 1] and monedas[i]))):
            instucciones.append(f"Sophia debe agarrar la primera ({monedas[i]})")
            i += 1
        else:
            instucciones.append(f"Sophia debe agarrar la ultima ({monedas[k + i - 1]})")
        k -= 1

        if k > 0:
            if monedas[i] <= monedas[k + i - 1]:
                instucciones.append(f"Mateo agarra la ultima ({monedas[k + i - 1]})")
            else:
                instucciones.append(f"Mateo agarra la primera ({monedas[i]})")
                i += 1
            k -= 1
    return instucciones


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

    """Defino una matriz de el optimo de subarreglos que se divide por el largo de el subarreglo en
     filas y por la posicion del arreglo original por la que empiezo a construir el subarreglo en columnas"""
    arr = [0] * (len(monedas))
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

    total_monedas = sum(monedas)
    total_sophia = matriz[len(monedas)][0]
    total_mateo = total_monedas - total_sophia
    decisiones = reconstruccion(monedas, matriz)

    return decisiones, total_sophia, total_mateo

