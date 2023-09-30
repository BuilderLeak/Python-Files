#GCD
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
a = num1
b = num2
while num1 != num2:
  if num1 > num2:
    num1 -= num2
  else:
    num2 -= num1
print("GCD of", a, "and", b, "is", num1)
  