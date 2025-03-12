import os  # Import os module for directory/file operations and system commands

# Create a directory named 'alat' to store input and output files for all calculations
# exist_ok=True prevents an error if the directory already exists
os.makedirs('alat', exist_ok=True)

# Loop through a range of lattice parameters (in Bohr radii) for silicon
# This range will allow us to find the equilibrium lattice constant by sampling around it
start = 8.0
end = 13.0
step = 0.1

for a in  [round(start + i * step,2) for i in range(int((end - start) / step) + 1)]:
    # Create a Quantum ESPRESSO input file for this lattice parameter writing the content to a new file
    with open(f'alat/silicon_{a}.in', 'w') as f:
        f.write(f"""
 &control
    prefix        = 'silicon',      
    calculation   = 'scf',          
    pseudo_dir    = '../../pseudo', 
    outdir        = './outdirs'     
 /
 &system    
    ibrav         = 2,              
    celldm(1)     = {a},            
    nat           = 2,              
    ntyp          = 1,              
    ecutwfc       = 12.0,           
 /
 &electrons
 /
ATOMIC_SPECIES
 Si  28.086  Si.pz-vbc.UPF          
ATOMIC_POSITIONS alat
 Si 0.00 0.00 0.00                  
 Si 0.25 0.25 0.25                  
K_POINTS automatic
  2 2 2 1 1 1                       
""")
    # Run Quantum ESPRESSO (pw.x) with the generated input file
    # Redirect output to corresponding output file for later analysis
    os.system(f"pw.x -inp alat/silicon_{a}.in > alat/silicon_{a}.out")