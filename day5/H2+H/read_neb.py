from ase.io import read, write
import os

if os.path.exists('neb/etot_xpos.dat'):
    os.remove('neb/etot_xpos.dat')

start = -1.5
end = 1.5
step = 0.2
trajectory = []
energies = []

with open(f'neb/etot_xpos.dat', 'w') as f:
    f.write(f'#xpos (Ang)       Etot (eV)\n')

for ii, xpos in  enumerate([round(start + i * step,2) for i in range(int((end - start) / step) + 1)]):
    
        structure = read(f'neb/h2+h_{ii}.out')
        trajectory.append(structure)
        energies.append(structure.get_potential_energy())

        with open(f'neb/etot_xpos.dat', 'a') as f:
            f.write(f'{xpos} {structure.get_potential_energy()}\n')

write('neb/trajectory.traj', trajectory)
print(f'Energy barrier: {round(max(energies) - min(energies),2)} eV')