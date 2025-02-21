import sys
import monedas_greedy

def obtener_datos(archivo_pruebas):
    with open(archivo_pruebas, 'r') as f:
        lineas = f.readlines()

    lista_monedas = []

    for linea in lineas[1].split(";"):
        if linea.isdigit():
            lista_monedas.append(int(linea))
        else:
            lista_monedas.append(int(linea[:-1]))

    return lista_monedas


if __name__ == "__main__":
    lista_monedas = obtener_datos(sys.argv[1])

    total_sophia, total_mateo, todas_elecciones = monedas_greedy.monedas_greedy(lista_monedas)

    monedas_greedy.imprimir_datos(total_sophia, todas_elecciones)
    