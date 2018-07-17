class UI:
    def input(self):
        d=dfa()     
        n=int(input("Enter number of states : "))
        m=int(input("Enter number of accepting states : "))
        for i in range(n):
            sta= st(i,False)
            d.addstate(sta)
        for i in range(m):
            q=int(input("Enter accepting state %d : " %(i+1)))
            sta=st(q,True)
            d.addstate(sta)
        for i in range(n):
            a=int(input("Enter destination of 'A' for row %d : " %(i+1)))
            b=int(input("Enter destination of 'B' for row %d : " %(i+1)))
            c=transition(d.states[a],d.states[b])
            d.addtransition(i,c)
            
        s=int(input("Enter number of strings : "))
        los=[]
        for i in range(s):
            mys=input("enter the next string")
            los.append(mys)
        return d,los
    def showoutput(self,d,s):
        for i in s:
            print(d.accept(i))
            

class transition:
    def __init__(self,adest,bdest):
        self.adest  = adest
        self.bdest  = bdest
    def getnext(self,c):
        if c=="a":
            return self.adest
        else:
            return self.bdest
  
class st:
    def __init__(self,state,accepting):
        self.state=state
        self.accepting=accepting
    def addtransition(self,t):
            self.transition=t
        
class dfa:
    def __init__(self):
        self.states={}
    def addstate(self, st):
        self.states[st.state]=st
    def addtransition(self,st,transition):
        self.states[st].addtransition(transition)
        
    def accept(self,s):
        currentstat=self.states[0]
        for i in s:
            newstate=currentstat.transition.getnext(i)
            if newstate is None:
                return False
            currentstat=newstate
        return newstate.accepting==True
    
            
 
        
a=UI()
c,d=a.input()
#import pdb
#pdb.set_trace()
a.showoutput(c,d)
