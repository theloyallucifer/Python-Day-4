str = input("Enter a string: ")
last = str[-1]
new_str = str[:-1].replace(last,"*") + last
print("Modified string: ", new_str)
