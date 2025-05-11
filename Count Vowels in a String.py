s = "Hello World"
vowels = "aeiou"
count = sum(1 for c in s.lower() if c in vowels)
print("Vowel count:", count)