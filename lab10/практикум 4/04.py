row1 = "1234567890"
row2 = "qwertyuiop"
row3 = "asdfghjkl"
row4 = "zxcvbnm"

n = int(input())

for _ in range(n):
    password = input().strip()
    
    r1 = False
    r2 = False
    r3 = False
    r4 = False
    
    for i in password:
        if i in row1:
            r1 = True
        elif i in row2:
            r2 = True
        elif i in row3:
            r3 = True
        elif i in row4:
            r4 = True
            
    if r1 and r2 and r3 and r4:
        print("strong")
    else:
        print("weak")
