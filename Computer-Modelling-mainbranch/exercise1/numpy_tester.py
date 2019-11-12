"""
CMod Ex2: tester of the numpy functions.
Creates a pair of random vectors (numbpy arrays) and
runs through a few numpy functions

Author: J. Waiton - s1739002
Version: 10/2019
"""

import math as m
import numpy as np
import random

def main():

    # create 3 random vectors
    v1 = np.array([random.random(),random.random(),random.random()])
    v2 = np.array([random.random(),random.random(),random.random()])
    v3 = np.array([random.random(),random.random(),random.random()])

    # Print out the 3 vectors
    print("v1 = ", v1)
    print("v2 = ", v2)
    print("v3 = ", v3)

    #Print magnitude of 3 vectors
    print("v1 magnitude = ", np.linalg.norm(v1))
    print("v2 magnitude = ", np.linalg.norm(v2))
    print("v3 magnitude = ", np.linalg.norm(v3))

    #print addition, dot & cross products of v1 and v2
    print("v1 + v2 =", v1 + v2)
    print("v1 . v2 =", np.inner(v1,v2))
    print("v1 x v2 =", np.cross(v1,v2))

    #vector identities
        #1
    identity1part1 = np.cross(v1,v2)
    identity1part2 = np.cross(-v2,v1)
    if np.allclose(identity1part1,identity1part2,1e-8) == True:
        print("Identity 1 is correct.")

        #2
    identity2part1 = np.cross(v1,v2+v3)
    identity2part2 = np.cross(v1,v2) + np.cross(v1,v3)
    if np.allclose(identity2part1,identity2part2,1e-8) == True:
        print("Identity 2 is correct.")

        #3
    identity3part1 = np.cross(v1,np.cross(v2,v3))
    identity3part2 = np.inner(v1,v3)*v2-np.inner(v1,v2)*v3
    if np.allclose(identity3part1,identity3part2,1e-8) == True:
        print("Identity 3 is correct.")

main()
