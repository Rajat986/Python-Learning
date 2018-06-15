class UI:
    def input(self):
        n=int(input("Enter number of instances : "))
        for i in range(n):
            q=sequence()

            l=int(input("Enter number of elements : "))
            for i in range(l):
                e=int(input("Enter %d element : " %(i+1)))
                
                q.add_element(e)
        return q 


class sequence:
    def __init__(self):
        self.ele=[]
        
        self.ascents = []
        self.descents = []
        self.plateaus = []
        
    def add_element(self,e):
        self.ele.append(e)
        print(self.ele)
    def add_a(self,a):
        self.ascents.append(a)
        print(self.ascents)
    def add_d(self,d):
        self.descents.append(d)
        print(self.descents)
    def add_p(self,p):
        self.plateaus.append(p)
        print(self.plateaus)
        
    def find_ascents(self):
        ctr=0
        for i in range(len(self.ele)-1):
            if(self.ele[i]<self.ele[i+1]):
                ctr=ctr+1

            print("Number of ascents : %d" %ctr)        

                
    def find_descents(self):
        pass

    def find_plateaus(self):
        pass

import pdb
pdb.set_trace()
w=UI()
b=w.input()
b.find_ascents()
b.find_descents()
b.find_plateaus()
#UI.show(b)
