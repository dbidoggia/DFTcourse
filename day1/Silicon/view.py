from ase.io import read
from ase.visualize import view

atoms = read('si.scf.out')

print(atoms.get_potential_energy())
view(atoms)