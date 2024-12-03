
def get_index(lista, barco, aparicion):
    cont = 0
    for i, n in enumerate(lista):
        if n == barco:
            cont += 1
            if cont == aparicion:
                return i


def contar_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total


def barcos_adyacentes(tablero, coordenada, inicio, barco):
    if coordenada[0] is None:
        coordenadas = (inicio, coordenada[1])
        for i in range(barco):
            for f in range(-1, 2):
                if coordenadas[0] + f < 0 or coordenadas[0] + f >= len(tablero):
                    continue
                for c in range(-1, 2):
                    if coordenadas[1] + c + i < 0 or coordenadas[1] + c + i >= len(tablero[0]):
                        continue
                    elif tablero[coordenadas[0] + f][coordenadas[1] + c + i] is not None:
                        return True
    else:
        coordenadas = (coordenada[0], inicio)
        for i in range(barco):
            for f in range(-1, 2):
                if coordenadas[0] + f + i < 0 or coordenadas[0] + f + i >= len(tablero):
                    continue
                for c in range(-1, 2):
                    if coordenadas[1] + c < 0 or coordenadas[1] + c >= len(tablero[0]):
                        continue
                    elif tablero[coordenadas[0] + f + i][coordenadas[1] + c] is not None:
                        return True

    return False


def posicionar_barco(barcos, valor_restriccion, restriccion_min, tablero, coordenada):
    for barco in barcos:
        if barco <= valor_restriccion:
            inicio = 0
            while inicio + barco <= len(restriccion_min):
                entra = True
                for j in range(barco):
                    if restriccion_min[inicio + j] <= 0:
                        entra = False
                        break

                if entra and not barcos_adyacentes(tablero, coordenada, inicio, barco):

                    return barco, inicio
                inicio += 1
    return -1, -1


def solucion_naval_jj(tablero, barcos, restricciones_f, restricciones_c):
    barcos_ordenados = sorted(barcos, reverse=True)
    solucion = {}
    colocado = False
    demanda_total = contar_lista(restricciones_f) + contar_lista(restricciones_c)
    max_r_fil = sorted(restricciones_f, reverse=True)
    max_r_col = sorted(restricciones_c, reverse=True)
    while len(barcos_ordenados) > 0 and len(max_r_fil) > 0 and len(max_r_col) > 0:
        coordenadas = []
        if colocado:
            max_r_fil = sorted(restricciones_f, reverse=True)
            max_r_col = sorted(restricciones_c, reverse=True)
        colocado = False
        if max_r_fil[0] >= max_r_col[0]:
            coordenada = restricciones_f.index(max_r_fil[0])
            barco, inicio = posicionar_barco(barcos_ordenados, max_r_fil[0], restricciones_c,  tablero, (coordenada, None))
            if barco == -1:
                max_r_fil.pop(0)
                continue
            for i in range(barco):
                coordenadas.append((coordenada, inicio + i))
                restricciones_c[inicio + i] -= 1
            restricciones_f[restricciones_f.index(max_r_fil[0])] -= barco
        else:
            coordenada = restricciones_c.index(max_r_col[0])
            barco, inicio = posicionar_barco(barcos_ordenados, max_r_col[0], restricciones_f, tablero, (None, coordenada))
            if barco == -1:
                max_r_col.pop(0)
                continue
            for i in range(barco):
                coordenadas.append((inicio + i, coordenada))
                restricciones_f[inicio + i] -= 1
            restricciones_c[restricciones_c.index(max_r_col[0])] -= barco

        i = 1
        while not colocado:
            posicion = get_index(barcos, barco, i)
            if posicion not in solucion:
                colocado = True
                solucion[posicion] = coordenadas.copy()
                for k in coordenadas:
                    tablero[k[0]][k[1]] = posicion
            i += 1
        barcos_ordenados.remove(barco)
    demanda_cumplida = 0
    for i in solucion:
        demanda_cumplida += len(solucion[i]) * 2
    return solucion, demanda_cumplida, demanda_total


def main():
    restricciones_f = [3,3,0,1,1]
    restricciones_c = [3,1,0,3,3]
    #restricciones_f = [3, 1, 2]
    #restricciones_c = [3, 2, 0]
    arr = [None] * (len(restricciones_c))
    tablero = []
    for i in range(len(restricciones_f)):
        tablero.append(arr.copy())
    barcos = [1,2,2,2,2,1]
    #barcos = [1,1]
    solucion, dc, dt = solucion_naval_jj(tablero, barcos, restricciones_f, restricciones_c)
    print(solucion)
    print(dc)
    print(dt)


main()
