class line_and_points:
    def __init__(self):
        self.line_and_points=[]
    def add_line_point(self,line_and_point):
        self.line_and_points.append(line_and_point)

class line_and_point:
    def __init__(self,line,point):
        self.line=line
        self.point=point

class line:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def is_point_on_line(self,p):
        pass
         
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,p2):
        dis=sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)
        print(dis)    
 
class UI:
    def input(self):
        n=int(input("Enter number of instances : "))
        q=line_and_points()
        for i in range(n):
            print("Enter point :- ")
            x=float(input("Enter X : "))
            y=float(input("Enter Y : "))
            w=point(x,y)
            
            print("Enter P1 :- ")
            x1=float(input("Enter X1 : "))
            y1=float(input("Enter Y1 : "))

            p1=point(x1,y1)
            print("Enter P2 :- ")
            x2=float(input("Enter X2 : "))
            y2=float(input("Enter Y2 : "))    
                
            p2=point(x2,y2)
            l=line(p1,p2)
            landp=line_and_point(l,w)
            q.add_line_point(landp)

        return q
import math
a=UI()
i=a.input()
