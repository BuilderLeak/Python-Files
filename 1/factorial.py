#Factorial
a=int(input("Enter the number: "))
factorial = 1
i = 1
while i <=a:
  factorial = factorial * i
  print(i,"!=",factorial)
  i=i+1