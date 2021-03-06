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
    3     f(x) = x**3
    4     f(x) = sin(x)
    5     f(x) = cos(x)
    6     f(x) = tan(x)
    7     f(x) = exp(x)
    8     f(x) = sqrt(|x|) '''
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

        elif sys.argv[1] == "4":
            yval.append(np.sin(i))

        elif sys.argv[1] == "5":
            yval.append(np.cos(i))

        elif sys.argv[1] == "6":
            yval.append(np.tan(i))
  
        elif sys.argv[1] == "7":
            yval.append(np.exp(i))

        elif sys.argv[1] == "8":
            yval.append(np.sqrt(np.abs(i)))

        else:
            print("Unknown argument.\n", usage)
            sys.exit()
            
    plt.plot(xval, yval)
    plt.show()
