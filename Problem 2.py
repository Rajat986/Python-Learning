
def computeF(l):
    r=[]
    for k in l:
        denominator =1
        for i in k:
            denominator *= i
        numerator = 0
        for i in k:
            numerator += denominator/i
        r.append((numerator,denominator))
    return r

def show(l,r):
    for k,result in zip(l,r):
        for j in k:
            print("1/%d+"%j)
        print("=")
        print("%d/%d"%(result[0],result[1]))
        
        
def inputF():
    m=int(input("Enter number of inputs : "))
    l=[]
    for i in range (m):
        n=int(input("Enter number of elements : "))
        k=[]
        for i in range (n):
            p=int(input("Enter elements : "))
            k.append(p)
        l.append(k)
    return l

l=inputF()
r=computeF(l)
show(l,r)


