import unittest
import naval_jj as jj


def generar_tablero(f, c):
    arr = [None] * c
    tablero = []
    for i in range(f):
        tablero.append(arr.copy())
    return tablero

class TestSolucionJJ(unittest.TestCase):

    def test_5x5(self):
        restricciones_f = [3, 3, 0, 1, 1]
        restricciones_c = [3, 1, 0, 3, 3]
        barcos = [1, 2, 2, 2, 2, 1]
        tablero = generar_tablero(len(restricciones_f), len(restricciones_c))
        solucion, dc, dt = jj.solucion_naval_jj(tablero, barcos, restricciones_f, restricciones_c)
        self.assertEqual(dc, 12)
        self.assertEqual(dt, 18)

    def test_8x7(self):
        restricciones_f = [1, 4, 4, 4, 3, 3, 4, 4]
        restricciones_c = [6, 5, 3, 0, 6, 3, 3]
        barcos = [2, 1, 2, 2, 1, 3, 2, 7, 7, 7]
        tablero = generar_tablero(len(restricciones_f), len(restricciones_c))
        solucion, dc, dt = jj.solucion_naval_jj(tablero, barcos, restricciones_f, restricciones_c)
        self.assertEqual(dc, 26)
        self.assertEqual(dt, 53)

if __name__ == '__main__':
    unittest.main()