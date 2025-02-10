import numpy as np


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])


def f2(x: np.ndarray) -> np.ndarray:
    return (x[0] - (-7.77 - ((-5.87 + x[1]) - np.tan(-8.3)))) / np.exp((1.79 / (x[2] + x[0])))


def f3(x: np.ndarray) -> np.ndarray:
    return ((-9.46 * x[1]) + (-3.45 * x[2])) + x[1]


def f4(x: np.ndarray) -> np.ndarray:
    return (np.cos(np.abs(x[1])) / 0.64) / ((np.sqrt(0.44) - np.exp(-2.25)) + (np.sin(x[0]) / 9.29))


def f5(x: np.ndarray) -> np.ndarray:
    return (((x[1] - x[1]) / np.tan(3.94)) / ((8.52 - (-5.53 + np.log(7.59))) / x[0]))


def f6(x: np.ndarray) -> np.ndarray:
    return (x[1] + ((4.72 ** -3.12) / np.exp(x[0]))) - np.abs(x[0])


def f7(x: np.ndarray) -> np.ndarray:
    return np.exp((np.abs(x[0]) + (x[0] * x[1]))) * np.exp((np.abs(x[0]) / -8.88))


def f8(x: np.ndarray) -> np.ndarray:
    return np.exp((x[5] - (-4.16))) + np.tan((np.cos(x[3]) + np.tan(x[4])))