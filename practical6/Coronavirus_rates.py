import matplotlib.pyplot as plt # to plot figure
corona={} #make an empty list
corona={'USA':30139457,'Brazil':11525477,'India':11409831,'Russia':4409438,'UK':5263527} #add the list value
Keyname=list(corona.keys()) #get all keys
coronavalue=list(corona.values()) #get all values
L=[]
total = 0

for i in coronavalue: #calculate total
    total += i
#print(total)

for i in coronavalue:    #form new list
    L.append(i / total)
dictionary = dict(zip(Keyname, L))   #form new dictionary with two lists
print("origin table")
print(corona)
print("frequency dic")
print(dictionary)
fig, ax1 = plt.subplots() #define row number and line number
ax1.pie(coronavalue, labels=Keyname, autopct='%.1f%%', pctdistance=0.7, shadow=True, startangle=90) #input value and define style
ax1.axis('equal')
plt.show()