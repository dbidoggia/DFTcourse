from ase.io import read 
import os



start_k = 4
end_k = 16
step_k = 4

start_degauss = 0.01
end_degauss = 0.15
step_degauss = 0.02

for k in  [round(start_k + i * step_k,2) for i in range(int((end_k - start_k) / step_k) + 1)]:
     if os.path.exists(f'k_degauss/etot_k{k}_degauss.dat'):
        os.remove(f'k_degauss/etot_k{k}_degauss.dat')
     for degauss in  [round(start_degauss + i * step_degauss,2) for i in range(int((end_degauss - start_degauss) / step_degauss) + 1)]:
         
            structure = read(f'k_degauss/al_{k}_{degauss}.out')
    
            with open(f'k_degauss/etot_k{k}_degauss.dat', 'a') as f:
                f.write(f'{degauss} {structure.get_potential_energy()}\n')