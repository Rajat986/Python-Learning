class UI:
    def input(self):
        q=()
        
        n=int(input("Enter number of vertices : "))
        for i in range(n):
            
            l=int(input("Enter %d element : " %(i+1)))

            q.add_element(l)
class digraph:
    def __init__(self):
        self.vertices=[]

    def add_vertex(self,e):
        self.ele.apped(e)
        print(self.ele)

    def find_cycle_particpants(self):
        pass

    def find_sortest_path(self,vertexno):
        pass
    





a=UI()
dg=a.input()
df.find_cycle_participants()
for i in df.vertices:
    print(df.find_shortest_path(i))
