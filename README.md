## Protein Parameter Analysis with ProtParam
This repository contains a Python script for analyzing protein parameters using Biopython's ProtParam module. The script calculates various physicochemical properties of proteins from a FASTA file and writes the results to an output text file.
## Requirements
Python 3.x

Biopython (install via pip install biopython)

## Input

Place your protein sequences in a FASTA format file named protein.fasta inside a directory.
Run the script:
     python3 protparam_analysis.py
The script will analyze each protein sequence, calculate its parameters, and write the results to protparam_analysis.txt in the directory.

## Output
protparam_analysis.txt: Contains the calculated parameters for each protein sequence, including count and percentage of amino acids, molecular weight, aromaticity, isoelectric point, secondary structure fraction, GRAVY value, instability index, and flexibility.

## Citation
If you are using the protparam_analysis.py script for your research, please consider citing it as follows: Sharma, R. (2024).ncbi_genome_downloader.py . Retrieved from https://github.com/BioinfoRhythm/protparam_analysis.py

## Acknowledgments
Biopython developers for providing the ProtParam module.
