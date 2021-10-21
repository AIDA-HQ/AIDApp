import numpy as np
from shapely.geometry.linestring import LineString


class Coords:
    x_ADRS_meters = np.array(
        [
            0,
            0.000130495,
            0.00013648,
            0.000143405,
            0.000150536,
            0.000157876,
            0.000165426,
            0.000174944,
            0.000183875,
            0.000194012,
            0.000205447,
            0.000217281,
            0.000230558,
            0.000244317,
            0.000260801,
            0.000277946,
            0.000295764,
            0.000316783,
            0.000340014,
            0.000365642,
            0.000393872,
            0.00042644,
            0.000443327,
            0.000462218,
            0.000481601,
            0.000501481,
            0.000523587,
            0.000548063,
            0.00057324,
            0.000599128,
            0.000627665,
            0.000659028,
            0.000691355,
            0.000726777,
            0.000765505,
            0.000807768,
            0.000851474,
            0.000899062,
            0.000950806,
            0.001006997,
            0.00107065,
            0.001136799,
            0.001193866,
            0.001252723,
            0.001313399,
            0.001407876,
            0.001473206,
            0.001574787,
            0.001644937,
            0.001753863,
            0.001867309,
            0.001985368,
            0.002108124,
            0.002279251,
            0.002413302,
            0.002599804,
            0.002795375,
            0.003000219,
            0.003269634,
            0.003496096,
            0.003793177,
            0.004103694,
            0.004353103,
            0.004714636,
            0.005035998,
            0.00542431,
            0.005885753,
            0.006123538,
            0.006366031,
            0.006675769,
            0.006928856,
            0.007251837,
            0.007582175,
            0.007988292,
            0.008334815,
            0.008760355,
            0.00919649,
            0.009643218,
            0.010177792,
            0.010726786,
            0.011371864,
            0.012035777,
            0.012718525,
            0.013509128,
            0.014323569,
            0.015351369,
            0.016316633,
            0.017513795,
            0.018753335,
            0.020143991,
            0.021810395,
            0.023543014,
            0.025586694,
            0.027843292,
            0.030462452,
            0.033339262,
            0.035868224,
            0.037733321,
            0.039885461,
            0.042181,
            0.04483526,
            0.04784821,
            0.051219748,
            0.055165215,
            0.059756447,
            0.065208334,
            0.071736448,
            0.075323192,
            0.079627308,
            0.084648768,
            0.089670327,
            0.095409423,
            0.102583152,
            0.110474122,
            0.119799644,
            0.130560199,
            0.143472399,
            0.159254616,
            0.173876874,
            0.173876775,
            0.173877205,
            0.173876191,
        ]
    )

    y_ADRS_meters = np.array(
        [
            2.37541302,
            3.22114293,
            3.23805537,
            3.25708677,
            3.27610836,
            3.29513976,
            3.31417116,
            3.33743067,
            3.35857122,
            3.38183073,
            3.40719939,
            3.43256805,
            3.46005567,
            3.48754329,
            3.51925902,
            3.55097475,
            3.58269048,
            3.61863432,
            3.65668731,
            3.69685926,
            3.73915017,
            3.78566919,
            3.80891889,
            3.83429736,
            3.85966602,
            3.88503468,
            3.9125223,
            3.94212888,
            3.97172565,
            4.00132242,
            4.03303815,
            4.06687284,
            4.10069772,
            4.13664156,
            4.17470436,
            4.21487631,
            4.25504826,
            4.29732936,
            4.34172942,
            4.38824844,
            4.43899557,
            4.48973289,
            4.5320238,
            4.5743049,
            4.61659581,
            4.68002727,
            4.72230837,
            4.78573983,
            4.82803074,
            4.8914622,
            4.95488385,
            5.01831531,
            5.08174677,
            5.16631878,
            5.22975024,
            5.31432225,
            5.39889426,
            5.48346627,
            5.58918864,
            5.67376065,
            5.77947321,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.81137533,
            5.66639334,
            5.38629822,
            5.09567697,
            4.81835808,
            4.53311271,
            4.24767114,
            3.96805671,
            3.68425341,
            3.40119567,
            3.11682339,
            2.83319667,
            2.69827974,
            2.55242466,
            2.40100731,
            2.26655145,
            2.13022188,
            1.98125703,
            1.83973797,
            1.69652178,
            1.55669985,
            1.41659343,
            1.27621233,
            1.09874943,
            0.83954961,
            0.61928568,
            0.42919731,
        ]
    )

    x_K1_eff = np.array(
        [
            0,
            0.000130495,
            0.00013648,
            0.000143405,
            0.000150536,
            0.000157876,
            0.000165426,
            0.000174944,
            0.000183875,
            0.000194012,
            0.000205447,
            0.000217281,
            0.000230558,
            0.000244317,
            0.000260801,
            0.000277946,
            0.000295764,
            0.000316783,
            0.000340014,
            0.000365642,
            0.000393872,
            0.00042644,
            0.000443327,
            0.000462218,
            0.000481601,
            0.000501481,
            0.000523587,
            0.000548063,
            0.00057324,
            0.000599128,
            0.000627665,
            0.000659028,
            0.000691355,
            0.000726777,
            0.000765505,
            0.000807768,
            0.000851474,
            0.000899062,
            0.000950806,
            0.001006997,
            0.00107065,
            0.001136799,
            0.001193866,
            0.001252723,
            0.001313399,
            0.001407876,
            0.001473206,
            0.001574787,
            0.001644937,
            0.001753863,
            0.001867309,
            0.001985368,
            0.002108124,
            0.002279251,
            0.002413302,
            0.002599804,
            0.002795375,
            0.003000219,
            0.003269634,
            0.003496096,
            0.003793177,
            0.004103694,
            0.004353103,
            0.004714636,
            0.005035998,
            0.00542431,
            0.005885753,
            0.006123538,
            0.006366031,
            0.006675769,
            0.006928856,
            0.007251837,
            0.007582175,
            0.007988292,
            0.008334815,
            0.008760355,
            0.00919649,
            0.009643218,
            0.010177792,
            0.010726786,
            0.011371864,
            0.012035777,
            0.012718525,
            0.013509128,
            0.014323569,
            0.015351369,
            0.016316633,
            0.017513795,
            0.018753335,
            0.020143991,
            0.021810395,
            0.023543014,
            0.025586694,
            0.027843292,
            0.030462452,
            0.033339262,
            0.035868224,
            0.037733321,
            0.039885461,
            0.042181,
            0.04483526,
            0.04784821,
            0.051219748,
            0.055165215,
            0.059756447,
            0.065208334,
            0.071736448,
            0.075323192,
            0.079627308,
            0.084648768,
            0.089670327,
            0.095409423,
            0.102583152,
            0.110474122,
            0.119799644,
            0.130560199,
            0.143472399,
            0.159254616,
            0.173876874,
            0.173876775,
            0.173877205,
            0.173876191,
        ]
    )

    y_K1_eff = np.array(
        [
            0,
            0.004141765,
            0.004331717,
            0.004551525,
            0.004777855,
            0.005010809,
            0.005250448,
            0.005552525,
            0.005836009,
            0.006157739,
            0.006520677,
            0.006896276,
            0.007317678,
            0.007754371,
            0.008277539,
            0.008821708,
            0.00938722,
            0.01005437,
            0.010791668,
            0.011605088,
            0.012501089,
            0.013534737,
            0.014070729,
            0.014670316,
            0.015285493,
            0.015916472,
            0.016618091,
            0.017394932,
            0.018194019,
            0.019015674,
            0.019921404,
            0.020916839,
            0.021942877,
            0.023067121,
            0.024296311,
            0.025637687,
            0.027024863,
            0.028535264,
            0.030177562,
            0.031961018,
            0.033981288,
            0.036080787,
            0.037892043,
            0.039760083,
            0.04168589,
            0.044684497,
            0.046757986,
            0.049982075,
            0.052208534,
            0.055665757,
            0.059266412,
            0.06301348,
            0.066909603,
            0.072341008,
            0.076595628,
            0.082515014,
            0.088722218,
            0.095223763,
            0.103774688,
            0.110962364,
            0.12039141,
            0.13024689,
            0.138162859,
            0.149637513,
            0.159837205,
            0.172161832,
            0.186807544,
            0.194354569,
            0.202051039,
            0.211881786,
            0.219914511,
            0.230165575,
            0.240650148,
            0.253539869,
            0.264538163,
            0.278044348,
            0.291886787,
            0.30606548,
            0.323032275,
            0.340456749,
            0.360930855,
            0.382002746,
            0.403672421,
            0.428765345,
            0.454614839,
            0.487236106,
            0.517872543,
            0.555869198,
            0.595210866,
            0.639348819,
            0.692238705,
            0.747230175,
            0.812094425,
            0.883716437,
            0.966845794,
            1.058152651,
            1.138419223,
            1.197615414,
            1.265922053,
            1.338780005,
            1.423023413,
            1.518651233,
            1.625660253,
            1.750885182,
            1.896605973,
            2.069643073,
            2.276838446,
            2.390677885,
            2.52728595,
            2.686661738,
            2.846040667,
            3.028193456,
            3.255879993,
            3.506330964,
            3.802313096,
            4.143841668,
            4.553661125,
            5.0545719,
            5.518666802,
            5.51866363,
            5.518677281,
            5.518645122,
        ]
    )

    x_p_mdof = np.array(
        [
            0,
            0.0004,
            0.0008,
            0.0012,
            0.0016,
            0.002,
            0.0024,
            0.0028,
            0.0032,
            0.0036,
            0.004,
            0.0044,
            0.0048,
            0.0052,
            0.0056,
            0.006,
            0.0064,
            0.0068,
            0.0072,
            0.0076,
            0.008,
            0.0084,
            0.0088,
            0.0092,
            0.0096,
            0.01,
            0.0104,
            0.0108,
            0.0112,
            0.0116,
            0.012,
            0.0124,
            0.0128,
            0.0132,
            0.0136,
            0.014,
            0.0144,
            0.0148,
            0.0152,
            0.0156,
            0.016,
            0.0164,
            0.0168,
            0.0172,
            0.0176,
            0.018,
            0.0184,
            0.0188,
            0.0192,
            0.0196,
            0.02,
            0.0204,
            0.0208,
            0.0212,
            0.0216,
            0.022,
            0.0224,
            0.0228,
            0.0232,
            0.0236,
            0.024,
            0.0244,
            0.0248,
            0.0252,
            0.0256,
            0.026,
            0.0264,
            0.0268,
            0.0272,
            0.0276,
            0.028,
            0.0284,
            0.0288,
            0.0292,
            0.0296,
            0.03,
            0.0304,
            0.0308,
            0.0312,
            0.0316,
            0.032,
            0.0324,
            0.0328,
            0.0332,
            0.0336,
            0.034,
            0.0344,
            0.0348,
            0.0352,
            0.0356,
            0.036,
            0.0364,
            0.0368,
            0.0372,
            0.0376,
            0.038,
            0.0384,
            0.0388,
            0.0392,
            0.0396,
            0.04,
            0.0404,
            0.0408,
            0.0412,
            0.0416,
            0.042,
            0.0424,
            0.0428,
            0.0432,
            0.0436,
            0.044,
            0.0444,
            0.0448,
            0.0452,
            0.0456,
            0.046,
            0.0464,
            0.0468,
            0.0472,
            0.0476,
            0.048,
            0.0484,
            0.0488,
            0.0492,
            0.0496,
            0.05,
            0.0504,
            0.0508,
            0.0512,
            0.0516,
            0.052,
            0.0524,
            0.0528,
            0.0532,
            0.0536,
            0.054,
            0.0544,
            0.0548,
            0.0552,
            0.0556,
            0.056,
            0.0564,
            0.0568,
            0.0572,
            0.0576,
            0.058,
            0.0584,
            0.0588,
            0.0592,
            0.0596,
            0.06,
            0.0604,
            0.0608,
            0.0612,
            0.0616,
            0.062,
            0.0624,
            0.0628,
            0.0632,
            0.0636,
            0.064,
            0.0644,
            0.0648,
            0.0652,
            0.0656,
            0.066,
            0.0664,
            0.0668,
            0.0672,
            0.0676,
            0.068,
            0.0684,
            0.0688,
            0.0692,
            0.0696,
            0.07,
            0.0704,
            0.0708,
            0.0712,
            0.0716,
            0.072,
            0.0724,
            0.0728,
            0.0732,
            0.0736,
            0.074,
            0.0744,
            0.0748,
            0.0752,
            0.0756,
            0.076,
            0.0764,
            0.0768,
            0.0772,
            0.0776,
            0.078,
            0.0784,
            0.0788,
            0.0792,
            0.0796,
            0.08,
            0.0804,
            0.0808,
            0.0812,
            0.0816,
            0.082,
            0.0824,
            0.0828,
            0.0832,
            0.0836,
            0.084,
            0.0844,
            0.0848,
            0.0852,
            0.0856,
            0.086,
            0.0864,
            0.0868,
            0.0872,
            0.0876,
            0.088,
            0.0884,
            0.0888,
            0.0892,
            0.0896,
            0.09,
            0.0904,
            0.0908,
            0.0912,
            0.0916,
            0.092,
            0.0924,
            0.0928,
            0.0932,
            0.0936,
            0.094,
            0.0944,
            0.0948,
            0.0952,
            0.0956,
            0.096,
            0.0964,
            0.0968,
            0.0972,
            0.0976,
            0.098,
            0.0984,
            0.0988,
            0.0992,
            0.0996,
            0.1,
            0.1004,
            0.1008,
            0.1012,
            0.1016,
            0.102,
            0.1024,
            0.1028,
            0.1032,
            0.1036,
            0.104,
            0.1044,
            0.1048,
            0.1052,
            0.1056,
            0.106,
            0.1064,
            0.1068,
            0.1072,
            0.1076,
            0.108,
            0.1084,
            0.1088,
            0.1092,
            0.1096,
            0.11,
            0.1104,
            0.1108,
            0.1112,
            0.1116,
            0.112,
            0.1124,
            0.1128,
            0.1132,
            0.1136,
            0.114,
            0.1144,
            0.1148,
            0.1152,
            0.1156,
            0.116,
            0.1164,
            0.1168,
            0.1172,
            0.1176,
            0.118,
            0.1184,
            0.1188,
            0.1192,
            0.1196,
            0.12,
        ]
    )

    y_p_mdof = np.array(
        [
            0,
            6.111379948,
            12.23563215,
            18.33303255,
            24.40057071,
            30.49105054,
            36.5696616,
            42.62723414,
            48.66819732,
            54.6994717,
            60.70306381,
            66.67482131,
            72.61405215,
            78.51487384,
            84.37936255,
            90.20094374,
            95.97338891,
            101.6942758,
            107.369141,
            112.99314,
            118.5593523,
            124.0636255,
            129.5018072,
            134.8815102,
            140.2086169,
            145.4744765,
            150.6808193,
            155.8120739,
            160.8751609,
            165.8770009,
            170.8214002,
            175.7221999,
            180.5752477,
            185.3829658,
            190.14397,
            194.8617208,
            199.5265291,
            204.1432396,
            208.71116,
            213.2354808,
            217.7217386,
            222.1720094,
            226.5921757,
            230.9801614,
            235.3394267,
            239.6730859,
            243.9787169,
            248.2566655,
            252.5090081,
            256.7381667,
            260.9444875,
            265.1297006,
            269.294152,
            273.4388797,
            277.566306,
            281.6747008,
            285.7651021,
            289.8371639,
            293.8957305,
            297.9425323,
            301.9696104,
            305.978695,
            309.9722083,
            313.9553408,
            317.9263623,
            321.8842347,
            325.8293041,
            329.7622625,
            333.6851861,
            337.5980748,
            341.4995446,
            345.3892494,
            349.2671893,
            353.1323261,
            356.9836218,
            360.8245367,
            364.6446898,
            368.4510018,
            372.2400124,
            376.0082613,
            379.7522882,
            383.4720931,
            387.1642157,
            390.8321164,
            394.4688745,
            398.0779503,
            401.6558836,
            405.2061346,
            408.7287034,
            412.2305104,
            415.715016,
            419.1787599,
            422.6252025,
            426.0578038,
            429.4731038,
            432.867642,
            436.2483391,
            439.6048143,
            442.9336071,
            446.238178,
            449.5116063,
            452.7504318,
            455.9581147,
            459.1346551,
            462.2765927,
            465.3873877,
            468.4705004,
            471.5224705,
            474.5467584,
            477.5468244,
            480.5226683,
            483.4708299,
            486.3947696,
            489.2944873,
            492.1630624,
            495.0039553,
            497.8171659,
            500.6026942,
            503.35708,
            506.0803232,
            508.7689636,
            511.4195409,
            514.032055,
            516.6099664,
            519.1498145,
            521.6515996,
            524.1118613,
            526.5305995,
            528.9112747,
            531.2538867,
            533.551515,
            535.8041597,
            538.0118207,
            540.1744979,
            542.2887312,
            544.3510603,
            546.3614851,
            548.313085,
            550.2093205,
            552.0501914,
            553.8253169,
            555.5450778,
            557.206014,
            558.8150459,
            560.3721735,
            561.8773969,
            563.3410969,
            564.7632735,
            566.1404663,
            567.4795961,
            568.784123,
            570.0575074,
            571.296289,
            572.503928,
            573.6838847,
            574.8326988,
            575.957291,
            577.0576612,
            578.1372697,
            579.1926562,
            580.227281,
            581.2446044,
            582.2446264,
            583.227347,
            584.1962264,
            585.1478044,
            586.082081,
            587.0025164,
            587.9021902,
            588.7880228,
            589.656554,
            590.511244,
            591.3417121,
            592.1617993,
            592.9611248,
            593.7431489,
            594.5044113,
            595.2518326,
            595.9854127,
            596.7051517,
            597.4075893,
            598.099646,
            598.7744013,
            599.4387758,
            600.0858488,
            600.7190807,
            601.3350112,
            601.93018,
            602.5080474,
            603.0616928,
            603.5945765,
            604.1032381,
            604.5911381,
            605.0582764,
            605.5081133,
            605.944109,
            606.3628034,
            606.7676565,
            607.1552083,
            607.5323792,
            607.8922487,
            608.2313565,
            608.5600835,
            608.871509,
            609.1725537,
            609.4597572,
            609.7331196,
            609.9961012,
            610.2487019,
            610.494382,
            610.726221,
            610.9442189,
            611.1552962,
            611.3490721,
            611.5324671,
            611.6985607,
            611.8473529,
            611.9788437,
            612.0964934,
            612.2003019,
            612.2937295,
            612.3802366,
            612.4563628,
            612.5255685,
            612.5913139,
            612.6466784,
            612.702043,
            612.750487,
            612.7920104,
            612.8300735,
            612.8646763,
            612.8923586,
            612.9165806,
            612.9373423,
            612.9546437,
            612.9650245,
            612.9719451,
            612.9754054,
            612.9719451,
            612.9684848,
            612.9546437,
            612.9373423,
            612.9165806,
            612.8923586,
            612.861216,
            612.8266132,
            612.7885501,
            612.7435664,
            612.6985827,
            612.6501387,
            612.5982345,
            612.5428699,
            612.4875054,
            612.4252203,
            612.3629352,
            612.3006501,
            612.2314444,
            612.1622387,
            612.0895728,
            612.0134465,
            611.9373203,
            611.8577338,
            611.774687,
            611.6881799,
            611.6016728,
            611.5117054,
            611.421738,
            611.3248501,
            611.2279622,
            611.7885281,
            616.4010862,
            607.5981246,
            605.6119218,
            601.9509417,
            600.843651,
            599.1827148,
            599.2173176,
            599.4249347,
            599.8159467,
            600.1481339,
            600.3384495,
            600.3592112,
            600.2727042,
            600.1723559,
            600.0650871,
            599.9612786,
            599.9474375,
            594.3452383,
            594.1376213,
            593.8469574,
            594.4628879,
            591.0891114,
            589.1721142,
            588.1755526,
            588.473137,
            588.8364667,
            588.9817986,
            588.4627561,
            588.3105036,
            588.4454547,
            588.3312653,
        ]
    )

    # Generate SDOF pushover curve
    def x_p_sdof(self, Γ):
        x_p_sdof_list = []
        for element in self.x_p_mdof:
            new_coord = element / Γ
            x_p_sdof_list.append(new_coord)
        return np.array(x_p_sdof_list)

    def y_p_sdof(self, Γ):
        y_p_sdof_list = []
        for element in self.y_p_mdof:
            new_coord = element / Γ
            y_p_sdof_list.append(new_coord)
        return np.array(y_p_sdof_list)

    ##

    def x_bilinear_line(self, start_graph, end_graph):
        return np.linspace(start_graph, end_graph, 1000)

    def find_intersections(self, curve_1, curve_2):
        intersection = curve_1.intersection(curve_2)
        intersection_coords = []
        if intersection.geom_type == "Point":
            intersection_coords.append((intersection.x, intersection.y))
        if intersection.geom_type == "MultiPoint":
            individual_points = [(pt.x, pt.y) for pt in intersection]
            for element in individual_points:
                intersection_coords.append(element)
        return intersection_coords

    def find_nearest_coordinate_index(self, curve_coordinates, coord):
        difference_array_x = np.absolute(curve_coordinates - coord)
        # find the index of minimum element from the array
        index = difference_array_x.argmin()
        return index

    def find_nearest_coordinate(self, curve_coordinates, coord):
        """
        Enter array of X or Y coordinates of a curve and X or Y coordinate of
        a point_a to find the nearest X or Y point_a to in the curve array
        """
        index = self.find_nearest_coordinate_index(curve_coordinates, coord)
        return curve_coordinates[index]

    def bilinear_m_q(self, x_1, x_2, y_1, y_2):
        """
        Enter coordinates of two points.
        Returns a tuple with m and q to generate
        one straight line which composes the bilinear line"""
        m, q = np.polyfit(x=[x_1, x_2], y=[y_1, y_2], deg=1)
        return m, q

    def generate_line(self, x_p_sdof, x_1_array, x_2_array, y_1_array, y_2_array):
        """
        Generate part of the bilinear curve: 1st or 2nd line that compose it
        Return a tuple with X and Y coordinates
        """
        m = self.bilinear_m_q(x_1_array, x_2_array, y_1_array, y_2_array)[0]
        q = self.bilinear_m_q(x_1_array, x_2_array, y_1_array, y_2_array)[1]
        x = self.x_bilinear_line(x_p_sdof[0], x_p_sdof[-1])
        y = m * x + q
        return x, y

    def interpolate_curve(self, x_coords, y_coords):
        curve = LineString(np.column_stack((x_coords, y_coords)))
        return curve

    def find_range_pushover(self, pushover_coord, line_1_coord, line_2_coord):
        index_0 = self.find_nearest_coordinate_index(pushover_coord, line_1_coord)
        index_1 = self.find_nearest_coordinate_index(pushover_coord, line_2_coord)
        list_fitting = [pushover_coord[index_0 : index_1 + 1]]
        # print("Nearest element to the given values is : ", pushover_coord[index_0])
        # print("Index of nearest value is : ", index_0)
        # print("Nearest element to the given values is : ", pushover_coord[index_1])
        # print("Index of nearest value is : ", index_1)
        return list_fitting
