class UI:
    def input(self):
        

        #n=int(input("Enter number of instances : "))
        #d=fibonacci_sequences()
        #for i in range(n):
            
            m=int(input("Enter number of strings/lines : "))
            
            s1=input("Enter 1st string : ")
            
            s2=input("Enter 2nd string : ")
            
            q=fibonacci_sequence(s1,s2,m)
            q.add_string(s1)
            q.add_string(s2)
            
            for i in range(m-2):
                q.concat()
                



            

            return q    
                

class fibonacci_sequence:
    def __init__(self,s1,s2,m):
        self.s1=s1
        self.s2=s2
        self.m=m
        self.strings=[]
        print(self.strings)

    def add_string(self,s):
        self.strings.append(s)
        print(self.strings)

    

    def concat(self):
        print("String 1 : %s" %self.s1)
        print("String 2 : %s" %self.s2)
        
        print(self.s1)
        print(self.s2)
        
        s1=self.s2
        s2=(self.s1)+(self.s2)
        self.add_string(s2)
        print(self.s2)
        return s2
        
        
    
            
#class fibonacci_sequences:
 #   def __init__(self):
  #      fibonacci_sequence()
   #     self.fibonacci_sequences=[]

    #def add_instance(self,seq):
     #   self.fibonacci_sequences.append(seq)
      #  print(self.fibonacci_sequences)



w=UI()
b=w.input()
