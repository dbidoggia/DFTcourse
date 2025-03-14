import os  

os.makedirs('k_degauss', exist_ok=True)

start_k = 4
end_k = 16
step_k = 4

start_degauss = 0.01
end_degauss = 0.15
step_degauss = 0.02

for k in  [round(start_k + i * step_k,2) for i in range(int((end_k - start_k) / step_k) + 1)]:
      for degauss in  [round(start_degauss + i * step_degauss,2) for i in range(int((end_degauss - start_degauss) / step_degauss) + 1)]:
         
         with open(f'k_degauss/al_{k}_{degauss}.in', 'w') as f:
            f.write(f"""
 &control
    prefix     = 'al'
    outdir     = './outdirs'
    pseudo_dir = '../../pseudo',
 /
 &system    
    ibrav      = 2,
    celldm(1)  = 7.50,
    nat        = 1,
    ntyp       = 1,
    ecutwfc    = 60, 
    occupations= 'smearing',
    smearing   = 'marzari-vanderbilt',
    degauss    = {degauss}
 /
 &electrons
 /
ATOMIC_SPECIES
 Al  26.98 Al.pz-vbc.UPF
ATOMIC_POSITIONS alat
 Al 0.00 0.00 0.00 
K_POINTS automatic
  {k} {k} {k} 1 1 1                
""")
    # Run Quantum ESPRESSO (pw.x) with the generated input file
    # Redirect output to corresponding output file for later analysis
         os.system(f"pw.x -inp k_degauss/al_{k}_{degauss}.in > k_degauss/al_{k}_{degauss}.out")