"""
CMod Ex2: Periodic Boundary Conditions
Computer Modelling
Author: J. Waiton - s1739002
Version: 10/2019
"""

import math as m
import numpy as np
import random

def main():
    #define main points
    x1 = float(input("Please give x1 value: "))
    x2 = float(input("Please give x2 value: "))
    x3 = float(input("Please give x3 value: "))
    x=np.array([x1,x2,x3])
    l = float(input("Please give length of the cubes' size: "))

    #f
    xcube = np.mod(x,l)
    xmic = np.mod(x+(l/2),l) - (l/2)

    print("The image inside the cube is: ", xcube)
    print("The image closest to the origin is: ", xmic)



main()
