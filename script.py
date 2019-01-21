#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

xval = [i for i in np.arange(-3.0, 3.1, 0.1) if round(i, 1) != 0.1]

yval = []

usage = (
    '''Usage: script.py [FUNCTION FORM]
Return a function in the domain [-5.0, 5.0] whose form depends on the argument given as an input:

    1     f(x) = x'''
)

if len(sys.argv) < 2:
    print(usage)

else:
    for i in xval:    
        if sys.argv[1] == "1":
            yval.append(i)
  
    plt.plot(xval, yval)
    plt.show()
