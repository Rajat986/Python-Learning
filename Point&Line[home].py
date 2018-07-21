class UI:
    def input(self):
        m=int(input("Enter number of instances : "))
        z=point_lines()
        w=test_ps()
        q=line_segs()
        for i in range(m):
            print("Enter test-point %d details :- " %(i+1))
            g=float(input("Enter X-coordinate of test-point : "))
            h=float(input("Enter Y-coordinate of test-point : "))
            tpoint=point(g,h)
            w.add_tp(tpoint)
            print("Enter details of line :-")
            a=float(input("Enter X-coordinate of one end of the line : "))
            b=float(input("Enter Y-coordinate of one end of the line : "))
            lp1=point(a,b)
            c=float(input("Enter X-coordinate of other end of the line : "))
            d=float(input("Enter Y-coordinate of other end of the line : "))
            lp2=point(c,d)
            lin=line_seg(lp1,lp2)
            q.add_lineseg(lin)
            s=point_line(tpoint,lin)
            z.add_pointandline(s)
        return z

    def output(self,inp):
        j=0
        for i in inp.point_and_line:
            j=j+1
            print("Point %d        = (%f,%f)" %(j,i.point.x,i.point.y))
            print("Line %d points  = (%f,%f),(%f,%f)" %(j,i.line.lp1.x,i.line.lp1.y,i.line.lp2.x,i.line.lp2.y))
            i.distance()

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class test_ps:
    def __init__(self):
        self.tps=[]
    def add_tp(self,tpss):
        self.tps.append(tpss)
        print(self.tps)
        

class line_seg:
    def __init__(self,lp1,lp2):
        self.lp1=lp1
        self.lp2=lp2

class line_segs:
    def __init__(self):
        self.lineseg=[]
    def add_lineseg(self,ls):
        self.lineseg.append(ls)
        print(self.lineseg)

   

class point_line:
    def __init__(self,point,line):
        self.point=point
        self.line=line

    #def distance(self,p):
        #dis=math.sqrt((self.x-p.x)**2 + (self.y-p.y)**2)
        #print(dis)

class point_lines:
    def __init__(self):
        self.point_and_line=[]
    def add_pointandline(self,pal):
        self.point_and_line.append(pal)
        print(self.point_and_line)


import math
a=UI()
#import pdb
#pdb.set_trace()
b=a.input()
a.output(b)
