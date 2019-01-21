#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

xval = [i for i in np.arange(-5.0, 5.1, 0.1) if round(i, 1) != 0.1]

yval = []

if sys.argv[1] == "1":
    for i in xval:
        yval.append(i)

plt.plot(xval, yval)
plt.show()
