num = int(input("Enter an integer: "))
sum_digits = sum(int(digit) for digit in str(num))
print("Sum of digits:", sum_digits)