#Fibonacci Series
n = int(input("Enter a number: "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci series is: ", end = " ")
while(count <= n):
  count += 1
  print(a, end=" ")
  a = b
  b = sum
  sum = a + b