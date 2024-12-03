import sys
import copy
import time

def obtener_datos(archivo_pruebas):
    with open(archivo_pruebas, 'r') as f:
        lineas = f.readlines()

    datos_ordenados = {"filas":[], "columnas":[]}

    datos = [[], [], []]
    numero_lista_actual = 0
    for i in range(2, len(lineas)):
        if lineas[i] == "\n":
            numero_lista_actual += 1
            continue
        if i == len(lineas)-1:
            datos[numero_lista_actual].append(int(lineas[i]))
        else:
            datos[numero_lista_actual].append(int(lineas[i][:-1]))

    datos_ordenados["filas"] = datos[0]
    datos_ordenados["columnas"] = datos[1]

    return datos_ordenados, datos[2]



def generar_posibles_posiciones(datos):
    posibles_posiciones = {}
    posiciones_usadas = {}

    for tamano_barco in datos["barcos"]:
        # Para no volver a generar las posiciones del mismo barco
        if tamano_barco in posibles_posiciones:
            continue

        posibles_posiciones[tamano_barco] = {"cantidad": 0, "derecha": {}, "abajo": {}}
        posiciones_usadas[tamano_barco] = {"derecha": {}, "abajo": {}}

        if tamano_barco == 1:
            for i in range(len(datos["filas"])):
                if datos["filas"][i] == 0:
                    continue
                for j in range(len(datos["columnas"])):
                    if datos["columnas"][j] == 0:
                        continue

                    if i not in posibles_posiciones[tamano_barco]["derecha"]:
                        posibles_posiciones[tamano_barco]["derecha"][i] = []

                    posibles_posiciones[tamano_barco]["derecha"][i].append([j])
                    posibles_posiciones[tamano_barco]["cantidad"] += 1

                posiciones_usadas[tamano_barco]["derecha"][i] = 0


        else:
            # DERECHA
            for i in range(len(datos["filas"])):

                # PARA DESCARTAR FILA 0 O QUE SEA MENOR AL BARCO
                if ( (datos["filas"][i] == 0) or (datos["filas"][i] < tamano_barco) ):
                    continue

                for j in range(len(datos["columnas"])):

                    # PARA DESCARTAR COLUMNA QUE SEA 0
                    if datos["columnas"][j] == 0:
                        continue

                    # PARA DESCARTAR COLUMNA EN DONDE EL BARCO NO ENTRA EN EL TABLERO
                    if len(datos["columnas"]) < (j+tamano_barco):
                        continue

                    posiciones = []
                    hay_espacio = True
                    for x in range(tamano_barco):
                        if datos["columnas"][j+x] < 1:
                            hay_espacio = False
                            break
                        posiciones.append(j+x)
                        
                    # HAY UN CERO UN MEDIO DE DONDE QUIERO PONER EL BARCO
                    if not hay_espacio:
                        continue

                    if i not in posibles_posiciones[tamano_barco]["derecha"]:
                        posibles_posiciones[tamano_barco]["derecha"][i] = []

                    posibles_posiciones[tamano_barco]["derecha"][i].append(posiciones)
                    posibles_posiciones[tamano_barco]["cantidad"] += 1

                    if i not in posiciones_usadas[tamano_barco]["derecha"]:
                        posiciones_usadas[tamano_barco]["derecha"][i] = 0

            # ABAJO
            for j in range(len(datos["columnas"])):

                # PARA DESCARTAR COLUMNA 0 O QUE SEA MENOR AL BARCO
                if ( (datos["columnas"][j] == 0) or (datos["columnas"][j] < tamano_barco) ):
                    continue

                for i in range(len(datos["filas"])):

                    # PARA DESCARTAR FILA QUE SEA 0
                    if datos["filas"][i] == 0:
                        continue

                    # PARA DESCARTAR FILA EN DONDE EL BARCO NO ENTRA EN EL TABLERO
                    if len(datos["filas"]) < (i+tamano_barco):
                        continue

                    posiciones = []
                    hay_espacio = True
                    for y in range(tamano_barco):
                        if datos["filas"][i+y] < 1:
                            hay_espacio = False
                            break
                        posiciones.append(i+y)
                        
                    # HAY UN CERO UN MEDIO DE DONDE QUIERO PONER EL BARCO
                    if not hay_espacio:
                        continue

                    if j not in posibles_posiciones[tamano_barco]["abajo"]:
                        posibles_posiciones[tamano_barco]["abajo"][j] = []

                    posibles_posiciones[tamano_barco]["abajo"][j].append(posiciones)
                    posibles_posiciones[tamano_barco]["cantidad"] += 1

                    if j not in posiciones_usadas[tamano_barco]["abajo"]:
                        posiciones_usadas[tamano_barco]["abajo"][j] = 0

    return posibles_posiciones, posiciones_usadas




