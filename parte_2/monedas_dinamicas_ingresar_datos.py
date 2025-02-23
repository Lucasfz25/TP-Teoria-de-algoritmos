import sys
import monedas_dinamicas

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

    valor_acumulado_sophia, turnos, valor_acumulado_mateo = monedas_dinamicas.monedas_dinamicas(lista_monedas)
    monedas_dinamicas.imprimir_resultado(valor_acumulado_sophia, turnos, valor_acumulado_mateo, lista_monedas)