class UI:
    def input(self):
        j=n_polygonal_chain()

        m=int(input("Enter number of polygonal chains : "))
        for i in range(m):
            n=int(input("Enter number of points in a polygonal chain %d : " %(i+1)))
            r=polygonal_chain()
            for i in range(n):
                a=int(input("Enter 'X' co-ordinate of point %d : " %(i+1)))
                b=int(input("Enter 'Y' co-ordinate of point %d: "%(i+1)))

                w=point(a,b)
                r.add_point(w)
            j.add_poly_chain(r)

        return(j)

    def output(self,inp):
        for i in inp.n_poly_chains:
            t=i.total_area()
            print("Output : %f" %t)

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class polygonal_chain:
    def __init__(self):
        self.poly_chains=[]

    def add_point(self,point):
        self.poly_chains.append(point)

    def total_area(self):
        u=0
        for i in range(len(self.poly_chains)-1):
            p1=self.poly_chains[i]
            p2=self.poly_chains[i+1]
            u = u + self.area_tra(p1,p2)
        return u
    
    def area_tra(self,p1,p2):
        x= p2.x - p1.x

        if(p1.y > p2.y):
            h_r= p2.y
        else:
            h_r=p1.y    

        h_t= abs(p1.y - p2.y)
         
        area=((0.5*x*h_t)+(x*h_r))

        return(area)
                

class n_polygonal_chain:
    def __init__(self):
        self.n_poly_chains=[]

    def add_poly_chain(self,p_c):
        self.n_poly_chains.append(p_c)

q=UI()
b=q.input()
q.output(b)
