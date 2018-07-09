class UI:
    def input_sequence():
        w=c_sequence()
        m=int(input("Enter number of elements in sequence %d : " %(j+1)))
        for i in range(m):
                ele=int(input("Enter sequence %d element %d : " %((j+1),(i+1))))
                w.add_ele_to_seq(ele)
        return w
    def input_sequences(self):
        n=int(input("Enter number of sequences : "))
        for j in range(n):
            w=self.input_sequence()
            q.add_seq_to_seqs(w)
        return(q)

    def output(self,inp)
        for i in inp.sequences:
            print("Smallest : %d \nLargest  : %d \nSecond Smallest : %d \nSecond Largest  : %d\n" % (i.small,i.large,i.s_small,i.s_large)
                  
class c_sequence:
    def __init__(self):
        self.sequence=[]

    def add_ele_to_seq(self,element):
        self.sequence.append(element)

    def result(self):
        small=self.sequence[0]
        large=self.sequence[0]
        s_large=self.sequence[0]
        s_small=self.sequence[0]

        
        #for i in range(len(self.sequence)):

            #if(small > self.sequence[i]):
            #    small=self.sequence[i]
            #if(large < self.sequence[i]):
            #    large=self.sequence[i]
        # We can do the above for Largest and smallest but for 2nd smallest and largest the below is better. Initializing small, large, s_small, s_large is not needed for the below method.
        rem_repeat=set(self.sequence)
        self.large=max(rem_repeat)
        rem_repeat.remove(large)
        self.s_large=max(rem_repeat)

        self.small=min(rem_repeat)
        rem_repeat.remove(small)
        self.s_small=min(rem_repeat)   
        return(small, large, s_small, s_large)

class c_sequences:
    def __init__(self):
        self.sequences=[]

    def add_seq_to_seqs(self,seq):
        self.sequences.append(seq)
    def compute(self):
        for i in self.sequences:
            result = i.result()
    
        


a=UI()
b=a.input()
c = b.compute()
#or
#b.compute()
#a.output(b)
