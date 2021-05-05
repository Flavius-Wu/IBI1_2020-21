# 3. Untranslated length calculator
import re
def untranslated():
	mRNA_seq = input('Please input a mRNA sequence: ')
	# start codon is AUG
	start_codon = 'ATG'
	stop_codon = input('Please input the stop codon: ')
	stop_codon = re.sub(r'U', 'T', stop_codon)
	mRNA_seq = re.sub(r'U', 'T', mRNA_seq)
	length = len(mRNA_seq)
	cut = re.split(stop_codon, mRNA_seq)
	goal = []
	for i in cut:
		goal1 = re.findall('(?<=ATG).*$', i)
		goal.append(goal1)
	count = 0
	for i in goal:
		count = count + len(i) + 6
	result = ((length - count) / length) * 100
	print('The percentage of untranslated sequence is ', result, '%.')
untranslated()

# ACACACACACACATGCGCGCGCGCGCGCGCGCGCGCGTGACACACACACACAC
# stop codon: TGA
