m=[["","",""],["","",""],["","",""]]

def checkandsetto_x(m,a,b,x):
    if m[a][b]=="x" or m[a][b]=="o":
        return 4
    else:
        m[a][b]=x

def win(m,a,b,x):
    if m[0][0]==m[0][1]==m[0][2]==x or m[1][0]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m[0][0]==m[1][0]==m[2][0]==x or m[0][1]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m[0][0]==m[2][2]==m[1][1]==x or m[1][2]==m[1][1]==m[2][0]==x:
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
    a=int(input("x="))
    b=int(input("y="))
    t=checkandsetto_x(m,a,b,"x")
    if t==4:
        print("Space Used")
        continue
    w=win(m,a,b,"x")
    if w==3:
        print("A wins")
        printboard(m)
        break        
    printboard(m)
    z=computeContinue(m)
    if z==1:
        print("Draw")

    while True:
        a=int(input("x="))
        b=int(input("y="))
        t=checkandsetto_x(m,a,b,"o")
        if t==4:
            print("Space Used")
            break
        w=win(m,a,b,"o")
        if w==3:
            print("B wins")
            printboard(m)
            exit()
            
        printboard(m)
        break

        
