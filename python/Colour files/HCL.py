import colour
import numpy as np


def RGB_to_HCL(RGB, gamma=3, Y_0=100):
    R, G, B = colour.utilities.tsplit(RGB)

    print('this is', str(R), str(G), str(B))

    Min = np.minimum(np.minimum(R, G), B)
    Max = np.maximum(np.maximum(R, G), B)

    alpha = (Min / Max) / Y_0

    Q = np.exp(alpha * gamma)

    L = (Q * Max + (Q - 1) * Min) / 2

    R_G = R - G
    G_B = G - B
    B_R = B - R

    C = Q * (np.abs(R_G) + np.abs(G_B) + np.abs(B_R)) / 3

    H = np.arctan(G_B / R_G)

    _2_3_H = 2 / 3 * H
    _4_3_H = 4 / 3 * H

    H = np.select([
        np.logical_and(R_G >= 0, G_B >= 0),
        np.logical_and(R_G >= 0, G_B < 0),
        np.logical_and(R_G < 0, G_B >= 0),
        np.logical_and(R_G < 0, G_B < 0),
    ], [
        _2_3_H,
        _4_3_H,
        np.pi + _4_3_H,
        _2_3_H - np.pi,
    ])

    return colour.utilities.tstack([H, C, L])


def HCL_to_RGB(HCL, gamma=3, Y_0=100):
    H, C, L = colour.utilities.tsplit(HCL)

    Q = np.exp((1 - (3 * C) / (4 * L)) * (gamma / Y_0))

    Min = (4 * L - 3 * C) / (4 * Q - 2)
    Max = Min + (3 * C) / (2 * Q)

    def _1_2_3(a):
        return colour.utilities.tstack([a, a, a], dtype=np.bool_)

    tan_3_2_H = np.tan(3 / 2 * H)
    tan_3_4_H_MP = np.tan(3 / 4 * (H - np.pi))
    tan_3_4_H = np.tan(3 / 4 * H)
    tan_3_2_H_PP = np.tan(3 / 2 * (H + np.pi))

    RGB = np.select(
        [
            _1_2_3(np.logical_and(0 <= H, H <= np.radians(60))),
            _1_2_3(np.logical_and(np.radians(60) < H, H <= np.radians(120))),
            _1_2_3(np.logical_and(np.radians(120) < H, H <= np.pi)),
            _1_2_3(np.logical_and(np.radians(-60) <= H, H < 0)),
            _1_2_3(np.logical_and(np.radians(-120) <= H, H < np.radians(-60))),
            _1_2_3(np.logical_and(-np.pi < H, H < np.radians(-120))),
        ],
        [
            colour.utilities.tstack([
                Max,
                (Max * tan_3_2_H + Min) / (1 + tan_3_2_H),
                Min,
            ]),
            colour.utilities.tstack([
                (Max * (1 + tan_3_4_H_MP) - Min) / tan_3_4_H_MP,
                Max,
                Min,
            ]),
            colour.utilities.tstack([
                Min,
                Max,
                Max * (1 + tan_3_4_H_MP) - Min * tan_3_4_H_MP,
            ]),
            colour.utilities.tstack([
                Max,
                Min,
                Min * (1 + tan_3_4_H) - Max * tan_3_4_H,
            ]),
            colour.utilities.tstack([
                (Min * (1 + tan_3_4_H) - Max) / (tan_3_4_H),
                Min,
                Max,
            ]),
            colour.utilities.tstack([
                Min,
                (Min * tan_3_2_H_PP + Max) / (1 + tan_3_2_H_PP),
                Max,
            ]),
        ],
    )

    return RGB


RGB = np.array([255, 0, 0])
print(RGB_to_HCL(RGB))
