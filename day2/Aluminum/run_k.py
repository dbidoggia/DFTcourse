import os  

os.makedirs('k', exist_ok=True)

start = 1
end = 10
step = 1

for k in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:

    with open(f'k/al_{k}.in', 'w') as f:
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
    ecutwfc    = ....., 
    occupations= 'smearing',
    smearing   = 'marzari-vanderbilt',
    degauss    = 0.06
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
    os.system(f"pw.x -inp k/al_{k}.in > k/al_{k}.out")