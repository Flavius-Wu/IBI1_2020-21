# DNA sequence molecular weight calculator.
# Used to determine molecular weight of a PCR primer.
# The molecular weight of the primer can be used to prepare the primer solution of a certain concentration.

seq = input("Enter a DNA primer:")
seq = seq.upper()

#build a dictionary, molecular weight for NT
dic = {'A': 331.22, 'G': 347.22,
       'C': 307.20, 'T': 322.21}
weight1 = 0

#add the NT weight one after another
for i in range(0, len(seq)):
    #find the corresponding nnumber in dic.
    weight1 += dic[seq[i]]

#H2O(18),exclude the water mass,    
#genrated after polycondensation
weight2 = weight1 - 18 * (len(seq) - 1)
print('Molecular weight in g/mol:', weight2)
