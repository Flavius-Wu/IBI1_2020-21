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
dic_a = {}
for term in terms:
    id = term.getElementsByTagName("id")[0]
    id_inf=id.childNodes[0].data
    #print(id.childNodes[0].data)
    description = term.getElementsByTagName("defstr")[0]
    #print(description.childNodes[0].data)
    des_inf =description.childNodes[0].data
    dic_def[id_inf]=des_inf
    is_a = term.getElementsByTagName("is_a")
    list1=[]
    for i in is_a:
        #print("is_a",i.childNodes[0].data)
        list1.append(i.childNodes[0].data)
    dic_a[id_inf]=list1

print(dic_a)

key = input('please input the keyword')
dic_temp = {}
for i in dic_def.keys():
    if re.search(key, dic_def[i]):
        value = dic_def[i]
        dic_temp[i] = value
array = dic_temp.keys()
print(array)
sum_array =[]
for id_name in array:
    print('id_name',id_name)
    count = 0
    fathernode = []
    for k in dic_a:
        if id_name in dic_a[k]:
            count = count + 1
            fathernode.append(k)
    fathernode_temp = fathernode[:]
    print(fathernode_temp)
    sum_up = count
    while sum_up != 0 :
        sum_up = 0
        fathernode = []
        for j in fathernode_temp:
            for q in dic_a:
                if j in dic_a[q]:
                    count = count + 1
                    sum_up = sum_up + 1
                    fathernode.append(q)
                    print(q)
        fathernode_temp = fathernode[:]
        print(fathernode_temp)
    sum_array.append(count)


count_add = 0
for i in sum_array:
    count_add = count_add + i
print(count_add)




labels = ['DNA', 'RNA', 'Protein','Oligosaccharide']
X = [270722, 34097, 684528,728]

fig = plt.figure()
plt.pie(X, labels=labels, autopct='%1.2f%%')
plt.title("Childnodes for macromolecule")

plt.show()












