class UI:
    def input(self):
        

        #n=int(input("Enter number of instances : "))
        #d=fibonacci_sequences()
        #for i in range(n):
            q=fibonacci_sequence()
            m=int(input("Enter number of strings/lines : "))
            
            s1=input("Enter 1st string : ")
            q.add_stringS1(s1)
            s2=input("Enter 2nd string : ")
            q.add_stringS2(s2)
            for i in range(m):
                q.concat(s1,s2)
                



            

            return q    
                

class fibonacci_sequence:
    def __init__(self):
        self.s1=[]
        self.s2=[]
        self.strings=[]

    def add_stringS1(self,s):
        self.s1.append(s)
        self.strings.append(s)
        print(self.strings)

    def add_stringS2(self,s2):
        self.s2.append(s2)
        self.strings.append(s2)
        print(self.strings)

    def concat(self,s1,s2):
        print("String 1 : %s" %s1)
        print("String 2 : %s" %s2)
        
        print(s1)
        print(s2)
        s2=s1+s2
        print(s2)
        self.strings.append(s2)

            
#class fibonacci_sequences:
 #   def __init__(self):
  #      fibonacci_sequence()
   #     self.fibonacci_sequences=[]

    #def add_instance(self,seq):
     #   self.fibonacci_sequences.append(seq)
      #  print(self.fibonacci_sequences)



w=UI()
b=w.input()
