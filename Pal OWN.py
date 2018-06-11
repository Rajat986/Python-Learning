class pal_t:
    def __init__(self):
        self.string=[]
        self.brokendownstring=[]
        self.allowed=[]
        self.pals=[]

    def addstring(self,s):
        self.string.append(s)
        print("Add String : %s" %self.string)

        pal_t.breakstring(self,s)

    def breakstring(self,s):
                  
            
        for i in range(len(s)):
            for j in range(len(s)):
                
                g=s[i:j+1]
                self.brokendownstring.append(g)

            
            
        print("Break String : %s" %self.brokendownstring)
        pal_t.all_owed(self,s)

    def all_owed(self,s):

        for i in range(len(self.brokendownstring)):
            
            if(len(self.brokendownstring[i])>2):
                self.allowed.append(self.brokendownstring[i])

        print("Allowed : %s" %self.allowed)
        pal_t.check_for_pal(self,s)

    def check_for_pal(self,s):
        for i in range(len(self.allowed)):
            h=self.allowed[i]
            rev=h[::-1]
            if(h==rev):
                self.pals.append(h)

        print("Palindromes : %s" %self.pals)
        
        j=list(set(self.pals))
        print("Pals after rejection : %s" %j)
            

        
    


class UI:
    def input(self):
        q=pal_t()

        n=int(input("Enter the number of strings : "))
        for i in range (n):
            l=int(input("Enter length of the string : "))
            s=input("Enter string : ")

            if(len(s)>l or len(s)<l):
                exit(0)

            q.addstring(s)        


a=UI()
a.input()
