from collections import deque

def elecciones(monedas, elecciones, turno_sophia):
    if (len(monedas) == 0) or (turno_sophia and monedas[0] > monedas[-1]) or (not turno_sophia and monedas[0] < monedas[-1]):
        elecciones.append(True)
        return monedas.popleft()
    else:
        elecciones.append(False)
        return monedas.pop()
    
def imprimir_datos(total_sophia, todas_elecciones):
    jugadores = ["Sophia", "Mateo"]
    for i in range(len(todas_elecciones)):
        if todas_elecciones[i]:
            print(f"Primera moneda para {jugadores[i%2]};", end=" ")
        else:
            print(f"Ultima moneda para {jugadores[i%2]};", end=" ")
    print()
    print(f"Ganancia de Sophia: {total_sophia}")

def monedas_greedy(monedas):
    total_sophia = 0
    total_mateo = 0
    todas_elecciones = []
    turno_de_sophia = True

    monedas = deque(monedas)

    while len(monedas) > 0:
        if turno_de_sophia:
            total_sophia += elecciones(monedas, todas_elecciones, turno_de_sophia)
        else:
            total_mateo += elecciones(monedas, todas_elecciones, turno_de_sophia)

        turno_de_sophia = not turno_de_sophia
        
    return total_sophia, total_mateo, todas_elecciones