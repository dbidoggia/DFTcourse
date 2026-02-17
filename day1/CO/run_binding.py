import os
import numpy as np
from ase.io import read

# Create the "binding" directory to store input/output files for different lattice parameters
os.makedirs("binding", exist_ok=True)

dists = []
energies = []

# Loop over different lattice parameters, create input files, and run calculations
for x in np.arange(1., 1.3, 0.03):
    x = round(x, 2)
    
    # Note: f-strings allow embedding variables directly inside curly braces {}
    print(f"Running calculation for distance = {x} Angstrom", end="\r")
    
    # Create an input file for the current lattice parameter
    # Use f-strings to insert the value of 'x' into the input file content
    with open(f"binding/co_{x}.in", "w") as f:
        f.write(f"""
&CONTROL
...
""")
    # Run the calculation using pw.x (same command used in the terminal)
    os.system(f"pw.x < binding/co_{x}.in > binding/co_{x}.out")



    # Read the output file of Quantum ESPRESSO
    atoms = read(f"binding/co_{x}.out")
    # Extract the total energy from the output file
    energy = atoms.get_potential_energy()

    dists.append(x)
    energies.append(energy)
    
# Save the results to a text file for later analysis
np.savetxt("binding/binding.dat", np.column_stack((dists, energies)), header="Distance (Angstrom)    Energy (eV)")