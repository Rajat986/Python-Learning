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
            t=i.area()
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

    def area(self):
        for i in range(len(self.poly_chains)-1):
            p1=self.poly_chains[i:i+1]
            x=p1[i+1].x-p1[i].x

            return(x)
                

class n_polygonal_chain:
    def __init__(self):
        self.n_poly_chains=[]

    def add_poly_chain(self,p_c):
        self.n_poly_chains.append(p_c)

q=UI()
b=q.input()
q.output(b)
