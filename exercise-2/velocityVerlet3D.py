"""
CMod Ex2: velocity Verlet time integration of
two particles moving with morse potential.

Plots the relative separation of two particles
and total energy of the system wrt time.
Writes two files containing particle separation
and total energy as functions of time.
"""

'''
IMPORTANT
When running this program, it is important to
include (as arguments) the two files you wish
to be run, being your initial particle positions
& constants. These files (in the correct format
for this code) will be provided for you, but your
own values can be used if needed.

input line;
python3 symplecticEuler3D.py initposO2 potconstO2
'''


import sys
import math
import numpy as np
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D
import morsepotential as mp



# Begin main code
def main():
    # Read name of output file from command line
    if len(sys.argv)!=3:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " <output file>")
        quit()
    else:
        #input files for initial position & potential constants
        inputfile1 = sys.argv[1]
        inputfile2 = sys.argv[2]

    # Open output files separation & total energy
    sep_outfile = open("separationfile.txt", "w")
    u_outfile = open("totalenergyfile.txt", "w")

    # Set up simulation parameters
    dt = float(input("Please determine timestep: "))
    tfinal = 12
    t = 0.0
    tstep = int(tfinal / dt)

    #open position file
    file_handle = open(inputfile1,"r")

    #Open potential constants file
    file_pot = open(inputfile2, "r")
    #read line of file
    line = file_pot.readline()
    #split file into components at "," within file, should have 4 elements
    components = line.split(" ")
    #convert to floats and separate
    vals = [float(i) for i in components]
    #separate for readability into constants
    De = vals[0]
    re = vals[1]
    alpha = vals[2]
    #NOTE mass is included in the initial positions file, not in here

    #Create particles from initial position files
    p1 = Particle3D.from_file(file_handle)
    p2 = Particle3D.from_file(file_handle)



    # Write out initial conditions, separation & energy
    separ = np.linalg.norm(Particle3D.separation(p1,p2))
    energy = p1.kinetic_energy() + p2.kinetic_energy() + mp.potenergy(p1,p2,re,De,alpha)

    u_outfile.write("{},{} \n".format(t,energy))
    sep_outfile.write("{},{} \n".format(t,separ))

    #Find pairwiseforces
    pairwisef1 = mp.pairwiseforces(p1,p2,re,De,alpha)
    pairwisef2 = -pairwisef1

    # Initialise data lists for plotting later, first points
    time_list = [t]
    sep_list = [separ]
    energy_list = [energy]
    #Print out of important variables
    print(p1)
    print(p2)
    print(separ)

    # Start the time integration loop
    for i in range(tstep):
        # Update particle position
        p1.leap_pos2nd(dt, pairwisef1)
        p2.leap_pos2nd(dt, pairwisef2)

        #new forces
        prwsf1 = mp.pairwiseforces(p1,p2,re,De,alpha)
        prwsf2 = -prwsf1
        # Update particle velocity by averaging
        # current and new forces
        p1.leap_velocity(dt, 0.5*(pairwisef1+prwsf1))
        p2.leap_velocity(dt, 0.5*(pairwisef2+prwsf2))

        # Re-define force value
        pairwisef1 = prwsf1
        pairwisef2 = prwsf2

        # Increase time
        t += dt

        # Output particle information
        #energy
        energy = p1.kinetic_energy() + p2.kinetic_energy() + mp.potenergy(p1,p2,re,De,alpha)
        u_outfile.write("{},{} \n".format(t,energy))
        #separation
        separ = np.linalg.norm(Particle3D.separation(p1,p2))
        sep_outfile.write("{},{} \n".format(t,separ))

        # Append information to data lists
        time_list.append(t)
        sep_list.append(separ)
        energy_list.append(energy)


    # Post-simulation:
    # Close output file
    sep_outfile.close()
    u_outfile.close()

    # Plot particle trajectory to screen
    pyplot.title('Velocity Verlet: Separation vs time')
    pyplot.xlabel('Time (10.18fs)')
    pyplot.ylabel('Separation (Angstroms)')
    pyplot.plot(time_list, sep_list)
    pyplot.legend(['Total Separation of the two particles'],loc=2)
    pyplot.show()

    # Plot particle energy to screen
    pyplot.title('Velocity Verlet: total energy vs time')
    pyplot.xlabel('Time (10.18fs)')
    pyplot.ylabel('Energy (eV)')
    pyplot.plot(time_list, energy_list)
    pyplot.legend(['Total energy of the two particles'],loc=2)
    pyplot.show()


# Execute main method, but only when directly invoked
if __name__ == "__main__":
    main()
