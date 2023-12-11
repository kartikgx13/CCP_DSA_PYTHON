def fact(x):
    if x==1:
        return x
    
    return x*fact(x-1)

print(fact(5))
""" 
1st 5*fact(4)
2nd 5*4*fact(3)
                      
                    fact(5)
                   /      \
                   5      fact(4)
                          /      \
                          4       fact(3) 
                          
                           0 1 1 2 3 5
"""