import unittest
import monedas_dinamicas as din


class TestsMonedasDinamicas(unittest.TestCase):
    def test_5_elementos(self):
        monedas = [96, 594, 437, 674, 950]
        ganancia = din.monedas_dinamicas(monedas)
        self.assertEqual(ganancia, 1483)

    def test_20_elementos(self):
        monedas = [455, 852, 725, 410, 835, 239, 404, 462, 629, 587, 171, 604, 826, 838, 384, 336, 21, 125, 378, 217]
        ganancia = din.monedas_dinamicas(monedas)
        self.assertEqual(ganancia, 5234)

    def test_1000_elementos(self):
        monedas = [1050, 2603, 2312, 95, 3637, 212, 2742, 1402, 3761, 4347, 3760, 322, 991, 910, 4041, 4773, 2002, 1420,
                   2277, 1523, 1028, 1174, 1878, 3247, 3092, 4100, 4960, 2039, 4229, 862, 4897, 1245, 3654, 2114, 3339,
                   325, 4805, 2605, 1052, 4876, 2489, 1812, 563, 1736, 4560, 1339, 4277, 286, 4462, 231, 393, 380, 1529,
                   1116, 1366, 3115, 818, 3826, 4868, 2805, 2403, 3820, 4870, 992, 2723, 3636, 621, 3746, 1546, 3401,
                   4843, 2217, 2598, 3613, 2840, 1172, 1808, 4050, 3449, 371, 2207, 731, 1654, 4978, 60, 3597, 1303,
                   3704, 4605, 2282, 3546, 3448, 686, 4162, 3259, 1454, 262, 360, 21, 1754, 4898, 2354, 2555, 2994,
                   3093, 1987, 1766, 4716, 29, 374, 4333, 4323, 3431, 2113, 2273, 3717, 3452, 728, 2668, 3384, 1457,
                   134, 354, 3649, 2696, 4425, 990, 1019, 2895, 677, 3618, 873, 2102, 4688, 2241, 4753, 2091, 2084, 882,
                   629, 2095, 2944, 3423, 3768, 3788, 1826, 1486, 1021, 2392, 4092, 2410, 1090, 329, 4609, 4855, 397,
                   3561, 259, 3473, 156, 1898, 1039, 2292, 4530, 637, 562, 38, 3553, 1414, 290, 199, 3521, 590, 4200,
                   1470, 4743, 4020, 4638, 831, 3740, 2056, 1994, 3557, 3064, 2451, 3668, 2144, 765, 1207, 1843, 2683,
                   2427, 3132, 2560, 4791, 4051, 23, 4138, 1814, 694, 3286, 1509, 4232, 295, 301, 3610, 4879, 3705,
                   2557, 303, 488, 3414, 4687, 2458, 859, 3560, 2702, 2879, 2528, 3142, 1228, 3863, 2249, 2181, 3998,
                   207, 56, 4693, 398, 1347, 1371, 294, 4807, 665, 217, 201, 1219, 680, 3209, 1582, 2872, 345, 4971,
                   4759, 4499, 2388, 3907, 3181, 3484, 1574, 289, 834, 2184, 4989, 978, 4153, 2382, 3457, 979, 2989,
                   1841, 4975, 3210, 2934, 2956, 4663, 3138, 293, 4915, 3537, 2651, 285, 1737, 2942, 1062, 1458, 4547,
                   1730, 756, 719, 464, 843, 1963, 1053, 1281, 3680, 4676, 826, 1208, 2491, 4363, 1765, 2373, 2716,
                   1517, 1748, 3769, 3069, 3865, 578, 4604, 132, 549, 241, 1215, 4728, 2390, 836, 2827, 3232, 4945,
                   3078, 3951, 4696, 4080, 940, 3735, 844, 3810, 691, 2220, 3230, 1070, 284, 417, 2769, 713, 2576, 2675,
                   2588, 1891, 3650, 1982, 2093, 1252, 4864, 1221, 4244, 689, 65, 105, 3497, 4800, 1859, 564, 2182,
                   4346, 4213, 3282, 3663, 4268, 593, 147, 2159, 3574, 646, 2021, 1658, 2176, 2167, 119, 2293, 4603,
                   872, 2454, 4771, 3819, 3067, 2336, 4161, 59, 1989, 4598, 2377, 1769, 3372, 3494, 4185, 1964, 4830,
                   1893, 1103, 1346, 99, 4093, 3665, 2930, 681, 908, 2878, 2839, 4916, 1315, 994, 1181, 3515, 2203,
                   1134, 1057, 4913, 1256, 4719, 1558, 1958, 2389, 880, 4128, 335, 2796, 1297, 2925, 1224, 1452, 3774,
                   466, 3174, 1080, 1669, 3407, 4673, 3815, 1059, 244, 3355, 3554, 1744, 4990, 4613, 2177, 3753, 1502,
                   3410, 2235, 1328, 15, 4940, 2550, 287, 2474, 2483, 2078, 496, 2395, 4003, 1966, 2593, 1997, 2487,
                   3582, 4116, 4643, 4396, 4354, 2362, 4536, 3600, 1614, 2165, 4944, 2173, 166, 3284, 2157, 4488, 4752,
                   2874, 2771, 4980, 605, 2399, 2587, 2652, 310, 1058, 3312, 3280, 1466, 476, 2343, 82, 174, 514, 3365,
                   658, 337, 714, 2214, 1613, 1388, 1950, 625, 3583, 1533, 408, 537, 3870, 3507, 4901, 89, 2725, 4563,
                   1386, 2706, 214, 1926, 1742, 4769, 3771, 1757, 3990, 4452, 1043, 4540, 3831, 4110, 1626, 1494, 3333,
                   1406, 1666, 3786, 2661, 430, 3034, 4930, 467, 3873, 3876, 2700, 3070, 4760, 3796, 4028, 4340, 2116,
                   1799, 1515, 4500, 4282, 218, 1842, 4238, 4419, 3855, 1382, 4165, 3840, 356, 4507, 1741, 1178, 4447,
                   672, 1560, 888, 1768, 1299, 3962, 1865, 3053, 2314, 3222, 2361, 1391, 4160, 4371, 487, 1074, 4025,
                   3400, 4948, 3013, 961, 3178, 170, 3197, 4439, 4664, 1487, 1131, 1240, 1194, 3261, 4508, 1909, 1638,
                   1821, 4880, 3158, 2785, 4015, 1894, 1010, 3341, 573, 2607, 2873, 4270, 93, 178, 138, 1789, 3737, 784,
                   1474, 2532, 2561, 3014, 1241, 379, 3156, 1450, 4265, 4568, 2899, 4002, 4552, 4633, 748, 361, 462,
                   3603, 1688, 988, 1047, 2724, 4838, 248, 4366, 1606, 2968, 1108, 3357, 4682, 4390, 4968, 3466, 1112,
                   1442, 3278, 1864, 2778, 4427, 165, 785, 3151, 2662, 3789, 3241, 671, 4085, 3830, 4227, 4486, 3445,
                   4826, 1511, 2547, 1046, 42, 1772, 4487, 2120, 3021, 1911, 3872, 4088, 3630, 2309, 4639, 1399, 2673,
                   1955, 3689, 1431, 1493, 2228, 3143, 2149, 3928, 1783, 3926, 4907, 3036, 1020, 2816, 2686, 159, 2937,
                   3937, 3008, 2729, 565, 3169, 4306, 3188, 3817, 3137, 1583, 1513, 2456, 3711, 4813, 150, 1568, 4810,
                   4326, 4228, 3846, 2334, 4320, 2190, 127, 3752, 482, 688, 955, 520, 3056, 2251, 1146, 2132, 1083, 460,
                   2986, 4802, 1337, 2633, 1973, 4908, 2401, 1323, 4545, 4597, 3374, 3608, 2744, 2617, 608, 3268, 3383,
                   2230, 682, 1791, 4249, 1694, 3050, 407, 1897, 363, 5000, 3001, 3808, 444, 1125, 4591, 4770, 2019,
                   3736, 1528, 2253, 4721, 1301, 135, 1942, 2558, 1892, 740, 4477, 3896, 1804, 1810, 3237, 2854, 822,
                   3807, 3411, 3071, 4336, 272, 527, 3321, 652, 904, 1063, 2851, 3950, 2193, 2975, 1981, 3349, 252, 806,
                   1309, 4231, 2833, 980, 2597, 25, 2979, 1485, 1415, 220, 308, 1790, 4275, 3982, 1489, 4159, 85, 4732,
                   4849, 909, 989, 2270, 63, 1354, 2201, 1032, 1145, 2226, 779, 2875, 4661, 823, 1618, 943, 2126, 1627,
                   362, 4739, 3890, 499, 754, 4782, 4375, 1065, 1882, 685, 4883, 4101, 1761, 447, 1847, 894, 2297, 130,
                   661, 1996, 3309, 773, 3923, 2003, 3925, 2936, 240, 770, 2689, 3205, 2761, 386, 2965, 981, 525, 4009,
                   2017, 535, 4254, 2464, 1871, 2809, 4191, 229, 409, 490, 3671, 4226, 2123, 2776, 226, 3722, 441, 1883,
                   1041, 1373, 824, 175, 4446, 842, 4850, 1679, 2494, 291, 4473, 1701, 111, 695, 2513, 4355, 1631, 846,
                   3160, 3295, 3200, 2653, 2122, 1541, 1425, 3579, 739, 963, 3304, 3201, 4059, 2378, 2890, 1313, 4584,
                   1427, 4130, 2086, 1130, 4369, 4496, 2885, 2698, 2783, 3589, 3842, 2332, 1756, 642, 2462, 2511, 1360,
                   3204, 4866, 2520, 3291, 4280, 1175, 49, 120, 1499, 4768, 2375, 3198, 223, 4445, 4727, 3894, 3149,
                   3350, 4203, 3787, 3898, 4734, 1310, 4816, 4579, 121, 1900, 2951, 1977, 2081, 2842, 4258, 2468, 897,
                   3183, 809, 3408, 557, 3127, 3829, 2444, 34, 660, 1520, 1559, 4386, 1005, 4482, 2281, 128, 4917, 2650,
                   4048, 3660, 2757, 2799, 3524, 1775, 4701, 4856, 4456, 1068, 4853, 2943, 4177]
        ganancia = din.monedas_dinamicas(monedas)
        self.assertEqual(ganancia, 1401590)



