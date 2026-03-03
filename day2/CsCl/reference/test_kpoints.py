import os
import numpy as np
from ase.io import read

parameter = 'kpoints'

os.makedirs(parameter, exist_ok=True)

params = []
energies = []

for x in np.arange(1, 10, 1):
    x = round(x, 2)
    
    print(f"Running calculation for {parameter} = {x}", end="\r")
    prefix = f"cscl_{x}"
    
    with open(f"{parameter}/{prefix}.in", "w") as f:
        f.write(f"""
&CONTROL
  calculation = 'scf'
  outdir = './outdirs/'
  prefix = '{prefix}'
  pseudo_dir = '../../pseudo/'
/
&SYSTEM
  ecutrho =   320   !typically 4 times ecutwfc for norm-conserving, 8 for ultrasoft pseudos (we are using ultrasoft (uspp in the name of psedos)) 
  ecutwfc =   40     !cutoff energy for wavefunctions (in Ry)
  ibrav = 1           !cubic
  celldm(1) = 7.8243  !extracted from day1 eos (in bohr)
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
{x} {x} {x} 0 0 0
!CELL_PARAMETERS angstrom
!      4.1404500000       0.0000000000       0.0000000000
!      0.0000000000       4.1404500000       0.0000000000
!      0.0000000000       0.0000000000       4.1404500000
""")

    os.system(f"pw.x < {parameter}/{prefix}.in > {parameter}/{prefix}.out")

    atoms = read(f"{parameter}/{prefix}.out")
    energy = atoms.get_potential_energy()

    params.append(x)
    energies.append(energy)
energies = np.array(energies) - energies[-1]  # Shift energies so that the last one is zero (reference)
np.savetxt(f"{parameter}.dat", np.column_stack((params, energies)), header="Parameter    Energy (eV)")
