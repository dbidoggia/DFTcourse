from ase.io import read  # Import ASE's read function to parse atomic structure files
import os  # Import os module for file operations

# Clean up: Remove any existing equation of state data file to avoid appending to old data
if os.path.exists('alat/eos.dat'):
    os.remove('alat/eos.dat')

# Loop through a range of lattice parameters (in atomic units, i.e. Bohr radii) for silicon
# This will sample the energy at different lattice constants to build an equation of state
start = 8.0
end = 13.0
step = 0.1

for a in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:
    # Read the structure from the corresponding output file for this lattice parameter
    structure = read(f'alat/silicon_{a}.out')
    
    # Open the equation of state data file in append mode ('a')
    # We append each new data point to build the complete dataset
    with open(f'alat/eos.dat', 'a') as f:
        # Write the lattice parameter and corresponding potential energy (in eV) to the file
        # Format: <lattice_parameter> <energy>
        f.write(f'{a} {structure.get_potential_energy()}\n')