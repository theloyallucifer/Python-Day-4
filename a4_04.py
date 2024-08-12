s = input("Enter a string: ")
s = s.lower()
c = input("Enter a word to check the occurance: ")
c = c.lower()
count_word = 0
words = s.split()
for i in words:
    if i == c :
        count_word += 1
print(f"Occurance of {c} is {count_word} times...")