"""
CMod Ex2: Defining potential energy and pairwise forces
of particles within a morse potential.
"""

import sys
import math as m
import numpy as np
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D

def potenergy(particle1, particle2, re, De, alpha):
    """
    Method to return potential energy
    of 2 particles interacting via
    the morse potential.

    :param particle1: 1st Particle3D instance
    :param particle2: 2nd Particle3D instance
    :param re: paramater re
    :param De: parameter De
    :param alpha: parameter alpha
    :return: potential energy of pairwise particles
    """
    #find separation using Particle3D separation
    sep = Particle3D.separation(particle1, particle2)
    #find potential by finding magnitude of separation and using given eqn
    potential = De*((1-np.exp(-alpha*(np.linalg.norm(sep)-re)))**2-1)
    return potential

def pairwiseforces(particle1, particle2, re, De, alpha):
    """
    Method to return pairwise forces
    of 2 particles interacting via the
    morse potential.

    :param particle1: 1st Particle3D instance
    :param particle2: 2nd Particle3D instance
    :param re: paramater re
    :param De: parameter De
    :param alpha: parameter alpha
    :return: potential energy of pairwise particles
    """
    #find separation using Particle3D separation
    sep = Particle3D.separation(particle1,particle2)
    #magnitude of separation vector
    r12 = np.linalg.norm(sep)
    #normalized separation vector
    rnorm = sep/r12
    #find constant out front
    L = -alpha*(r12-re)
    const = 2*alpha*De*(1-np.exp(L))*np.exp(L)
    #const = 2*alpha*De*((1-(np.exp(-alpha*(r12-re))))*(np.exp(-alpha*(r12-re))))
    #find force on particle 1
    f1 = np.multiply(const,rnorm)
    #unsure if return both f1 or just one and inverse in main code
    return f1
