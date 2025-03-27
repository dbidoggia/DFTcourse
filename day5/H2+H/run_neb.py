import os  

os.makedirs('neb', exist_ok=True)

start = -1.5
end = 1.5
step = 0.2

for ii, xpos in  enumerate([round(start + i * step,2) for i in range(int((end - start) / step) + 1)]):
    print(f'Calculation {ii+1}/{int((end - start) / step)+1}')
    with open(f'neb/h2+h_{ii}.in', 'w') as f:
        f.write(f"""
&CONTROL
  outdir = './outdirs'
  prefix = 'H2+H'
  pseudo_dir = '../../pseudo'
/
&SYSTEM
  ibrav                  = 0,
  nat                    = 3,
  ntyp                   = 1,
  ecutwfc                = 20.0D0,
  ecutrho                = 100.0D0,
  nspin                  = 2,
  starting_magnetization = 0.5D0,
  occupations            = "smearing",
  degauss                = 0.03D0,
/
&ELECTRONS
  conv_thr    = 1.D-6,
  mixing_beta = 0.7D0,
/
&IONS
/
ATOMIC_SPECIES
H  1.00794  H.pbe-rrkjus_psl.1.0.0.UPF
ATOMIC_POSITIONS angstrom
H       -2.00000000       0.00000000       0.00000000
H        {xpos}           0.00000000       0.00000000
H        2.00000000       0.00000000       0.00000000
K_POINTS automatic
  1 1 1 0 0 0
CELL_PARAMETERS angstrom
  10.00000  0.00000  0.00000
   0.00000  5.00000  0.00000
   0.00000  0.00000  5.00000
            
""")
    # Run Quantum ESPRESSO (pw.x) with the generated input file
    # Redirect output to corresponding output file for later analysis
    os.system(f"mpirun -np 1 pw.x -inp neb/h2+h_{ii}.in > neb/h2+h_{ii}.out")