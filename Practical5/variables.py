a = 200287
b = 190784
c = 202139
d = abs(a-c)
e = abs(a-b)
if d > e :
    print("d is greater")
else:
    print("e is greater")

X = True
Y = False
Z =(X and not Y) or (Y and not X)
W = X!=Y
print (Z)
print (W)
