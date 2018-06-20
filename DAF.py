class UI:
    def input(self):
        

        m=int(input("Enter number of states : "))
        k=int(input("Enter number of accepting states : "))
        for i in range(k):
            d=int(input("Enter position of %d accepting state : " %i))
            q.add_accepting_states(d)
        for i in range(m):
            a=int(input("Enter destination of 'A' from %s state : " %i))
            b=int(input("Enter destination of 'B' from %s state : " %i))




class line1:
    def __init__(self,m,k):
        self.m=m
        self.k=k

class line2:
    def __init__(self,acc):
        self.acc_states=[]

    def add_accepting_states(self,d):
        self.acc_states.append(d)

class line3_m:
    def __init__(self,

    def transition(self,s,a,b):









a=UI()
b=a.input()
