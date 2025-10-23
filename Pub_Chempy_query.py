# --- SECTION 2: PubChem Query and Data Export ---

import pubchempy as pcp
from tqdm import tqdm
import os
import requests

# Initialize storage variables
data = []
ligand_index = 1

# Create output folder for .sdf files
output_folder = '/home/pastore29/Desktop/Dolastatine'
os.makedirs(output_folder, exist_ok=True)

# Loop through similar ligands and fetch PubChem info
for ligand in tqdm(similar_ligands):
    smiles = ligand['molecule_structures']['canonical_smiles']
    chembl_id = ligand['molecule_chembl_id']
    
    try:
        compounds = pcp.get_compounds(smiles, 'smiles')
        if compounds:
            compound = compounds[0]
            ligand_name = compound.iupac_name or "N/A"
            cid = compound.cid

            # Download SDF file from PubChem
            url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF"
            response = requests.get(url)
            response.raise_for_status()
            sdf_data = response.text
            
            sdf_filename = os.path.join(output_folder, f"Dol_{ligand_index}.sdf")
            with open(sdf_filename, 'w') as sdf_file:
                sdf_file.write(sdf_data)
            
            data.append([f"FMN_{ligand_index}", ligand_name, chembl_id])
            ligand_index += 1
        else:
            print(f"No compound found for SMILES: {smiles}")
    except Exception as e:
        print(f"Error querying PubChem for ligand {smiles}: {e}")
        continue

# Save collected data to CSV
if data:
    df = pd.DataFrame(data, columns=['ligand_index', 'ligand_name', 'chembl_id'])
    csv_output_path = os.path.join(output_folder, 'dol.csv')
    df.to_csv(csv_output_path, index=False)
    print(f"Saved {len(data)} ligands to {csv_output_path}")
else:
    print("No data was collected.")
