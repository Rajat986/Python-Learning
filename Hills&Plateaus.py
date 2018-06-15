class UI:
    def input(self):
        n=int(input("Enter number of instances : "))
        d=sequences()
        for i in range(n):
            q=sequence()

            l=int(input("Enter number of elements : "))
            for i in range(l):
                e=int(input("Enter %d element : " %(i+1)))
                
                q.add_element(e)
            d.add_sequence(q)
        return d

    def show(self,d):
        pass


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
        for i in self.ele:
            if(self.ele[i] > self.ele[i+1] or self.ele[i]==self.ele[i+1]):
                ctr=ctr+1
            print("Number of ascents : %d" %ctr)

                
    def find_descents(self):
        pass

    def find_plateaus(self):
        pass

class sequences:
    def __init__(self):
        self.sequences=[]
    def add_sequence(self,seq):
        self.sequences.append(seq)
        print(self.sequences)
        


        

w=UI()
b=w.input()
b.find_ascents()
b.find_descents()
b.find_plateaus()
UI.show(b)
