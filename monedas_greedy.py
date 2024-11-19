

def elegir_sophia(monedas, decisiones):
    if monedas[0] < monedas[-1] or len(monedas)==1:
        decisiones.append("Última moneda para Sophia")
        return -1
    else:
        decisiones.append("Primera moneda para Sophia")
        return 0


def elegir_mateo(monedas, decisiones):
    if monedas[0] > monedas[-1] or len(monedas)==1:
        decisiones.append("Última moneda para Mateo")
        return -1
    else:
        decisiones.append("Primera moneda para Mateo")
        return 0


def monedas_greedy(monedas):
    monedas_sophia = []
    monedas_mateo = []
    decisiones = []

    while len(monedas) > 0:
        moneda_elegida = monedas.pop(elegir_sophia(monedas, decisiones))
        monedas_sophia.append(moneda_elegida)
        if len(monedas) > 0:
            moneda_elegida = monedas.pop(elegir_mateo(monedas, decisiones))
            monedas_mateo.append(moneda_elegida)

    return decisiones, monedas_sophia, monedas_mateo
