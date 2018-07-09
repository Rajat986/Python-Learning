class UI:
    def input(self):
        n=int(input("Enter number of sequences : "))
        q=c_sequences()
        for j in range(n):
            m=int(input("Enter number of elements in sequence %d : " %(j+1)))
            w=c_sequence()
            for i in range(m):
                ele=int(input("Enter sequence %d element %d : " %((j+1),(i+1))))

                w.add_ele_to_seq(ele)
            print()
            q.add_seq_to_seqs(w)
        return(q)

    def output(self,inp):
        for i in inp.sequences:
            t=i.result()
            print("Smallest : %d \nLargest  : %d \nSecond Smallest : %d \nSecond Largest  : %d\n" %t)

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
        large=max(rem_repeat)
        rem_repeat.remove(large)
        s_large=max(rem_repeat)

        small=min(rem_repeat)
        rem_repeat.remove(small)
        s_small=min(rem_repeat)

        
            
        return(small, large, s_small, s_large)

class c_sequences:
    def __init__(self):
        self.sequences=[]

    def add_seq_to_seqs(self,seq):
        self.sequences.append(seq)
        


a=UI()
b=a.input()
a.output(b)
