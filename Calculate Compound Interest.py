principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): ")) / 100
time = float(input("Enter time in years: "))
n = int(input("Enter number of times interest is compounded per year: "))

compound_interest = principal * (1 + rate/n)**(n*time) - principal
print("Compound Interest:", compound_interest)