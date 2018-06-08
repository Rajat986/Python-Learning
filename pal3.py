class pal_t:
    def __init__(self):
        self.string=[]
        self.brokendownstring=[]
    def addstring(self,s):
        self.string.append(s)
        print(self.string)

    def reverse(s):
        if(s==s[::-1]):
            return True
        else:
            return False
    def breakdown():
        pass
        


class UI:
    def input(self):
        q=pal_t()
        n=int(input("Enter the no.of strings : "))
        for i in range (n):
            l=int(input("Enter the length : "))
                
            s=input("Enter the string : ")
            
            if(len(s)<l or len(s)>l):
                exit(0)
            q.addstring(s)
        return q
        
        

a=UI()
q=a.input()        

u=pal_t()
u.reverse(s)

