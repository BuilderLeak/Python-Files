#Compound Interest
principal=int(input("Enter principal amount: "))
years=int(input("Enter number of years: "))
rpr=int(input("Enter the interest rate per year: "))
sr = principal*rpr*years/100
print("Compound interest for principle amount Rs",principal,"/- for",years,"years at the rate of ",rpr,"%per year is",sr,"")