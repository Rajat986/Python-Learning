class board:
    def __init__(self):
        self.a=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

    def compute(self):
        for i in range(9):
            r=getrow(i)
            if checkvalid(r)
            r=getcolum(m)
        

    def getrow(i):
        return self.a[i]
    def getcolumn(i):
        return [ j[i] for j in self.a] 
    def getblock(i):
        ....


class UI:
    def readmatrix(self):
        m=board()
        for i in range(9):
            for j in range(9):
                m.a[i][j]=int(input("enter %d,%d element : "%(i,j)))
        return m
    

    
 
c=UI()
b=c.readboard()
print(m.a)
