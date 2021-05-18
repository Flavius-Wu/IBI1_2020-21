def calculator(name, code, poster, final):
    #input all the necessary information
    code = int(code)
    poster = int(poster)
    final = int(final)
    #calculate the grade as defined
    all= ((code/100)*40 + (poster/100)*30 + (final/100)*30)
    all = str(all)
    return(name + ''''s Score for IBI1 is '''+ all)

print(calculator('Yuefeng','90','90','90'))



