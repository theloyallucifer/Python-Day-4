s = input("Enter a string: ")

s= s.lower()
s= s.replace(" ","")

if s == s[::-1] :
    print("The string is palindrome.")
else :
    print("The string is not palindrome.")