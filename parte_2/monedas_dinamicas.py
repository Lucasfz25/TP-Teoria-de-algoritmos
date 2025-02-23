def imprimir_resultado(valor_acumulado_sophia, turnos, valor_acumulado_mateo, monedas):
    i, j = 0, len(monedas)-1
    jugadores = ("Sophia", "Mateo")

    for x in range(len(turnos)):
        if turnos[x] == 0:
            print(f"{jugadores[x%2]} debe agarrar la primera ({monedas[i]})", end="; ")
            i += 1
        else:
            print(f"{jugadores[x%2]} debe agarrar la ultima ({monedas[j]})", end="; ")
            j -= 1

    print()
    print(f"Ganancia Sophia: {valor_acumulado_sophia}")
    print(f"Ganancia Mateo: {valor_acumulado_mateo}")

def indices_luego_turno_mateo(monedas, i, j, turnos_actuales, turno_actual):
    if monedas[i] >= monedas[j]:
        turnos_actuales[turno_actual] = 0
        return (i+1, j)
    turnos_actuales[turno_actual] = -1
    return (i, j-1)


def valor_acumulado_mas_alto(monedas, i, j, datos, turno_actual):
    if j == i-1:
        return 0, {}
    
    if i == j:
        return monedas[i], {turno_actual: 0}
    
    if (i, j) in datos:
        return datos[(i, j)]["valor"], datos[(i, j)]["turnos"]
    
    turnos_primeros_actuales = {turno_actual: 0}
    i_luego_mateo, j_luego_mateo = indices_luego_turno_mateo(monedas, i+1, j, turnos_primeros_actuales, turno_actual+1)
    valor_acumulado, turnos_primeros_todos = valor_acumulado_mas_alto(monedas, i_luego_mateo, j_luego_mateo, datos, turno_actual+2)
    primero = monedas[i] + valor_acumulado

    turnos_ultimos_actuales = {turno_actual: -1}
    i_luego_mateo, j_luego_mateo = indices_luego_turno_mateo(monedas, i, j-1, turnos_ultimos_actuales, turno_actual+1)
    valor_acumulado, turnos_ultimos_todos = valor_acumulado_mas_alto(monedas, i_luego_mateo, j_luego_mateo, datos, turno_actual+2)
    ultimo = monedas[j] + valor_acumulado

    datos[(i, j)] = {}

    if primero >= ultimo:
        datos[(i, j)]["valor"] = primero
        turnos_finales = {**turnos_primeros_actuales, **turnos_primeros_todos}
    else:
        datos[(i, j)]["valor"] = ultimo
        turnos_finales = {**turnos_ultimos_actuales, **turnos_ultimos_todos}

    datos[(i, j)]["turnos"] = turnos_finales

    return datos[(i, j)]["valor"], turnos_finales



def monedas_dinamicas(monedas):
    datos = {}
    turno_actual = 0

    valor_acumulado_sophia, turnos = valor_acumulado_mas_alto(monedas, 0, len(monedas)-1, datos, turno_actual)
    valor_acumulado_mateo = sum(monedas) - valor_acumulado_sophia

    return valor_acumulado_sophia, turnos, valor_acumulado_mateo

