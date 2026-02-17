import os
import numpy as np
from ase.io import read

# Create the "eos" directory to store input/output files for different lattice parameters
os.makedirs("eos", exist_ok=True)

dists = []
energies = []

# Loop over different lattice parameters, create input files, and run calculations
for x in np.arange(3.8, 4.5, 0.06):
    x = round(x, 2)
    
    # Note: f-strings allow embedding variables directly inside curly braces {}
    print(f"Running calculation for distance = {x} Angstrom", end="\r")
    
    # Create an input file for the current lattice parameter
    # Use f-strings to insert the value of 'x' into the input file content
    with open(f"eos/cscl_{x}.in", "w") as f:
        f.write(f"""
&CONTROL
  calculation = 'scf'
  outdir = './outdirs/'
  prefix = 'cscl_{x}'
  pseudo_dir = '../../pseudo/'
/
&SYSTEM
  ecutrho =   240
  ecutwfc =   30
  ibrav = 0
  nat = 2
  ntyp = 2
/
&ELECTRONS
  conv_thr =   1.0d-6
  electron_maxstep = 80
  mixing_beta =   0.4
/
ATOMIC_SPECIES
Cl     35.453       cl_pbesol_v1.4.uspp.F.UPF
Cs     132.9054519  cs_pbesol_v1.uspp.F.UPF
ATOMIC_POSITIONS crystal
Cs           0.0000000000       0.0000000000       0.0000000000
Cl           0.5000000000       0.5000000000       0.5000000000
K_POINTS automatic
2 2 2 0 0 0
CELL_PARAMETERS angstrom
      {x}       0.0000000000       0.0000000000
      0.0000000000       {x}       0.0000000000
      0.0000000000       0.0000000000       {x}
""")
    # Run the calculation using pw.x (same command used in the terminal)
    os.system(f"pw.x < eos/cscl_{x}.in > eos/cscl_{x}.out")



    # Read the output file of Quantum ESPRESSO
    atoms = read(f"eos/cscl_{x}.out")
    # Extract the total energy from the output file
    energy = atoms.get_potential_energy()

    dists.append(x)
    energies.append(energy/13.6058)  # Convert energy from eV to Rydberg
    
# Save the results to a text file for later analysis
np.savetxt("eos/eos.dat", np.column_stack((dists, energies)), header="Distance (Angstrom)    Energy (Ry)")