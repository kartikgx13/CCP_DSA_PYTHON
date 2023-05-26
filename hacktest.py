def convertString(s):
    num=''
    alphabets={
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8,
        'i':9,
        'j':1,
        'k':2,
        'l':3,
        'm':4,
        'n':5,
        'o':6,
        'p':7,
        'q':8,
        'r':9,
        's':1,
        't':2,
        'u':3,
        'v':4,
        'w':5,
        'x':6,
        'y':7,
        'z':8
        
    }
    
    for i in range(len(s)):
        if s[i] in alphabets.keys():
            num += str(alphabets.get(s[i]))
    
    return int(num)

t=int(input())
for _ in range(t):
    n=int(input())
    string=input()
    print(convertString(string))