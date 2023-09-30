def gcd(a, b):
	if(b == 0):
		return a
	else:
		return gcd(b, a % b)
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("The gcd of ",a,"and ",b,"is: ",end="")
print(gcd(a, b))