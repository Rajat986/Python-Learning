class UI:
    def input(self):
        q=dis_to_cycle()
        
        n=int(input("Enter number of vertices : "))
        for i in range(n):
            
            l=int(input("Enter %d element : " %(i+1)))

            q.add_element(l)
class dis_to_cycle:
    def __init__(self):
        self.ele=[]

    def add_element(self,e):
        self.ele.append(e)
        print(self.ele)

    





a=UI()
a.input()
