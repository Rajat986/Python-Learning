a=str(input("Enter 1st Key: "))
b=str(input("Enter 1st Key's Value: "))
c=str(input("Enter 2nd Key: "))
d=str(input("Enter 2nd Key's Value: "))

def dictionary():

    dicti={a:b,c:d}

    print(dicti.keys())
    print(dicti.values())
    print("Required output is:")
    print(a,"=",b,";",c,"=",d)
    

dictionary()