def tiene_adyacentes_libres_abajo(datos, tablero, x, y, tamano_barco):
    for i in range(tamano_barco):
        # IZQUIERDA
        if ( (y > 0) and (tablero[x+i][y-1]) ):
            return False

        # DERECHA
        if ( (y < len(datos["columnas"])-1) and (tablero[x+i][y+1]) ):
            return False
        
    # ARRIBA
    if ( (x > 0) and (tablero[x-1][y]) ):
            return False
    
    # ABAJO
    if ( (x+tamano_barco < len(datos["filas"])) and (tablero[x+tamano_barco][y]) ):
        return False
    
    # CORNER SUPERIOR IZQUIERDO
    if ((x > 0) and (y > 0) and (tablero[x-1][y-1]) ):
        return False
    
    # CORNER SUPERIOR DERECHO
    if ( (x > 0) and (y < len(datos["columnas"])-1) and (tablero[x-1][y+1]) ):
        return False
    
    # CORNER INFERIOR IZQUIERDO
    if ( (x+tamano_barco < len(datos["filas"])) and (y > 0) and (tablero[x+1][y-1]) ):
        return False
    
    # CORNER INFERIOR DERECHO
    if ( (x+tamano_barco < len(datos["filas"])) and (y < len(datos["columnas"])-1) and (tablero[x+1][y+1]) ):
        return False
    
    return True

def es_valida_posicion_abajo(datos, tablero, tamano_barco, y, valores_x):
    for x in valores_x:
        if datos["filas"][x] == 0:
            return False
        
        if tablero[x][y]:
            return False

    return tiene_adyacentes_libres_abajo(datos, tablero, valores_x[0], y, tamano_barco)

def poner_barco_abajo(datos, tablero, tamano_barco, y, valores_x, resultado_actual):
    for x in valores_x:
        tablero[x][y] = True
        datos["filas"][x] -= 1

    datos["columnas"][y] -= tamano_barco

    resultado_actual["cumplido"] += tamano_barco*2

    if tamano_barco == 1:
        resultado_actual["posiciones"].append([valores_x[0], y])
    else:
        resultado_actual["posiciones"].append([valores_x[0], y, valores_x[-1], y])

def sacar_barco_abajo(datos, tablero, tamano_barco, y, valores_x, resultado_actual):
    for x in valores_x:
        tablero[x][y] = False
        datos["filas"][x] += 1

    datos["columnas"][y] += tamano_barco

    resultado_actual["cumplido"] -= tamano_barco*2

    resultado_actual["posiciones"].pop()



def tiene_adyacentes_libres_derecha(datos, tablero, x, y, tamano_barco):
    for i in range(tamano_barco):
        # ARRIBA
        if ( (x > 0) and (tablero[x-1][y+i]) ):
            return False
        # ABAJO
        if ( (x < len(datos["filas"])-1) and (tablero[x+1][y+i]) ):
            return False
    
    # IZQUIERDA
    if ( (y > 0) and (tablero[x][y-1]) ):
        return False
    
    # DERECHA
    if ( (y+tamano_barco < len(datos["columnas"])) and (tablero[x][y+tamano_barco]) ):
        return False
    
    # CORNER SUPERIOR IZQUIERDO
    if ( (x > 0) and (y > 0) and (tablero[x-1][y-1]) ):
        return False
    
    # CORNER SUPERIOR DERECHO
    if ( (x > 0) and (y+tamano_barco < len(datos["columnas"])) and (tablero[x-1][y+tamano_barco]) ):
        return False
    
    # CORNER INFERIOR IZQUIERDO
    if ( (x < len(datos["filas"])-1) and (y > 0) and (tablero[x+1][y-1]) ):
        return False
    
    # CORNER INFERIOR DERECHO
    if ( (x < len(datos["filas"])-1) and (y+tamano_barco < len(datos["columnas"])) and (tablero[x+1][y+tamano_barco]) ):
        return False

    return True     

def es_valida_posicion_derecha(datos, tablero, tamano_barco, x, valores_y):
    for y in valores_y:
        if datos["columnas"][y] == 0:
            return False
        
        if tablero[x][y]:
            return False

    return tiene_adyacentes_libres_derecha(datos, tablero, x, valores_y[0], tamano_barco)

def sacar_barco_derecha(datos, tablero, tamano_barco, x, valores_y, resultado_actual):
    for y in valores_y:
        tablero[x][y] = False
        datos["columnas"][y] += 1

    datos["filas"][x] += tamano_barco

    resultado_actual["cumplido"] -= tamano_barco*2

    resultado_actual["posiciones"].pop()


