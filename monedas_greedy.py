

def elegir_sophia(monedas):
    if monedas[0] < monedas[-1]:
        return -1
    else:
        return 0


def elegir_mateo(monedas):
    if monedas[0] > monedas[-1]:
        return -1
    else:
        return 0


def monedas_greedy(monedas):
    monedas_sophia = []
    moneda_mateo = []

    while len(monedas) > 0:
        moneda_elegida = monedas.pop(elegir_sophia(monedas))
        monedas_sophia.append(moneda_elegida)
        if len(monedas) > 0:
            moneda_elegida = monedas.pop(elegir_mateo(monedas))
            moneda_mateo.append(moneda_elegida)

    return monedas_sophia, moneda_mateo
