# 2. Open Reading Frame length calculator

import re
#define a function for calculating
def ORF_length_calculator():
        mRNA_seq = input('Please input a mRNA sequence: ')

	# Only exist one start codon AUG
        start_codon = 'ATG'
	# Choose one of three stop codon 
        stop_codon = input('Please input the stop codon: ')

	#transfer all 'U' to 'T'
        stop_codon = re.sub(r'U', 'T', stop_codon)
        mRNA_seq = re.sub(r'U', 'T', mRNA_seq)
	#calculate the length
        length = len(mRNA_seq)
	
	#split the seq. by stop codon
	#form a list
        cut = re.split(stop_codon, mRNA_seq)
        goal = []
	#Find the seq. start from 'AUG'
        for i in cut:
                goal1 = re.findall('(?<=ATG).*$', i)
                goal.append(goal1)
        count = 0
	#count each seq. length
        for i in goal:
                count = count + len(i) + 6
	#calculate the percantage
        result = (count / length) * 100
        print('The percentage of ORF length is', result, '%.')
ORF_length_calculator()

# TTTATGCCCCCCCCCTGAAAAATGCCCCCCCCCTGAATGCCCCCCCCCTGACCCCC
# stop codon: TGA
