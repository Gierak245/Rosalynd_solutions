# -*- coding: utf-8 -*-
"""
@author: giera
"""

import re  # for regex
import requests  # for API

# [XY] means "either X or Y" and {X} means "any amino acid except X." 
# For example, the N-glycosylation motif is written as N{P}[ST]{P}.

def protein_motif(IDS_url):
    
    # opening file with IDS for protein motif saved
    with open(IDS_url, 'r') as file:
        ID_list = [line for line in file]

    # creating a listo for storing a positions where motif is present
    positions = []
    start = 0
    
    
    seq_with_positions ={}
    
    
    for ID in ID_list:
        
        # Deleting everything from first "_" occurance because it's not worting with API
        new_ID = re.sub("_[A-Za-z0-9]*", "", ID)
        
        positions = []
        start = 0
        pattern = r'N[^P][ST][^P]'
        new_ID = new_ID.strip()  # deleting "\n" at the end of every line
        
        # Downloading fasta files and getting seqence of a gene
        fasta_file = requests.get(f'https://rest.uniprot.org/uniprotkb/{new_ID}.fasta').text.splitlines()
        seq = ''.join(str(line) for line in fasta_file[1:]) 
        
        # iteration trought sequence and adppending match position to the list 
        while start < len(seq) - 4:
            
            string = seq[start:start + 4]
            
            if re.match(pattern, string):
                positions.append(seq.find(string) + 1)  # using .find() to find position of matched pattern 
                start += 1
            else:
                start += 1
    
        seq_with_positions[ID.strip()] = positions
    
    for key,value in seq_with_positions.items():
        print(key)
        print(value)
    
    return seq_with_positions

path = "C:/users/giera/onedrive/dokumenty/python_scripts/rosalind_mprt.txt"
result = protein_motif(path)
    