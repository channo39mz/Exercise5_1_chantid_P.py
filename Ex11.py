num = int(input())
txt = ""
R = ""
for x in range(num): # แภว
    txt = " "*(num -x -1)
    for y in range(x+1): # จำนวน*
        txt = txt + "*"
        R = "*" * y
    print(txt+R)
