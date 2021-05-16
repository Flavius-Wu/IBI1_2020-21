import re
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
prot=''
seq=''

filename=input('please import your filename')
#Asks the user to input	a filename as the new fasta file
filename = filename+'.fa'
#make it as a FASTA file
fastq = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
count = 0
all=''
names=[]
number=[]
dic={}
file=open(filename,'w')
for line in fastq:
#read the file line by line
        s=str(line)
        if re.search('>',line):
            #if the line start with > make it as a key
            key=line
            dic[key]=''
        else:
            #put the following thing as value
            ori=dic[key]
            dic[key]=ori + line

for key in dic.keys():
    if re.search('unknown function',key):
        output = re.findall(r'^>([^ ]+)_mRNA',key)
        output = str(output)
        seq=str(dic[key])
        seq=seq.replace('\n', '').replace('\r', '')
        if len(seq)%3 == 0 :
            #select the	DNA	sequence is	made up	of complete	codons
            file.write(output)
            #transcribe DNA to amino acid as task1 described
            for i in range(0, len(seq) + 3, 3):
                codon = seq[:i]
                codon = codon[-3:]
                if codon in codon_table:
                    prot = prot + codon_table[codon] + ' '
            length = str(len(prot))
            file.write(length)
            file.write('\n')
            file.write(prot)
            file.write('\n')

file.close()





