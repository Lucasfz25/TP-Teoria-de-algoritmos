import unittest
import monedas_greedy as greedy

class TestsMonedasGreedy(unittest.TestCase):
    def test_una_moneda(self):
        monedas = [5]
        decisiones, s, _ = greedy.monedas_greedy(monedas)
        self.assertEqual(sum(s), 5)
        self.assertEqual(decisiones, ["Última moneda para Sophia"])

    def test_lista_ordenada(self):
        monedas = [72,165,794,892,880,341,882,570,679,725,979,375,459,603,112,436,587,699,681,83]
        m_asc = sorted(monedas)
        m_dec = sorted(monedas, reverse=True)
        _, s_asc, m_asc = greedy.monedas_greedy(m_asc)
        _, s_dec, m_dec = greedy.monedas_greedy(m_dec)
        self.assertGreater(sum(s_asc), sum(m_asc))
        self.assertGreater(sum(s_dec), sum(m_dec))

    def test_valores_iguales_par(self):
        monedas = [5,5,5,5,5,5,5,5,5,5]
        _, s, m = greedy.monedas_greedy(monedas)
        self.assertEqual(sum(s), sum(m))

    def test_valores_alternados(self):
        monedas = [1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10]
        _, s, m = greedy.monedas_greedy(monedas)
        self.assertGreater(sum(s), sum(m))

    def test_lista_simetrica(self):
        monedas = [5,4,3,2,1,2,3,4,5]
        _, s, m = greedy.monedas_greedy(monedas)
        self.assertGreater(sum(s), sum(m))

    def test_20_elementos(self):
        monedas = [72,165,794,892,880,341,882,570,679,725,979,375,459,603,112,436,587,699,681,83]
        decisiones_esperadas = ["Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo"]
        decisiones, monedas_s, monedas_m = greedy.monedas_greedy(monedas)
        ganancia = sum(monedas_s)
        self.assertEqual(ganancia, 7165)
        self.assertEqual(decisiones, decisiones_esperadas)
    def test_1000_elementos(self):
        monedas = [79,755,257,648,721,209,542,766,864,687,957,461,484,122,604,498,572,181,967,521,642,357,47,861,440,890,969,663,63,200,983,58,228,252,895,253,44,453,432,759,765,424,352,298,256,295,229,847,17,768,605,925,728,851,679,865,734,483,204,666,240,560,936,120,431,686,530,781,733,207,491,513,988,345,465,447,897,118,744,796,80,342,517,364,411,827,887,897,911,327,315,476,816,860,365,261,433,122,826,32,297,106,127,659,90,151,667,759,415,754,259,66,43,931,390,542,777,998,333,638,987,674,341,829,994,710,13,904,600,710,722,334,434,157,796,81,477,420,318,863,27,59,532,710,975,722,815,302,53,578,505,314,888,129,313,179,656,798,390,198,980,133,879,851,797,848,573,667,722,477,360,341,790,760,746,61,613,317,350,210,484,741,467,457,860,214,128,745,158,578,746,219,707,190,411,707,666,724,324,351,893,949,744,83,290,970,919,662,544,22,658,955,485,680,539,310,542,758,693,969,582,822,438,719,528,533,884,726,337,826,53,244,737,986,120,151,920,962,461,196,927,575,722,362,699,30,941,680,351,748,407,657,932,843,476,828,703,172,430,990,665,303,549,979,939,228,26,846,864,57,624,542,387,995,233,482,963,795,365,899,142,931,776,135,455,572,950,721,820,939,597,86,661,959,574,151,901,388,590,86,853,994,142,428,492,854,925,812,911,866,182,75,553,955,800,501,565,490,585,303,823,778,68,651,562,521,898,722,274,81,425,932,156,191,376,406,522,701,657,62,290,903,243,617,78,849,550,875,985,243,11,385,829,122,155,870,879,888,325,222,764,865,168,568,717,752,682,139,377,678,169,548,110,827,294,915,966,15,46,26,138,433,553,559,192,798,400,889,293,847,425,715,377,847,831,275,343,353,524,892,413,473,926,230,910,427,445,859,623,404,77,502,806,433,309,131,743,368,75,262,401,361,825,632,964,422,14,613,384,936,393,153,368,542,307,54,455,231,276,16,457,65,115,408,186,854,282,379,367,907,451,124,964,234,225,826,269,900,89,696,286,533,398,925,236,118,701,667,682,787,330,46,669,137,274,554,363,535,70,576,590,846,484,12,671,184,94,623,373,786,67,936,609,180,443,927,42,701,648,407,153,73,998,852,635,302,678,998,593,700,891,339,725,279,873,574,703,54,704,788,611,599,457,816,784,358,717,130,216,384,966,952,874,203,407,479,217,32,582,714,121,776,371,279,106,547,185,10,141,300,295,991,218,998,887,635,170,246,745,896,657,238,584,356,865,168,950,362,543,558,316,140,837,439,219,711,454,464,428,215,545,409,437,659,424,597,270,991,650,258,529,252,58,654,167,426,29,257,748,70,168,576,775,340,213,882,158,799,353,351,398,684,967,183,914,747,442,596,506,260,210,773,95,413,106,36,165,409,51,635,343,699,95,931,101,986,468,775,44,996,538,107,267,911,845,560,540,127,819,368,492,543,906,326,384,342,513,229,39,333,899,122,557,798,51,609,408,992,164,467,548,671,363,41,45,419,876,351,972,787,118,581,372,551,543,896,241,320,925,724,551,207,666,343,975,531,349,420,104,581,14,170,878,907,647,905,118,138,587,204,486,504,308,446,21,214,531,29,34,639,506,10,229,734,773,639,986,63,740,408,65,821,458,705,749,326,313,521,558,183,322,626,799,950,191,366,104,822,862,576,613,400,224,229,680,112,782,355,625,429,913,281,649,103,479,402,890,128,600,159,687,497,858,942,96,566,898,76,914,984,313,257,708,122,302,111,567,309,671,658,181,512,458,17,271,336,466,457,458,633,536,156,501,858,910,702,962,920,463,450,625,58,360,405,196,419,59,459,268,54,98,841,268,521,439,876,17,99,430,315,54,242,611,835,548,258,82,182,784,243,152,124,830,630,553,451,494,823,712,937,661,714,343,234,730,587,403,485,949,592,51,935,362,770,812,461,775,751,678,909,721,75,225,131,632,661,574,35,599,703,519,216,954,284,950,416,194,262,96,678,216,824,354,215,546,482,791,830,474,402,968,240,909,781,408,839,357,732,629,670,517,197,515,408,872,535,862,410,585,964,334,923,155,642,97,750,668,275,442,303,85,805,453,814,216,51,606,743,906,353,590,978,215,979,702,650,541,284,921,848,568,906,413,919,147,644,307,54,629,208,89,136,549,439,819,352,665,544,152,744,674,140,890,945,113,811,873,10,384,345,944,998,530,35,777,17,74,239,915,665,373,447,87,974,20,854,798,691,67,426]

        decisiones_esperadas = ["Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo", "Primera moneda para Sophia", "Primera moneda para Mateo", "Última moneda para Sophia", "Última moneda para Mateo"]

        decisiones, monedas_s, monedas_m = greedy.monedas_greedy(monedas)
        ganancia_s, ganancia_m = sum(monedas_s), sum(monedas_m)
        self.assertGreaterEqual(ganancia_s, ganancia_m)
        self.assertEqual(decisiones, decisiones_esperadas)