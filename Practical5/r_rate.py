n = float(84) # the students number in IBI
r = float(input("R value:")) # input the r value
R = int(5) # input the round number
for i in range(R):  # repeat the round for many times
    m = n * r
    n = m + n
print("r rate is"+ " " + str(r) + " "+"total number of individuals infected after 5 generations is" + " "+str(n)) #print the answer

