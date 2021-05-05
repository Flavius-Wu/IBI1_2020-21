# 4. Exon length calculator
import re
def exon_length_calculator():
	DNA_seq = input('Enter a DNA sequence: ')
	total_length = len(DNA_seq)
	intron = re.findall(r'GT[AGCT]+?AG', DNA_seq)
	intron_length = 0
	for i in intron:
		intron_length = intron_length + len(i)
	axon_p = (1 - intron_length/total_length)*100
	print('The percentage is ', axon_p, '%.')
exon_length_calculator()

# 1.intron-exon-intron-exon-intron-exon: GTCGCGCAGTTTTGTCCAGTTTTTTTTTTTTGTCCCAGCCCCCC
# 2.intron-exon-intron-exon-intron: GTCGAGTTTAAACCGTCCAGTTTTTTTGTACACAG
# 3.exon-intron-exon-intron-exon-intron: TTTTTTGTCCAGTTTTTTGTCCAGAAAAAAGTCCCAG
# 4.exon-intron-exon-intron-exon: TTTTGTCCAGTTTTTTGTCCAGTTTTT