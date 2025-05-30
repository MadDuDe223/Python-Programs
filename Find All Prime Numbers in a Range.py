def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print(f"Prime numbers between {start} and {end} are:", end=" ")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")