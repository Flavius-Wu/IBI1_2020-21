from xml.dom.minidom import parse
import re
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

doc= parse('go_obo.xml')
# get rootnode
root=doc.documentElement
terms=root.getElementsByTagName('term')
dic_def = {}
#store the relationship between id and its description
dic_a = {}
#store the relationship between id and is_a
for term in terms:
    id = term.getElementsByTagName("id")[0]
    id_inf=id.childNodes[0].data
    # get the id in each terms
    #print(id.childNodes[0].data) # !!!!write for test use only
    description = term.getElementsByTagName("defstr")[0]
    #get the corresponding description for each id
    #print(description.childNodes[0].data) # !!!!write for test use only
    des_inf =description.childNodes[0].data
    dic_def[id_inf]=des_inf
    # build a dictionary for the relationship between id and its description
    is_a = term.getElementsByTagName("is_a")
    # get the corresponding is_a for each id
    list1=[]
    #multiple is_a existed, use a list to store them
    for i in is_a:
        #print("is_a",i.childNodes[0].data)
        list1.append(i.childNodes[0].data)
    dic_a[id_inf]=list1
    # build a dictionary for the relationship between id and its is_a

#print(dic_a) # !!!!write for test use only

key = input('please input the keyword')
# the DNA, RNA, and protein have been put and the outcomes were taken
#oligosaccharide is the fourth macromolecule
dic_temp = {}
for i in dic_def.keys():
    if re.search(key, dic_def[i]):
        #test if the 'DNA' or other intended keynames existed
        value = dic_def[i]
        dic_temp[i] = value
array = dic_temp.keys()
#A list store all the key related ids
#print(array) # !!!!write for test use only
sum_array =[]
for id_name in array:
    #take one ids at a time
    #print('id_name',id_name)  # !!!!write for test use only
    count = 0
    fathernode = []
    for k in dic_a:
        if id_name in dic_a[k]:
            #test whether fathernodes exist
            count = count + 1
            fathernode.append(k)
            #store its fathernodes in a list
    fathernode_temp = fathernode[:]
    # print(fathernode_temp) # !!!!write for test use only
    sum_up = count
    while sum_up != 0 :
        sum_up = 0
        fathernode = []
        for j in fathernode_temp:
            for q in dic_a:
                if j in dic_a[q]:
                    count = count + 1
                    sum_up = sum_up + 1
                    #while fathernode existed the sum_up is greater than 0, the while loop will keep running
                    fathernode.append(q)
                    #print(q) # !!!!write for test use only
        fathernode_temp = fathernode[:]
        #print(fathernode_temp) # !!!!write for test use only
    sum_array.append(count)
    #store the node number for each id


count_add = 0
#get the total number
for i in sum_array:
    count_add = count_add + i
print(count_add)



labels = ['DNA', 'RNA', 'Protein','Oligosaccharide']
X = [270722, 34097, 684528,728]

fig = plt.figure()
plt.pie(X, labels=labels, autopct='%1.2f%%')
plt.title("Childnodes for macromolecule")

plt.show()












