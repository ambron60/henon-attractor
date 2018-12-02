#!/usr/bin/python3


import argparse
from matplotlib import pyplot as plt
from mpmath import mp, mpf


def henon_map(xn, yn, a, b):
    """
    Two-dimensional dissipative map.
    :param xn: First evolution point.
    :param yn: Second evolution point.
    :param a: First system parameter.
    :param b: Second system parameter.
    :return: Next iteration.
    """
    return yn + 1 - (a * xn**2), b*xn


def initial_params():
    parser = argparse.ArgumentParser(description="Henon Map parameter collector. Enter "
                                                 "the below parameters separated by spaces.")
    parser.add_argument("x0", help="Initial condition X0", type=str)
    parser.add_argument("y0", help="Initial condition Y0", type=str)
    parser.add_argument("a", help="Initial condition a", type=str)
    parser.add_argument("b", help="Initial condition b", type=str)
    parser.add_argument("iterations", help="Number of iterates as an integer", type=int)
    return vars(parser.parse_args())


def plot_attractor(x, y):
    plt.scatter(x, y, c="blue", s=1)
    plt.xlabel(r"$X_n$")
    plt.ylabel(r"$Y_n$")
    plt.title("The H\xe9non Attractor")
    plt.show()


def main():
    x, y, a, b = [mpf(param) for param in list(initial_params().values())[:-1]]
    iterations = initial_params()["iterations"]
    mp.dps = 16  # set decimal precision of all parameters except iterations
    xt, yt = [], []  # store iterations of xn and yn
    for _ in range(iterations + 1):
        xn, yn = henon_map(x, y, a, b)
        xt.append(x)
        yt.append(y)
        x, y = xn, yn  # forward evolutions
    plot_attractor(xt, yt)  # plot Henon map


if __name__ == "__main__":
    main()
