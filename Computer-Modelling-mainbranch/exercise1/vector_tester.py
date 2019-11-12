"""
CMod Ex2: tester of the vector.py module.
Creates a pair of random vectors and
runs through all functions implemented in vector.py

Author: J. Waiton  - s1739002
Version: 10/2019
"""

import math as m
import numpy as np
import random
import vector as vc

# Main method:
def main():

    # create 3 random vectors
    v1 = [random.random(),random.random(),random.random()]
    v2 = [random.random(),random.random(),random.random()]
    v3 = [random.random(),random.random(),random.random()]

    # Print out the 3 vectors
    print("v1 = ", v1)
    print("v2 = ", v2)
    print("v3 = ", v3)

    #Print magnitude of 3 vectors
    print("v1 magnitude = ", vc.mod(v1))
    print("v2 magnitude = ", vc.mod(v2))
    print("v3 magnitude = ", vc.mod(v3))

    #print addition, dot & cross products of v1 and v2
    print("v1 + v2 =", vc.addv(v1,v2))
    print("v1 . v2 =", vc.dot_prod(v1,v2))
    print("v1 x v2 =", vc.crossprod(v1,v2))

    #vector identities
        #1
    identity1part1 = vc.crossprod(v1,v2)
    identity1part2 = vc.crossprod(vc.scale(v2,-1),v1)
    if vc.same(identity1part1,identity1part2) == True:
        print("Identity 1 is correct.")

        #2
    identity2part1 = vc.crossprod(v1,vc.addv(v2,v3))
    identity2part2 = vc.addv(vc.crossprod(v1,v2),vc.crossprod(v1,v3))
    if vc.same(identity2part1,identity2part2) == True:
        print("Identity 2 is correct.")

        #3
    identity3part1 = vc.crossprod(v1,vc.crossprod(v2,v3))
    identity3part2 = vc.subv((vc.scale(v2,vc.dot_prod(v1,v3))),(vc.scale(v3,vc.dot_prod(v1,v2))))
    if vc.same(identity3part1,identity3part2) == True:
        print("Identity 3 is correct.")


main()
