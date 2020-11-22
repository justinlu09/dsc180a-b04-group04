import pandas as pd
import os
import shutil

def generate_gene_mat(kallisto_out, gene_matrix_out):
    
    gene_matrix = pd.DataFrame()
    
    if ('.ipynb_checkpoints' in os.listdir(kallisto_out)):
        shutil.rmtree(os.path.join(kallisto_out, '.ipynb_checkpoints'))
    
    for i in sorted(os.listdir(kallisto_out)):
        SRR_path = os.path.join(kallisto_out, i)
        abundance_tsv = os.path.join(SRR_path, 'abundance.tsv')
        abundance = pd.read_csv(abundance_tsv, sep = '\t')['tpm']
        gene_matrix[i] = abundance

    
    gene_matrix.index = pd.read_csv(os.path.join(kallisto_out, i, 'abundance.tsv'), sep = '\t')['target_id']
    gene_matrix.index.name = 0
    
    gene_matrix.to_csv(gene_matrix_out)
    
    return