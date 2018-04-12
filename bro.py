import pdb
pdb.set_trace() 
m=[["","",""],["","",""],["","",""]]

def checkandsettox(m,a,b,x):
    if m[a][b]=="o" or m[a][b]=="x":
        return True
    else:
        m[a][b]=x

def checkandsettoo(m,a,b,o):
    if m[a][b]=="o" or m[a][b]=="x":
        return True
    else:
        m[a][b]=o

def checkwin(m,a,b,x):
    if m[0][0]==m[0][1]==m[0][2]==x or m[1][0]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m[0][0]==m[1][0]==m[2][0]==x or m[0][1]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m[0][0]==m[2][2]==m[1][1]==x or m[1][2]==m[1][1]==m[2][0]==x:
        return 1

def computeContinue(m):
   if m[0][0]==""or m[0][1]==""or m[0][2]==""or m[1][0]==""or m[1][1]==""or m[1][2]==""or m[2][0]==""or m[2][1]==""or m[2][2]=="":
      return 1
   else:
      return 0        

def printboard(m):
    for i in m:
        print(i)

while True:
    a=int(input("X="))
    b=int(input("Y="))
    r=checkandsettox(m,a,b,"x")
    if r==True:
        print("Overlap not allowed!!!")
        continue
    s=checkwin(m,a,b,"x")
    if s==1:
        print("A wins")
        break
    printboard(m)
    
    a=int(input("X="))
    b=int(input("Y="))
    r=checkandsettox(m,a,b,"o")
    if r==True:
        print("Overlap not allowed!!!")
        continue
    checkwin(m,a,b,"o")
    if checkwin(m,a,b,"o")==1:
        print("B wins")
        break
    printboard(m)
    computeContinue(m)
    if computeContinue(m)==0:
        exit()
