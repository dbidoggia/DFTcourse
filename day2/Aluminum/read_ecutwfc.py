from ase.io import read 
import os

if os.path.exists('ecutwfc/etot_ecutwfc.dat'):
    os.remove('ecutwfc/etot_ecutwfc.dat')

start = 20
end = 200
step = 10

for ecutwfc in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    structure = read(f'ecutwfc/al_{ecutwfc}.out')
    
    with open(f'ecutwfc/etot_ecutwfc.dat', 'a') as f:
        f.write(f'{ecutwfc} {structure.get_potential_energy()}\n')