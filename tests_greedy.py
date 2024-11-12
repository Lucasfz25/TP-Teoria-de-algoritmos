import unittest
import monedas_greedy as greedy


class TestsMonedasGreedy(unittest.TestCase):
    def test_20_elementos(self):
        monedas = [72,165,794,892,880,341,882,570,679,725,979,375,459,603,112,436,587,699,681,83]
        monedas_s = greedy.monedas_greedy(monedas)
        ganancia = sum(monedas_s)
        self.assertEqual(ganancia, 7165)
