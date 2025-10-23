import os
import glob
import subprocess

input_folder = "/home/pastore29/Desktop/Dolastatine/dol_pdb"
output_folder = "/home/pastore29/Desktop/Dolstatine/dol_pdbqt"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

sdf_files = glob.glob(os.path.join(input_folder, "*.sdf"))

for sdf_file in sdf_files:
    try:
        output_file = os.path.join(output_folder, os.path.basename(sdf_file).replace(".sdf", ".pdb"))
        subprocess.run(["obabel", "-i", "sdf", sdf_file, "-o", "pdb", "-O", output_file, "-xh"], check=True)
        print(f"Converted {sdf_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion of {sdf_file}: {e}")

