class UI:
    def input(self):
        n=int(input("Enter number of instances : "))
        socp=set_of_circle_pairs()
        for i in range(n):
            r1=float(input("Enter radius of circle 1 : "))
            x1=float(input("Enter x co-ordinate of center : "))
            y1=float(input("Enter y co-ordinate of center : "))
            p1=point(x1,y1)
            c1=circle(r1,p1)
            
        
            r2=float(input("Enter radius of circle 2 : "))
            x2=float(input("Enter x co-ordinate of center : "))
            y2=float(input("Enter y co-ordinate of center : "))
            p2=point(x2,y2)
            c2=circle(r2,p2)

            point.distance(self,x1,x2,x2,y2)
            circle_pair.is_intersecting(self,c1,c2)

            cp=circle_pair(self,dis,r1,r2)
            socp.add_circle_pair(cp)
        return socp  

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance(self,x1,y1,x2,y2):
        dis=math.sqrt((x1-x2)**2+(y1-y2)**2)
        print("Distance : %f" %dis)
        

class circle:
    def __init__(self,r,p):
        self.r=r
        self.p=p
    
        
class circle_pair:
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2

    def is_intersecting(self,dis,r1,r2):
        if(dis <(r1+r2)):
            print(True)
        else:
            print(False)

class set_of_circle_pairs:
    def __init__(self):
        self.n_circles=[]


    
    def add_circle_pair(self,cp):
        self.n_circles.append(cp)
        print(self.n_circles)

import math
a=UI()
b=a.input()


