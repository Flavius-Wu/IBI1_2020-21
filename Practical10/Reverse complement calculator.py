import string
def rev_seq_cal(seq):
    seq = seq.upper()
    # make it suitable for both upper case, lower case, or a mixture of the two
    list_seq = list(seq) #transfer string to list
    new_seq = [] # make teo empty list
    rev_seq = []
    for i in list_seq:
        #    print(i) for test use only
        if i == 'A':
            i = 'T'
            new_seq.append(i)
        else:
            if i == 'T':
                i = 'A'
                new_seq.append(i)
            else:
                if i == 'G':
                    i = 'C'
                    new_seq.append(i)
                else:
                    if i == 'C':
                        i = 'G'
                        new_seq.append(i)

    for i in reversed(new_seq):
        rev_seq.append(i)
        pass

    return('The reverse sequence from 5"'"to 3"'"is ' + str(rev_seq))

seq= input('The origin sequence')
print(rev_seq_cal(seq))




