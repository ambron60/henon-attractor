# Hénon Attractor generator in Python

The Hénon map is a discrete-time dynamical system. It is one of the most studied examples of dynamical systems that exhibit chaotic behavior. The Hénon map takes a point (xn, yn) in the plane and maps it to a new point

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/87672565712868250e7d2b410307bb1b047f31a7)

The map depends on two parameters, a and b, which for the classical Hénon map have values of a = 1.4 and b = 0.3. For the classical values the Hénon map is chaotic. For other values of a and b the map may be chaotic, intermittent, or converge to a periodic orbit. An overview of the type of behavior of the map at different parameter values may be obtained from its orbit diagram.

The map was introduced by Michel Hénon as a simplified model of the Poincaré section of the Lorenz model. For the classical map, an initial point of the plane will either approach a set of points known as the Hénon strange attractor, or diverge to infinity. The Hénon attractor is a fractal, smooth in one direction and a Cantor set in another. Numerical estimates yield a correlation dimension of 1.25 ± 0.02[1] and a Hausdorff dimension of 1.261 ± 0.003[2] for the attractor of the classical map. [[Wikipedia]](https://en.wikipedia.org/wiki/H%C3%A9non_map)

#### Instructions:

Open a terminal window and type (for example):

```python3 henon.py -.75 .32 1.2 0.3 10000```

Where the first four parameters indicate X0, Y0, a, b and iterations (e.g., 10000) indicates the number of forward evolutions. You can always type: ```python3 henon.py -h``` to view these instructions from the console itself.

Requires (libraries): argparse, matplotlib, and mpmath
