#Palindrome
n = int(input("Enter a number: "))
temp = n
sum = 0
while(n>0):
  r = n % 10
  sum = sum * 10 + r
  n = n // 10
if(temp==sum):
  print("It is a Palindrome number")
else:
  print("It is not a palindrome number")