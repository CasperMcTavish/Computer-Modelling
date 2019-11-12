"""

CMod Ex. 2: vector.py, a set of functions used to allow vector operations

Author: J. Waiton - s1739002
Version: 10/2019

"""
import math as m


def dot_prod(v1,v2):
    """
    Dot Product

    :param v1: Vector 1
    :param v2: Vector 2
    :return: dot product v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
    """
    dotproduct = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
    return dotproduct


def norm_sq(v):
    """
    Square modulus

    :param v: Vector 1
    :return: squared modulus dot_prod(v,v)
    """
    normalsq = (dot_prod(v,v))
    return normalsq

def mod(v):
    """
    Modulus

    :param v: Vector 1
    :return: modulus sqrt(norm_sq(v))
    """
    modulus = m.sqrt(norm_sq(v))
    return modulus

def scale(v, scal):
    """
    Multiplication of Vector with scalar

    :param v: vector
    :param scal: scalar factor
    :return: scaled vector [scal*v[0],scal*v[1],scal*v[2]]
    """
    scaled = [scal*v[0],scal*v[1],scal*v[2]]
    return scaled

def div(v, scal):
    """
    Division of Vector with scalar

    :param v: vector
    :param scal: scalar
    :return: scaled vector [v[0]/scal,v[1]/scal,v[2]/scal]
    """
    if scal == 0:
        print("You can't divide by zero!")
        return m.nan
    else:
        scaled = [v[0]/scal,v[1]/scal,v[2]/scal]
        return scaled

def addv(v1, v2):
    """
    Vector sum

    :param v1: vector 1
    :param v2: vector 2
    :return: vector sum [v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2]]
    """
    ad = [v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2]]
    return ad

def subv(v1, v2):
    """
    Vector difference

    :param v1: vector 1
    :param v2: vector 2
    :return: vector difference [v2[0]-v1[0],v2[1]-v1[1],v2[2]-v1[2]]
    """
    su = [v2[0]-v1[0],v2[1]-v1[1],v2[2]-v1[2]]
    return su

def crossprod(v1,v2):
    """
    Cross Product

    :param v1: Vector 1
    :param v2: Vector 2
    :return: Cross Product [(v1[1]*v2[2])-(v1[2]*v2[1]),-((v1[0]*v2[2])-(v1[2]*v2[0])),(v1[0]*v2[1])-(v1[1]*v2[0])]
    """
    crossprod = [(v1[1]*v2[2])-(v1[2]*v2[1]),-((v1[0]*v2[2])-(v1[2]*v2[0])),(v1[0]*v2[1])-(v1[1]*v2[0])]
    return crossprod

def same(v1,v2):
    """
    Checking vectors for identicality

    :param v1: Vector 1
    :param v2: Vector 2
    :return: If vectors are identical (true), otherwise (false) with a tolerance of 1e-8
    """
    if ((m.isclose(v1[0],v2[0], rel_tol=1e-8)) == (m.isclose(v1[1],v2[1], rel_tol=1e-8)) == (m.isclose(v1[2],v2[2], rel_tol=1e-8))):
        return True
    else:
        return False
