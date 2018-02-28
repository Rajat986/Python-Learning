a=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    b=int(input("Enter element:"))
    a.append(b)

l=a[0]
#print(a[0])
for i in range(n):
    if (l<a[i]):
        l=a[i]
print("Largest element is:",l)
