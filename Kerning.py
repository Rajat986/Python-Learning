class UI:
    def input(self):
        p=int(input("Enter the number of bitmaps : "))
        w=n_bitmap()
        for i in range (p):
            m=int(input("Enter number of rows of bitmap : "))
            n=int(input("Enter number of columns of bitmap : "))
            print("Enter only '0' & '1' only :-")
            l=[]
            for i in range(m):
                for i in range(n):
                    l.append(input())
                print("")

            p=m*n
            for i in range(p):
                if(i>1):
                    if(i % n == 0):
                        print("")
                print(l[i],end="")
                
            q=bitmap(l)
        return(w)

            



    def output(self,inp):
        for i in inp.bit_maps:
            t=i.compute()
            print("Output : %d" %t)
            
                
    




            
class bitmap:
    def __init__(self,bit_map):
        self.bit_map=bit_map
        

class n_bitmap:
    def __init__ (self):
        self.bit_maps=[]
    def add_bitmap(self,bit):
        self.bit_maps.append(bit)

    def compute(self):
        t=544
        return(t)

a=UI()
b=a.input()
a.output(b)
