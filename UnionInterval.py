class UI:
    def input(self):
        inst_s=union_instance_s()

        n=int(input("Enter number of instances : "))
        for i in range(n):
            q=interval_s()
            r=int(input("Enter number of inputs for instance %d : " %(i+1)))
            for i in range(r):
                a=int(input("Enter upper bound of interval %d : " %(i+1)))
                b=int(input("Enter lower bound of interval %d : " %(i+1)))
                r=interval(a,b)
                q.add_to_intervals(r)
            w=union_instance(q)
            inst_s.add_to_instances(w)
        return inst_s


class interval:
    def __init__(self,u,l):
        self.u=u
        self.l=l

class interval_s:
    def __init__(self):
        self.intervals=[]

    def add_to_intervals(self,inter):
        self.intervals.append(inter)

class union_instance:
    def __init__(self,ins):
        self.ins=ins

class union_instance_s:
    def __init__(self):
        self.instances=[]

    def add_to_instances(self,insta):
        self.instances.append(insta)

    def compute

import pdb
pdb.set_trace()
a=UI()
b=a.input()

