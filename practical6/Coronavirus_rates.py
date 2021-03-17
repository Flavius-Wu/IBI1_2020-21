import matplotlib.pyplot as plt # to plot figure
corona={} #make an empty list
corona={'USA':30139457,'Brazil':11525477,'India':11409831,'Russia':4409438,'UK':5263527} #add the list value
Keyname=(corona.keys()) #get all keys
coronavalue=(corona.values()) #get all values
fig, ax1 = plt.subplots() #define row number and line number
ax1.pie(coronavalue, labels=Keyname, autopct='%.1f%%', pctdistance=0.7, shadow=True, startangle=90) #input value and define style
ax1.axis('equal')
plt.show()