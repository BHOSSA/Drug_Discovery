# --- SECTION 1: Ligand Similarity Search (ChEMBL) ---

from chembl_webresource_client.new_client import new_client
import pandas as pd

# Initialize ChEMBL client
molecule = new_client.molecule
activity = new_client.activity
similarity = new_client.similarity

# Define the SMILES string for FMN (Flavin mononucleotide)
fmn_smiles = 'CC[C@H](C)[C@@H]([C@@H](CC(=O)N1CCC[C@H]1[C@H](OC)[C@@H](C)C(=O)N[C@@H](Cc1ccccc1)c1nccs1)OC)N(C)C(=O)[C@@H](NC(=O)[C@H](C(C)C)N(C)C)C(C)C'

# Fetch similar ligands to FMN from ChEMBL (≥70% similarity)
similar_ligands = similarity.filter(smiles=fmn_smiles, similarity=70)

print(f"Found {len(similar_ligands)} similar ligands in ChEMBL.")
