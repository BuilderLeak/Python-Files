#Average of 5 marks
sub1=int(input("Enter 1st subject marks: "))
sub2=int(input("Enter 2nd subject marks: "))
sub3=int(input("Enter 3rd subject marks: "))
sub4=int(input("Enter 4th subject marks: "))
sub5=int(input("Enter 5th subject marks: "))
total=sub1+sub2+sub3+sub4+sub5
avg=total/5

print("Toatal marks are: ",total)
print("The Average marks are: ",avg)

if avg>=90:
 print("The Gade is O")
elif avg>=80:
 print("The Gade is A")
elif avg>=70:
 print("The Gade is B")
elif avg>=60:
 print("The Gade is C")
elif avg>=50:
 print("The Gade is D")
elif avg>50:
 print("Fail")