def poner_barco_derecha(datos, tablero, tamano_barco, x, valores_y, resultado_actual):
    for y in valores_y:
        tablero[x][y] = True
        datos["columnas"][y] -= 1

    datos["filas"][x] -= tamano_barco

    resultado_actual["cumplido"] += tamano_barco*2

    if tamano_barco == 1:
        resultado_actual["posiciones"].append([x, valores_y[0]])
    else:
        resultado_actual["posiciones"].append([x, valores_y[0], x, valores_y[-1]])



def escribir_posiciones(indice, posiciones):
    if posiciones == [0]:
        print(f"{indice}: None")
    elif len(posiciones) == 2:
        print(f"{indice}: ({posiciones[0]}, {posiciones[1]})")
    else:
        print(f"{indice}: ({posiciones[0]}, {posiciones[1]}) - ({posiciones[2]}, {posiciones[3]})")

def crear_respuesta(resultado_final, barcos_sin_ordenar):
    indices_barcos = sorted(range(len(barcos_sin_ordenar)), key=lambda x: barcos_sin_ordenar[x], reverse=True)
    
    respuesta_barcos = []

    for i in range(len(indices_barcos)):
        respuesta_barcos.append([indices_barcos[i], resultado_final["posiciones"][i]])

    return respuesta_barcos

def imprimir_respuesta(datos, resultado_final, posiciones_barcos_originales):
    print("Posiciones:")
    for barco in posiciones_barcos_originales:
        escribir_posiciones(barco[0], barco[1])
    print("Demanda cumplida:", resultado_final["cumplido"])
    print("Demanda total:", datos["demanda_total"])



def modificar_tablero(datos, tablero, resultado_final, posiciones_barcos_originales):
    for i in range(len(resultado_final["posiciones"])):
        if resultado_final["posiciones"][i] == [0]:
            continue

        x = resultado_final["posiciones"][i][0]
        y = resultado_final["posiciones"][i][1]

        if len(resultado_final["posiciones"][i]) == 2:
            tablero[x][y] = posiciones_barcos_originales[i][0]
        else:
            if y == resultado_final["posiciones"][i][3]:
                for j in range(datos["barcos"][i]):
                    tablero[x+j][y] = posiciones_barcos_originales[i][0]
            else:
                for j in range(datos["barcos"][i]):
                    tablero[x][y+j] = posiciones_barcos_originales[i][0]

def imprimir_tablero(datos, tablero, resultado_final, posiciones_barcos_originales):
    modificar_tablero(datos, tablero, resultado_final, posiciones_barcos_originales)

    ancho_maximo = 5
    no_elemento = "-"

    print(" ---> TABLERO <--- ")
    for fila in tablero:
        print(''.join([(f"{no_elemento:<{ancho_maximo}}" if elemento == False else f"{elemento:<{ancho_maximo}}") for elemento in fila]))
    print()


def es_solucion(datos, resultado_final, resultado_actual):
    if resultado_final["cumplido"] < resultado_actual["cumplido"]:
        
        resultado_final["cumplido"] = resultado_actual["cumplido"]
        resultado_final["posiciones"] = resultado_actual["posiciones"].copy()

        if (resultado_final["cumplido"] == datos["demanda_total"]):
            return True
            
        if (resultado_final["cumplido"] == datos["maxima_demanda_posible"]):
            return True

    return False



def cortar_si_no_va_superar_resultado_final(datos, resultado_final, resultado_actual, indice_barco):
    resultado_posible = resultado_actual["cumplido"]
    for i in range(indice_barco, len(datos["barcos"])):
        resultado_posible += (datos["barcos"][i] * 2)

    return resultado_posible <= resultado_final["cumplido"]



