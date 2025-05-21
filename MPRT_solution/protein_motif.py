# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 19:34:40 2025

@author: giera
"""

# common protein motif

import re  # for regex
import requests  # for API

# [XY] means "either X or Y" and {X} means "any amino acid except X." 
# For example, the N-glycosylation motif is written as N{P}[ST]{P}.

# x = 'ATGCCATGCCAGTGATCCAGTGAGCC'

# pattern = 'CC'

# matches = re.finditer(pattern, x)

# # for i in matches:
# #     print(i.start())    
# z = [match.start() for match in matches]

# string = 'P07204_TRBM_HUMAN'

# url użyty do testowania
# url_test = "https://rest.uniprot.org/uniprotkb/P07204.fasta"

# path = "C:/Users/giera/Downloads/ids.txt"

# # Wczytanie wszystkich ID
# with open(path, 'r') as file:
#     ID_list = [re.sub("_[A-Za-z0-9]*", "",line) for line in file]

# # Wysyłanie zapytania do API w celu uzyskania sekwencji fasta
# fasta_file = requests.get(url_test).text.splitlines()

# # Wydobycie sekwencji z pliku fasta
# seq = ''.join(str(line) for line in fasta_file[1:]) 

# # Wzór naszego szukanego motywu białka
# pattern = r'N[^P][ST][^P]'

# matches = re.finditer(pattern, seq)  # niestety, po znalezieniu patternu pomija dany kawałek przez co
#                                      # pomija też jeden z pasujących odczytów.




# positions = []
# start = 0

# seq_with_positions ={}


# for ID in ID_list:
    
#     positions = []
#     start = 0
#     pattern = r'N[^P][ST][^P]'
#     ID = ID.strip()  # usunięcie "\n" na końcu linii
    
#     # Pobranie pliku fasta i wydobycie sekwencji
#     fasta_file = requests.get(f'https://rest.uniprot.org/uniprotkb/{ID}.fasta').text.splitlines()
#     seq = ''.join(str(line) for line in fasta_file[1:]) 
    
#     # iteracja przez sekwencję po 4 nukl i dodanie pozycji do listy gdy pasuje do patternu
#     while start < len(seq) - 4:
        
#         string = seq[start:start + 4]
        
#         if re.match(pattern, string):
#             positions.append(seq.find(string) + 1)  # wykorzystanie .find() by znaleźć pozycję patternu
#             start += 1
#         else:
#             start += 1

#     seq_with_positions[ID] = positions

# for i,j in seq_with_positions.items():
#     print(i)
#     print(j)

# Looking for precision protein motif N{P}[ST]{P}

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

path = "C:/Users/giera/Downloads/rosalind_mprt(1).txt"
result = protein_motif(path)
    
