sentence = input("Enter a string: ")
words = sentence.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)