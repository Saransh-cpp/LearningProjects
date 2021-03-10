import colour
import numpy as np
# import numpy as np
import unittest
from itertools import permutations
from colour import (domain_range_scale)

from colour.utilities import (as_float_array, from_range_1, to_domain_1,
                              tsplit, tstack)

def handle_numpy_errors(**kwargs):
    """
    Decorator for handling *Numpy* errors.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        Keywords arguments.

    Returns
    -------
    object

    References
    ----------
    :cite:`Kienzle2011a`

    Examples
    --------
    >>> import numpy
    >>> @handle_numpy_errors(all='ignore')
    ... def f():
    ...     1 / numpy.zeros(3)
    >>> f()
    """

    context = np.errstate(**kwargs)

    def wrapper(function):
        """
        Wrapper for given function.
        """

        @functools.wraps(function)
        def wrapped(*args, **kwargs):
            """
            Wrapped function.
            """

            with context:
                return function(*args, **kwargs)

        return wrapped

    return wrapper


ignore_numpy_errors = handle_numpy_errors(all='ignore')



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

def RGB_to_HSL(RGB):
    """
    Converts from *RGB* colourspace to *HSL* colourspace.

    Parameters
    ----------
    RGB : array_like
        *RGB* colourspace array.

    Returns
    -------
    ndarray
        *HSL* array.

    Notes
    -----

    +------------+-----------------------+---------------+
    | **Domain** | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``RGB``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    +------------+-----------------------+---------------+
    | **Range**  | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``HSL``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    References
    ----------
    :cite:`EasyRGBl`, :cite:`Smith1978b`, :cite:`Wikipedia2003`

    Examples
    --------
    >>> RGB = np.array([0.45620519, 0.03081071, 0.04091952])
    >>> RGB_to_HSL(RGB)  # doctest: +ELLIPSIS
    array([ 0.9960394...,  0.8734714...,  0.2435079...])
    """

    RGB = to_domain_1(RGB)

    minimum = np.amin(RGB, -1)
    maximum = np.amax(RGB, -1)
    delta = np.ptp(RGB, -1)

    R, G, B = tsplit(RGB)

    L = (maximum + minimum) / 2

    S = np.where(
        L < 0.5,
        delta / (maximum + minimum),
        delta / (2 - maximum - minimum),
    )
    S[np.asarray(delta == 0)] = 0

    delta_R = (((maximum - R) / 6) + (delta / 2)) / delta
    delta_G = (((maximum - G) / 6) + (delta / 2)) / delta
    delta_B = (((maximum - B) / 6) + (delta / 2)) / delta

    H = delta_B - delta_G
    H = np.where(G == maximum, (1 / 3) + delta_R - delta_B, H)
    H = np.where(B == maximum, (2 / 3) + delta_G - delta_R, H)
    H[np.asarray(H < 0)] += 1
    H[np.asarray(H > 1)] -= 1
    H[np.asarray(delta == 0)] = 0

    HSL = tstack([H, S, L])

    return from_range_1(HSL)


# =====================TEST=========================================

class TestRGB_to_HCL(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.cylindrical.RGB_to_HCL` definition unit
    tests methods.
    """

    def test_RGB_to_HCL(self):
        """
        Tests :func:`colour.models.rgb.cylindrical.RGB_to_HCL` definition.
        """

        np.testing.assert_almost_equal(
            RGB_to_HCL(np.array([0.45620519, 0.03081071, 0.04091952])),
            np.array([-0.03167854, 0.2841715, 0.22859647]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_HCL(np.array([1.00000000, 2.00000000, 0.50000000])),
            np.array([1.83120102, 1.0075282, 1.00941024]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_HCL(np.array([2.00000000, 1.00000000, 0.50000000])),
            np.array([0.30909841, 1.0075282, 1.00941024]),
            decimal=7)

        np.testing.assert_almost_equal(
            RGB_to_HCL(np.array([0.50000000, 1.00000000, 2.00000000])),
            np.array([-2.40349351, 1.0075282, 1.00941024]),
            decimal=7)

    def test_n_dimensional_RGB_to_HCL(self):
        """
        Tests :func:`colour.models.rgb.cylindrical.RGB_to_HCL` definition
        n-dimensional arrays support.
        """

        RGB = np.array([0.45620519, 0.03081071, 0.04091952])
        HCL = RGB_to_HCL(RGB)

        RGB = np.tile(RGB, (6, 1))
        HCL = np.tile(HCL, (6, 1))
        np.testing.assert_almost_equal(RGB_to_HCL(RGB), HCL, decimal=7)

        RGB = np.reshape(RGB, (2, 3, 3))
        HCL = np.reshape(HCL, (2, 3, 3))
        np.testing.assert_almost_equal(RGB_to_HCL(RGB), HCL, decimal=7)

    def test_domain_range_scale_RGB_to_HCL(self):
        """
        Tests :func:`colour.models.rgb.cylindrical.RGB_to_HCL` definition
        domain and range scale support.
        """

        RGB = np.array([0.45620519, 0.03081071, 0.04091952])
        HCL = RGB_to_HCL(RGB)

        d_r = (('reference', 1), (1, 1), (100, 100))
        for scale, factor in d_r:
            with domain_range_scale(scale):
                np.testing.assert_almost_equal(
                    RGB_to_HCL(RGB * factor), HCL * factor, decimal=7)

    @ignore_numpy_errors
    def test_nan_RGB_to_HCL(self):
        """
        Tests :func:`colour.models.rgb.cylindrical.RGB_to_HCL` definition nan
        support.
        """

        cases = [-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]
        cases = set(permutations(cases * 3, r=3))
        for case in cases:
            RGB = np.array(case)
            RGB_to_HCL(RGB)


RGB = np.array([0.50000000, 1.00000000, 2.00000000])
print(RGB_to_HCL(RGB))
