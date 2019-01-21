#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

xval = [i for i in np.arange(-3.0, 3.1, 0.1) if round(i, 1) != 0.1]

yval = []

usage = (
    '''Usage: script.py [FUNCTION FORM]
Return a function in the domain [-3.0, 3.0] whose form depends on the argument given as an input:

    1     f(x) = x
    2     f(x) = x**2
    3     f(x) = x**3'''
)

if len(sys.argv) < 2:
    print(usage)

else:
    for i in xval:    
        if sys.argv[1] == "1":
            yval.append(i)

        elif sys.argv[1] == "2":
            yval.append(i**2)

        elif sys.argv[1] == "3":
            yval.append(i**3)
  
    plt.plot(xval, yval)
    plt.show()
