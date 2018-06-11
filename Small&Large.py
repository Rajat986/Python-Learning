class UI:
    def input(self):
        q=Sequence()

        n=int(input("Enter number of instances : "))
        for i in range(n):
            l=int(input("Enter number of elements : "))
            if(l<2):
                print("Enter at least 2 elements!!!!")
                exit(0)
            else:
                
                for i in range(l):
                    e=int(input("Enter elements : "))

                    q.add_ele(e)
        return q
        


class Sequence:
    def __init__(self):
        self.ele=[]

    def add_ele(self,e):
        self.ele.append(e)
        print(self.ele)
        
    def find_result(self):
        largest=self.ele[0]
        smallest=self.ele[0]
        print(largest)
        for i in self.ele:
            if(largest < i):
                largest=i

            if(smallest > i):
                samllest=i
        print("Largest= %d" %largest)
        print("Smallest= %d" %samllest)



z=UI()
q=z.input()
largest = q.find_result()
