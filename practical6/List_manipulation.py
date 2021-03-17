from numpy import *     #use this for divide number
import matplotlib.pyplot as plt  # to plot figure
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981] #make list for gene_lengths
exon_counts=[51,1142,42,216,25,650,32533,57,1,523] #make list for exon_counts
average_exon_length=[a/b for a,b in zip(gene_lengths,exon_counts)]  #count for average
gene_lengths_sorted=sorted(average_exon_length) #sort the order
print(gene_lengths_sorted) #print the order
plt.figure(figsize=(5,10))  #define the figure size
plt.title('List_manipulation',fontsize=20) #define the figure title
plt.boxplot(gene_lengths_sorted) #plot the figure
plt.show()
