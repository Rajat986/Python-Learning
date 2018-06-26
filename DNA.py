class ui:
    def input(self):


        n=int(input("Enter number of nucleotides : "))
        for i in range(n):
            s=input("Enter the set of nucleotide %d : " %(i+1))
            for i in range(len(s)):
                if(s[i]=='A' or s[i]=='T' or s[i]=='C' or s[i]=='G' or s[i]=='a' or s[i]=='t' or s[i]=='c' or s[i]=='g'):
                    a=c_nucleotide()
                    a.add_nucleotide(s)
                else:
                    print("Error!!!")
                    exit(0)
class genome:
    def __init__(self):
        self.genome=[]
    
    def add_nucleotide(self,nucleo):
        self.genome.append(nucleo)
    def count(self,nucleotide):
       

    
        

class c_nucleotide:
    def __init__(self):
        self.nucleotide=[]

class break_nucleotides:
    def __init__(self):
        self.nucleotides=[]
    
    
      


  
   




w=ui()
w.input()
