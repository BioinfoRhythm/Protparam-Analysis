from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO

# Open a file for writing output
outfile = open('/Path to the file/protparam_analyais.txt','w')

# Counter for protein IDs
a = 0 

# Iterate over each sequence in the FASTA file
for seq in SeqIO.parse('/Path to the file/protein.fasta','fasta'):
    # print("protein id: ",seq.id)
    a+=1
    
    # Write protein ID to file
    outfile.write(f"protein id ({a}): {seq.id}")
    protein_sequence = seq.seq#"".join(f.read().splitlines())
    
    # Create a ProteinAnalysis object
    prot_param = ProteinAnalysis(protein_sequence)
    
    # Calculate various protein parameters
    count_aa = prot_param.count_amino_acids()
    percent_aa = prot_param.get_amino_acids_percent()
    molecular_weight = prot_param.molecular_weight()
    aromaticity = prot_param.aromaticity()
    flexibility = prot_param.flexibility()
    isoelectric_point = prot_param.isoelectric_point()
    secondary_structure_fraction = prot_param.secondary_structure_fraction()
    gravy = prot_param.gravy()
    instability_index = prot_param.instability_index()
    
    # Print the results
    outfile.write(f"\nCount of amino acids:{count_aa}")
    outfile.write(f"\nPercentage of amino acids:{percent_aa}")
    outfile.write(f"\nMolecular weight:{molecular_weight}")
    outfile.write(f"\nAromaticity:{aromaticity}")
    outfile.write(f"\nIsoelectric point:{isoelectric_point}")
    outfile.write(f"\nSecondary structure fraction:{secondary_structure_fraction}")
    outfile.write(f"\nGRAVY value:{gravy}")
    outfile.write(f"\nInstability index:{instability_index}")
    outfile.write(f"\nFlexibility:{flexibility}")
    outfile.write("\n")
    outfile.write('*'*40)
    outfile.write("\n\n")
outfile.close()
