class ui:
    def input(self):
        z=EKGs()

        n=int(input("Enter the number of EKG : "))
        for i in range (n):
            t=input("Enter EKG %d :" %(i+1))
            ctr=0
            for i in range (len(t)):
                if(t[i]=='R' or t[i]=='P' or t[i]=='Q' or t[i]=='S' or t[i]=='T' or t[i]=='U' or t[i]=='-'  or t[i] == "p" or t[i] == "q" or t[i] == "r" or t[i] == "s" or t[i] == "t" or t[i]=="u"):
                    for j in range(len(t)):
                        
                        if(t[j] =='R' or t[j] == 'r'):
                            ctr=ctr+1
                    if(ctr<3):
                        print("There must be minimum 3 'R's...!!!!!")
                        exit(0)
                    y=EKG(t)
                    z.add_EKG(y)

                else:
                    print("Enter only 'P','Q','R','S','T','U' or '-' ONLY!!!!")
                    exit(0)

        return z
    def output(self,pEKGs):
        for i in pEKGs.ekgs:
            t=i.isregular()
            print(ekg,"Regular" if (t==True) else "i")




class EKG:
    def __init__(self,ekg):
        self.ekg=ekg
        
    def isregular(self):
        
        

class EKGs:
    def __init__(self):
        self.ekgs=[]
        
    def add_EKG(self,EKG):
        self.ekgs.append(EKG)
        


a=ui()
b=a.input()
c=a.output(b)
#for i in b.testcases:
