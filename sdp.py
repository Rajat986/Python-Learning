x=[["","",""],["","",""],["","",""]]
def compute(m,a,b,x):
    m[a][b]=x
    if m[0][0]==m[0][1]==m[0][2]==x or m[1][0]==m[1][1]==m[1][2]==x or m[2][0]==m[2][1]==m[2][2]==x or m[0][0]==m[1][0]==m[2][0]==x or m[0][1]==m[1][1]==m[2][1]==x or m[0][2]==m[1][2]==m[2][2]==x or m[0][0]==m[1][1]==m[2][2]==x or m[0][2]==m[1][1]==m[2][0]==x:
        return 0
    if m[0][0]=="" or m[0][1]== "" or m[0][2]=="" or m[1][0]== "" or m[1][1]== "" or m[1][2]=="" or m[2][0]== "" or m[2][1]== "" or m[2][2]=="":
        return 1

def printboard(m):
    for i in m:
        print(i)
while True:
    a=int(input("x"))
    b=int(input("y"))
    r=compute(x,a,b,"x")
    printboard(x)
    if r==0:
        print("Player A wins")
        break
    if not r==1:
        print("Draw")
        break
    a=int(input("x"))
    b=int(input("y"))
    r=compute(x,a,b,"o")
    printboard(x)
    if r==0:
        print("Player B wins")
        break
    if not r==1:
        print("Draw")
        break 
