class UI:
    def input(self):
        print("Enter 2 numbers to add:-")
        a=float(input("Enter 1st number : "))
        b=float(input("Enter 2nd number : "))
        c=compute(a,b)
        d=c.add();
        return d;

    def output(self,inp):
        print("The sum is : %f" %inp)

class compute:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return(self.x + self.y)


z=UI()
y=z.input()
z.output(y)
