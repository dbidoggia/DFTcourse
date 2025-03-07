
import os
import numpy as np

os.makedirs('alat', exist_ok=True)

for alat in np.arange(8, 13, 0.1):
    with open(f'alat/silicon_{alat}.in', 'w') as f:
        f.write(f"""
""")
    os.system(f"pw.x ...")