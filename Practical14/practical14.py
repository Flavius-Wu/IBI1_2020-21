from xml.dom.minidom import parse
import re
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#remove all the duplicate elements from the list
def similar(list):
    list1=[]
    list2=[]
    list1 = list
    for i in list1:
        if i not in list2:
            list2.append(i)

    return list2

doc= parse('go_obo.xml')
# get rootnode
root=doc.documentElement
terms=root.getElementsByTagName('term')
dic_def = {}
dic_a = {}
for term in terms:
    #split the xml into categories by terms
    id = term.getElementsByTagName("id")[0]
    id_inf=id.childNodes[0].data
    #get the id content
    #print(id.childNodes[0].data) !!!for test use only
    description = term.getElementsByTagName("defstr")[0]
    #print(description.childNodes[0].data)
    des_inf =description.childNodes[0].data
    #get the description conntent for each corresponding id
    dic_def[id_inf]=des_inf
    #form a list, key is the id, value is description
    is_a = term.getElementsByTagName("is_a")
    list1=[]
    # put all corresponding is_a into a list
    for i in is_a:
        #print("is_a",i.childNodes[0].data)!!!for test use only
        list1.append(i.childNodes[0].data)
    dic_a[id_inf]=list1
    #form a list, key is the id, value is is_a list
# print(dic_a)!!!for test use only

key = input('please input the keyword')
dic_temp = {}
#go through the dictionary to screen out ids we want
for i in dic_def.keys():
    if re.search(key, dic_def[i]):
        value = dic_def[i]
        dic_temp[i] = value
array = dic_temp.keys() #contain the ids we want
#print(array) !!!for test use only
sum_array =[] #used to store the total fathernode number for each selected id

for id_name in array:
    #grab a id at a time
    # print('id_name',id_name)!!!for test use only
    count = 0
    fathernode = []
    all_node=[]
    #get id's fathernode put them in a new list
    for k in dic_a:
        if id_name in dic_a[k]:
            fathernode.append(k)
            fathernode=similar(fathernode)
            #only put new fathernode into the list
    fathernode_temp = fathernode[:]
    count = len(fathernode_temp)
    #print(fathernode_temp)!!!for test use only
    all_node = fathernode_temp
    sum_up = count
    #if on fathernode existed quit the test for this id
    #while father node still can be found, keep searching
    while sum_up != 0 :
        sum_up = 0
        fathernode = []
        for j in fathernode_temp:
            for q in dic_a:
                if j in dic_a[q]:
                    sum_up = sum_up + 1
                    #if no fathernode, the sum_up will be 0
                    fathernode.append(q)
                    #print(q) !!!for test use only
        fathernode_temp = fathernode[:]
        fathernode_temp = similar(fathernode_temp)
        all_node = all_node + fathernode_temp        
    all_node = similar(all_node)
    #only count different nodes for each seleced id
    sum_array.append(len(all_node))

#sum up the fathernode number for all selected ids
count_add = 0
for i in sum_array:
    count_add = count_add + i
print(count_add)


#the DNA, RNA, protein and oligosaccharide have been put into test
#the results are shown below
#it is a time consuming program, please wait

labels = ['DNA', 'RNA', 'protein','oligosaccharide']
X = [12707, 20383, 77691,580]

fig = plt.figure()
plt.pie(X, labels=labels, autopct='%1.2f%%')
plt.title("Childnodes for macromolecule")

plt.show()












