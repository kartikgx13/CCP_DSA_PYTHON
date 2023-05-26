def countChars(S):
    c1=0
    c2=0
    c3=0
    c4=0
    special_characters = "!@#$%^&*()-+?_=,<>/"
    for i in range(len(S)):
        if S[i].isupper():
            c1 += 1
        elif S[i].islower():
            c2 += 1
        elif S[i].isdigit():
            c3 += 1
        elif S[i] in special_characters:
            c4 += 1
    
    return c1,c2,c3,c4

str1="#GeeKs01fOr@gEEks07"
print(countChars(str1))

        
    
    

