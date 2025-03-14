from ase.io import read 
import os

if os.path.exists('k/etot_k.dat'):
    os.remove('k/etot_k.dat')

start = 1
end = 20
step = 1

for k in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    structure = read(f'k/al_{k}.out')
    
    with open(f'k/etot_k.dat', 'a') as f:
        f.write(f'{k} {structure.get_potential_energy()}\n')