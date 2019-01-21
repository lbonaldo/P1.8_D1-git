#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

xval = [i for i in np.arange(-5.0, 5.1, 0.1) if round(i, 1) != 0.1]

yval = []

usage = (
    '''Usage: script.py [FUNCTION FORM]
Return a function in the domain [-5.0, 5.0] whose form depends on the argument given as an input:

    1     f(x) = x
    2     f(x) = exp(x)
    3     f(x) = sqrt(|x|) '''
)

if len(sys.argv) < 2:
    print(usage)

else:
    for i in xval:    
        if sys.argv[1] == "1":
            yval.append(i)

        elif sys.argv[1] == "2":
            yval.append(np.exp(i))

        elif sys.argv[1] == "3":
            yval.append(np.sqrt(np.abs(i)))

        else:
            print("Unknown argument.\n", usage)
            sys.exit()
            
    plt.plot(xval, yval)
    plt.show()
