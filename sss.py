a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
def min():
	if a>=b and a>=c:
		print(a,"is the largest")
	elif b>=a and b>=c:
		print(b,"is the largest")
	elif c>=a and c>=b:
		print(c,"is the largest")

min()
