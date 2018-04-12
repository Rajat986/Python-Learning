m=[["","",""],["","",""],["","",""]]

def checkandsetto_x(m,a,b,x):
    if m[a][b]=="x" or m[a][b]=="o":
        return 4
    else:
        m[a][b]=x

def win(m,a,b,x):
    if m[0][0]==m[0][1]==m[0][2]==x or m[1][0]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m[0][0]==m[1][0]==m[2][0]==x or m[0][1]==m[1][1]==m[2][1]==x or m[0][2]==m[1][2]==m[2][2]==x or m[0][0]==m[1][1]==m[2][2]==x or m[0][2]==m[1][1]==m[2][0]==x:
        return 3

def computeContinue(m):
    if m[0][0] =="" or m[0][1]==""or m[0][2]==""or m[1][0]==""or m[1][1]==""or m[1][2]==""or m[2][0]==""or m[2][1]==""or m[2][2]=="":
        return 0
    else:
        return 1
    
def printboard(m):
    for i in m:
        print(i)

while True:
    print("Player A's turn:")
    a=int(input("X="))
    b=int(input("Y="))
    t=checkandsetto_x(m,a,b,"x")
    if t==4:
        print("Overlap Not Allowed!!!")
        print()
        continue
    w=win(m,a,b,"x")
    if w==3:
        print("YAY Player A wins!!!")
        printboard(m)
        exit(0)
        
    printboard(m)
    z=computeContinue(m)
    if z==1:
        print("Draw")
        exit(0)

    while True:
        print("Player B's turn:")
        a=int(input("X="))
        b=int(input("Y="))
        t=checkandsetto_x(m,a,b,"o")
        if t==4:
            print("Overlap Not Allowed!!!")
            print()
            continue
        w=win(m,a,b,"o")
        if w==3:
            print("YAY Player B wins!!!")
            printboard(m)
            exit(0)
        printboard(m)
        if z==1:
            print("Well Played DRAW")
        break