def cumplir_maxima_demanda(datos, tablero, resultado_final, resultado_actual, indice_barco, posiciones_usadas):
    if len(resultado_actual["posiciones"]) == len(datos["barcos"]):
        return es_solucion(datos, resultado_final, resultado_actual)
    
    if cortar_si_no_va_superar_resultado_final(datos, resultado_final, resultado_actual, indice_barco):
        return False
    
    tamano_barco = datos["barcos"][indice_barco]

    if ( (indice_barco) and (tamano_barco != datos["barcos"][indice_barco-1]) ):
        for indice_x in posiciones_usadas[tamano_barco]["derecha"]:
            posiciones_usadas[tamano_barco]["derecha"][indice_x] = 0  

        for indice_y in posiciones_usadas[tamano_barco]["abajo"]:
            posiciones_usadas[tamano_barco]["abajo"][indice_y] = 0
    else:
        posiciones_usadas = copy.deepcopy(posiciones_usadas)

    i_inicial_derecha = posiciones_usadas[tamano_barco]["derecha"]
    i_inicial_abajo = posiciones_usadas[tamano_barco]["abajo"]

    if datos["posibles_posiciones"][tamano_barco]["derecha"]:
        for indice_x in datos["posibles_posiciones"][tamano_barco]["derecha"]:
            if datos["filas"][indice_x] < tamano_barco:
                continue

            for i in range(i_inicial_derecha[indice_x], len(datos["posibles_posiciones"][tamano_barco]["derecha"][indice_x])):
                posiciones_usadas[tamano_barco]["derecha"][indice_x] += 1

                valores_y = datos["posibles_posiciones"][tamano_barco]["derecha"][indice_x][i]

                if es_valida_posicion_derecha(datos, tablero, tamano_barco, indice_x, valores_y):
                    poner_barco_derecha(datos, tablero, tamano_barco, indice_x, valores_y, resultado_actual)
                    if cumplir_maxima_demanda(datos, tablero, resultado_final, resultado_actual, indice_barco+1, posiciones_usadas):
                        return True
                    sacar_barco_derecha(datos, tablero, tamano_barco, indice_x, valores_y, resultado_actual)

    if datos["posibles_posiciones"][tamano_barco]["abajo"]:
        for indice_y in datos["posibles_posiciones"][tamano_barco]["abajo"]:
            if datos["columnas"][indice_y] < tamano_barco:
                continue
            
            for i in range(i_inicial_abajo[indice_y], len(datos["posibles_posiciones"][tamano_barco]["abajo"][indice_y])):
                posiciones_usadas[tamano_barco]["abajo"][indice_y] += 1

                valores_x = datos["posibles_posiciones"][tamano_barco]["abajo"][indice_y][i]

                if es_valida_posicion_abajo(datos, tablero, tamano_barco, indice_y, valores_x):
                    poner_barco_abajo(datos, tablero, tamano_barco, indice_y, valores_x, resultado_actual)
                    if cumplir_maxima_demanda(datos, tablero, resultado_final, resultado_actual, indice_barco+1, posiciones_usadas):
                        return True
                    sacar_barco_abajo(datos, tablero, tamano_barco, indice_y, valores_x, resultado_actual)

    resultado_actual["posiciones"].append([0]) 
    if cumplir_maxima_demanda(datos, tablero, resultado_final, resultado_actual, indice_barco+1, posiciones_usadas):
        return True
    resultado_actual["posiciones"].pop()



if __name__ == "__main__":
    datos, barcos_sin_ordenar = obtener_datos(sys.argv[1])
    #datos, barcos_sin_ordenar = obtener_datos("parte_3/datos_parte_3/10_10_10.txt")

    tiempo_inicial = time.time()

    datos["barcos"] = sorted(barcos_sin_ordenar, reverse=True)
    datos["posibles_posiciones"], posiciones_usadas = generar_posibles_posiciones(datos)

    tablero = [[False for _ in range(len(datos["columnas"]))] for _ in range(len(datos["filas"]))]

    barcos_que_pueden_ponerse = {}
    barcos_que_no_pueden_ponerse = 0
    for barco in datos["posibles_posiciones"]:
        if datos["posibles_posiciones"][barco]["cantidad"] == 0:
            barcos_que_no_pueden_ponerse += datos["barcos"].count(barco)
        else:
            barcos_que_pueden_ponerse[barco] = 0

    resultado_final = {"cumplido": 0, "posiciones": [[0]]*barcos_que_no_pueden_ponerse}
    resultado_actual = {"cumplido": 0, "posiciones": [[0]]*barcos_que_no_pueden_ponerse}

    datos["demanda_total"] = sum(datos["filas"]) + sum(datos["columnas"])
    datos["maxima_demanda_posible"] = sum(datos["barcos"][barcos_que_no_pueden_ponerse:]) *2

    cumplir_maxima_demanda(datos, tablero, resultado_final, resultado_actual, barcos_que_no_pueden_ponerse, posiciones_usadas)

    posiciones_barcos_originales = crear_respuesta(resultado_final, barcos_sin_ordenar)
    imprimir_tablero(datos, tablero, resultado_final, posiciones_barcos_originales)
    posiciones_barcos_originales.sort(key=lambda x: x[0])
    imprimir_respuesta(datos, resultado_final, posiciones_barcos_originales)

    tiempo_final = time.time()
    print("Tiempo que tardo en correr --> {}".format(tiempo_final - tiempo_inicial))
