"""
 CMod Ex2: Particle3D, a class to describe 3D particles
 Author: J.Waiton - s1739002
 Date 10/2019
"""
#importing relevant modules
import math as m
import numpy as np
import random

class Particle3D(object):
    """
    Class to describe 3D particles.

    Properties:
    position(numpy array - floats) - position along the x,y,z axis
    velocity(numpy array - floats) - velocity along the x,y,z axis
    mass(float) - particle mass

    Methods:
    * formatted output
    * kinetic energy
    * first-order velocity update
    * first- and second order position updates
    """

    def __init__(self, posx, posy, posz, velx, vely, velz, mass, label):
        """
        Initialise a Particle3D instance

        :param posx: position in x as float
        :param posy: position in y as float
        :param posz: position in z as float
        :param velx: velocity in x as float
        :param vely: velocity in y as float
        :param velz: velocity in z as float
        :param mass: mass as float
        """
        self.position = np.array([posx,posy,posz])
        self.velocity = np.array([velx,vely,velz])
        self.mass = mass
        self.label = label


    def __str__(self):
        """
        Define output format.
        For particle p=([2.0,2.0,2.0], [0.5,0.5,0.5], 1.0) this will print as
        "x = 2.0, y = 2.0, z = 2.0, vx = 0.5, vy = 0.5, vz = 0.5, m = 1.0"
        """
        """return "x = " + str(self.position[0]) ", y = " + str(self.position[1]) + ", z = " + str(self.position[2]) + ", v = " + str(self.velocity) + ", m = " + str(self.mass)"""
        return "Label = " + str(self.label) + "x = " + str(self.position[0]) + ", y = " + str(self.position[1]) + ", z = " + str(self.position[2]) + ", vx = " + str(self.velocity[0]) + ", vy = " + str(self.velocity[1]) + ", vz = " + str(self.velocity[2])

    def kinetic_energy(self):
        """
        Return kinetic energy as
        1/2*mass*[vel]^2
        """
        # np.linalg.norm is finding the magnitude of the velocity
        return 0.5*self.mass*(np.linalg.norm(self.velocity))**2


    # Time integration methods
    def leap_velocity(self, dt, force):
        """
        First-order velocity update,
        v(t+dt) = v(t) + dt*F(t)

        :param dt: timestep as float
        :param force: force on particle as float
        """
        #Relies on force also being a 3D numpy array
        for i in range(3):
            self.velocity[i] += dt*force[i]/self.mass
        return self.velocity

    def leap_pos1st(self, dt):
        """
        First-order position update,
        x(t+dt) = x(t) + dt*v(t)

        :param dt: timestep as float
        """
        for i in range(3):
            self.position[i] += dt*self.velocity[i]
        return self.position


    def leap_pos2nd(self, dt, force):
        """
        Second-order position update,
        x(t+dt) = x(t) + dt*v(t) + 1/2*dt^2*F(t)

        :param dt: timestep as float
        :param force: current force as float
        """
        #requires force to be a 3D numpy array
        for i in range(3):
            self.position[i] += dt*self.velocity[i] + 0.5*dt**2*force[i]/self.mass
        return self.position

    @staticmethod
    def from_file(file_handle):
        """
        Create particle from file line which is read into the class.
        file read in is of format;
        posx, posy, posz, velx, vely, velz, mass, label
        """
        #read line of file
        line = file_handle.readline()
        #split file into components at "," within file
        comp = line.split(" ")
        print(comp)
        #convert list of strings into list of floats
        vals = [float(x) for x in comp]
        #apply this list to Particle3D and return the particle
        return Particle3D(vals[0],vals[1],vals[2],vals[3],vals[4],vals[5],vals[6],vals[7])


    @staticmethod
    def separation(par1,par2):
        """
        Particle separation for two 3D particles
        sep = par2 - par1

        :param par1: Particle 1
        :param par2: Particle 2
        """
        #print((par2.position,par1.position))
        #finding separation
        sep = par2.position - par1.position
        return sep
