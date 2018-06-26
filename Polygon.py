class UI:
    def input(self):
        po=polygon()
        
        p=int(input("Enter number of vertices : "))
        if(p <= 2):
            print("Enter at least 3 vertices!!!!!")
            exit(0)
        else:
            for i in range(p):
                a=float(input("Enter 'X' co-ordinate for vertex %d : " %(i+1)))
                b=float(input("Enter 'Y' co-ordinate for vertex %d : " %(i+1)))
                g=vertex_or_point(a,b)
                r=c_vertices()
                r.add_vertices(g)

            m=int(input("Enter number of points to test : "))
            for i in range(m):
                c=float(input("Enter 'X' co-ordinate for point %d : " %(i+1)))
                d=float(input("Enter 'Y' co-ordinate for point %d : " %(i+1)))
                s=vertex_or_point(c,d)
                w=c_test_points()
                w.add_test_points(s)

        return po




class vertex_or_point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class c_vertices:
    def __init__(self):
        self.vertices=[]
        
    def add_vertices(self,ver):
        self.vertices.append(ver)
        
class c_test_points:
    def __init__(self):
        self.test_points=[]

    def add_test_points(self,tp):
        self.test_points.append(tp)

class polygon:
    pass


e=UI()
b=e.input()
