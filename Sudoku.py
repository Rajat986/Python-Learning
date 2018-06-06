class matrix:
    def __init__(self):
        self.a=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        





class UI:
    def readmatrix(self):
        m=matrix()
        for i in range(9):
            for j in range(9):
                m.a[i][j]=int(input("enter %d,%d element : "%(i,j)))
        return m
    
    
 
c=UI()
m=c.readmatrix()
print(m.a)
