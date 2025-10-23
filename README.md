# 🧪 FMN Ligand Similarity and Structure Conversion Pipeline

This repository automates the process of finding and converting **ligands similar to Flavin mononucleotide (FMN)** using **ChEMBL**, **PubChem**, and **Open Babel**.  
It performs similarity search, data retrieval, and structural file conversion for molecular modeling or docking workflows.

---

## 📊 Workflow Overview

1. **Ligand Similarity Search (ChEMBL)**  
   Retrieve ligands with ≥70% similarity to FMN.

2. **PubChem Data Retrieval**  
   Download molecular data in `.sdf` format and export basic information (`dol.csv`).

3. **Structure Conversion (Open Babel)**  
   Convert `.sdf` → `.pdb` format for visualization or docking simulations.

---

## ⚙️ Requirements

Install dependencies:
```bash
pip install -r requirements.txt
