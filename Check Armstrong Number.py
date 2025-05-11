num = int(input("Enter an integer: "))
n = len(str(num))
sum = 0
original = num

while original > 0:
    digit = original % 10
    sum += digit ** n
    original //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")