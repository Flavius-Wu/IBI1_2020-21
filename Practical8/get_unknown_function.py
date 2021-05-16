import re
fastq = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
#open the file
count = 0
all=''
names=[]
number=[]
dic={}
for line in fastq:
#read file line by line
        s=str(line)
        if re.search('>',line):
            #chech if the line start with >
            #put the gene name as a dictionary key
            key=line
            dic[key]=''
        else:
            #add the contain of the gene to the dictionary value
            ori=dic[key]
            dic[key]=ori + line

for key in dic.keys():
    #go through every key
    if re.search('unknown function',key):
        #get the gene with unknown function
        name = str(key)
        output = re.findall(r'^>([^ ]+)_mRNA',key)
        #get the text we want
        value = str(dic[key])
        value = value.replace('\n', '').replace('\r', '')
        #get rid of line breaks
        print(output,len(value))
        print(dic[key])
file=open('unknown_function.fa','w')
#write the file as above method described
for key in dic.keys():
    if re.search('unknown function',key):
        name = str(key)
        output = re.findall(r'^>([^ ]+)_mRNA',key)
        value = str(dic[key])
        value = value.replace('\n', '').replace('\r', '')
        value =str(len(value))
        output=str(output)
        file.write(output)
        file.write(value)
        file.write('\n')

        file.write(dic[key])


file.close()