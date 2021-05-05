# 1. Exon counter

import re
#imput the sequence as a string
seq = input('Enter a DNA sequence:')
#convert lower letters to upper
seq = seq.upper()
#split the string into a list
#based on regular expression 'GT...AG'
exon = re.split(r'GT[AGCT]+?AG', seq)
#remove all the blank space
while '' in exon:
    exon.remove('')
#count and print the exon number
print('Exon number:', len(exon))

# 1.intron-exon-intron-exon-intron-exon: GTCGCGCAGTTTTGTCCAGTTTTTTTTTTTTGTCCCAGCCCCCC
# 2.intron-exon-intron-exon-intron: GTCGAGTTTAAACCGTCCAGTTTTTTTGTACACAG
# 3.exon-intron-exon-intron-exon-intron: TTTTTTGTCCAGTTTTTTGTCCAGAAAAAAGTCCCAG
# 4.exon-intron-exon-intron-exon: TTTTGTCCAGTTTTTTGTCCAGTTTTT
