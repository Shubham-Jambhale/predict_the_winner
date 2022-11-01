def predict_winner ( s ) :
    astk=[]
    ostk=[]
    
    for i in range(len(s)):
        if s[i] == "A":
            astk.append(i)
        if s[i] == "O":
            ostk.append(i)
    
    while astk != [] and ostk != []:
    
        a = astk.pop(0)
        o = ostk.pop(0)
        
        if a < o:
            astk.append((a+len(s)))
        else :
            ostk.append((o+len(s)))

    if astk == []:
        return "Orange"
    else:
        return "Apple"
