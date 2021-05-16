import re
seq ='ATGCGACTACGATCGAGGGCC'
prot=''
#import the codon table
codon_table = {'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',
          'TTC':'F','TCC':'S', 'TAC':'Y', 'TGC':'C',
          'TTA':'L','TCA':'S','TAA':'O','TGA':'X',
          'TCG':'S', 'TAG':'U', 'TGG':'W', 'CTT':'L',
          'CCT':'P', 'CAT':'H', 'CGT':'R','CTC':'L',
          'CCC':'P', 'CAC':'H', 'CGC':'R','ATT': 'I',
          'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',
          'CTG':'L', 'CCG':'P', 'CAG':'Z', 'CGG':'R',
          'ACT':'T', 'AAT':'N','AGT':'S','ATC':'I',
          'ACC':'T', 'AAC':'B', 'AGC':'S','ATA':'J',
          'ACA':'T','AAA':'K', 'AGA':'R','ATG': 'M',
          'ACG':'T', 'AAG':'K', 'AGG':'R','GTT':'V',
          'GCT':'A', 'GAT':'D', 'GGT':'G','GTC':'V',
          'GCC':'A', 'GAC':'D', 'GGC':'G','GTA':'V',
          'GCA':'A', 'GAA':'E', 'GGA':'G','GTG':'V',
          'GCG':'A', 'GAG':'E', 'GGG':'G','TTG':'L'}


for i in range(0,len(seq)+3,3):
    #read the sequence three by three
    #print(i) no use in the program for test use only
    codon = seq[:i]
    #each time 3 NT more
    #print(codon)no use in the program for test use only
    #get the last three
    codon = codon[-3:]
    #print(codon)no use in the program for test use only
    if codon in codon_table:
        prot = prot + codon_table[codon] +' '
print(prot)


