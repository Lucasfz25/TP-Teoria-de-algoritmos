"""
1)Tablero n x m (n filas por n columnas)

2)Lista de k barcos (el barco i tien bi de largo)

3)Lista de restricciones para las filas: la fila i tiene el numero
de casilleros a ocupar en la misma (ni mas ni menos)

4)Lista de restricciones para las columnas: simil filas ,
pero para las columnas

5)La posicion de los k barcos: una lista de listas, donde cada 
sub-lista son las posiciones de lo barcos (sub-lista de tuplas (x,y))


cada posicion i de esta lista representa las posiciones del barco i
ubicacion_barcos = [[(),(),...,()],
                    [(),(),...,()],
                    ...,
                    [(),(),...,()]]
"""

def verificador_de_solucion(tablero,longitud_barcos,restricciones_filas,restricciones_columnas,
                ubicacion_barcos):

    n = len(tablero) ## cantidad de filas del tablero 
    m = len(tablero[1]) ##cantidad de columnas del tablero
    k = len(longitud_barcos) ##cantidad de barcos que deber haber en el tablero

    if not es_valida_la_lista_ubicacion_barcos(n,m,longitud_barcos,k,ubicacion_barcos):
        return False

    ## Colocamos lo barcos en tablero 
    id_barco = 0
    for posiciones_de_barco in ubicacion_barcos:
        
        for (f,c) in posiciones_de_barco:
            tablero[f][c] = id_barco
        
        id_barco += 1
    ####

    if not se_cumplen_requisitos_consumo_filas_y_columnas(tablero,n,m,restricciones_filas,restricciones_columnas):
        return False
    
    if hay_barcos_adyacentes(tablero,n,m,ubicacion_barcos,k):
        return False
    
    return True


def es_valida_la_lista_ubicacion_barcos(n,m,longitud_barcos,k,ubicacion_barcos):

    if len(ubicacion_barcos) != k:
        return False
    
    for i in range(0,k):
        posiciones_de_barco = ubicacion_barcos[i]
        if len(posiciones_de_barco) != longitud_barcos[i]:
            return False
        
        for (f,c) in posiciones_de_barco:

            if not (0 <= f <= n-1) or not (0 <= c <= m-1):
                return False
    
    return las_posiciones_de_cada_barco_son_verticales_u_horizontales(ubicacion_barcos)

def las_posiciones_de_cada_barco_son_verticales_u_horizontales(ubicacion_barcos):

    for posiciones_de_barco in ubicacion_barcos:
        if not barco_esta_posicionado_de_forma_vertical(posiciones_de_barco) and \
        not barco_esta_posicionado_de_forma_horizontal(posiciones_de_barco):
            return False
    return True


def barco_esta_posicionado_de_forma_vertical(posiciones_de_barco):

    pos_columna = posiciones_de_barco[0][1]
    for i in range(1,len(posiciones_de_barco)):
        _,c = posiciones_de_barco[i]
        if c != pos_columna:
            return False
    return True

def barco_esta_posicionado_de_forma_horizontal(posiciones_de_barco):

    pos_fila = posiciones_de_barco[0][0]
    for i in range(1,len(posiciones_de_barco)):
        f,_ = posiciones_de_barco[i]
        if f != pos_fila:
            return False
    return True


def se_cumplen_requisitos_consumo_filas_y_columnas(tablero,n,m,restricciones_filas,restricciones_columnas):

    return se_cumplen_requisitos_consumo_filas(tablero,n,restricciones_filas) and \
    se_cumplen_requisitos_consumos_columnas(tablero,n,m,restricciones_columnas)
    

def se_cumplen_requisitos_consumo_filas(tablero,n,restricciones_filas):

    cant_elementos_en_fila = 0
    for f in range(0,n):
        fila = tablero[f]
        for elemento in fila:
            if elemento != None:
                cant_elementos_en_fila += 1

        if cant_elementos_en_fila != restricciones_filas[f]:
            return False
        
        cant_elementos_en_fila = 0
    
    return True

def se_cumplen_requisitos_consumos_columnas(tablero,n,m,restricciones_columnas):


    cant_elementos_en_columna = 0

    for c in range(0,m):
        for f in range(0,n):

            elemento = tablero[f][c]
            if elemento != None:
                cant_elementos_en_columna += 1
        
        if cant_elementos_en_columna != restricciones_columnas[c]:
            return False
        
        cant_elementos_en_columna = 0
    
    return True


def hay_barcos_adyacentes(tablero,n,m,ubicacion_barcos,k):

    id_barco = 0
    for posiciones_de_barco in ubicacion_barcos:
        for (f,c) in posiciones_de_barco:
            
            for i in range(-1,2):
                for j in range(-1,2):
                    
                    offset_f = f+i
                    offset_c = c+j

                    if offset_f == f and offset_c == c:
                        continue
                    
                    if posicion_de_desplazamiento_hay_posicion_de_otro_barco(tablero,n,m,offset_f,offset_c,id_barco):
                        return True
        id_barco += 1
    return False


def posicion_de_desplazamiento_hay_posicion_de_otro_barco(tablero,n,m,offset_f,offset_c,id_barco):
    
    ultima_pos_de_fila = n-1
    ultima_pos_de_columna = m-1

    if 0 <= offset_f <= ultima_pos_de_fila:
        if 0 <= offset_c <= ultima_pos_de_columna:
            return tablero[offset_f][offset_c] != None and tablero[offset_f][offset_c] != id_barco
                ##return True
            ##return False
        return False
    return False

###Este seria el tablero con las ubicaciones de los barcos que se muestra en imagen en el tp3
tablero = [[None for _ in range(10)] for _ in range(10)]
longitud_barcos =  [3,1,1,2,4,2,1,3,1,2]
restricciones_filas = [3,2,2,4,2,1,1,2,3,0]
restricciones_columnas = [1,2,1,3,2,2,3,1,5,0]
ubicacion_barcos = [[(0,4),(0,5),(0,6)],
                    [(1,0)],
                    [(1,8)],
                    [(2,2),(2,3)],
                    [(3,5),(3,6),(3,7),(3,8)],
                    [(4,1),(5,1)],
                    [(4,3)],
                    [(6,8),(7,8),(8,8)],
                    [(7,6)],
                    [(8,3),(8,4)]]

print(verificador_de_solucion(tablero,longitud_barcos,restricciones_filas,restricciones_columnas,ubicacion_barcos))
