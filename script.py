#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

xval = [i for i in np.arange(-5.0, 5.1, 0.1) if round(i, 1) != 0.1]

yval = []

for i in xval:
    if sys.argv[1] == "1":
        yval.append(i)

    elif sys.argv[1] == "2":
        yval.append(np.sin(i))

    elif sys.argv[1] == "3":
        yval.append(np.cos(i))

    elif sys.argv[1] == "4":
        yval.append(np.tan(i))
        
plt.plot(xval, yval)
plt.show()
