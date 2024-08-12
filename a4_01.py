
c_a = 0
c_e = 0
c_i = 0
c_o = 0
c_u = 0


s = input("Enter a string: ")


for i in s:
    if i == 'a' or i == 'A':
        c_a+=1
    elif i == 'e' or i == 'E':
        c_e+=1
    elif i == 'i' or i == 'I':
        c_i+=1
    elif i == 'o' or i == 'O':
        c_o+=1
    elif i == 'u' or i == 'U':
        c_u+=1

print(f"Total no. of vowels are:\na = {c_a}\ne = {c_e}\ni = {c_i}\no = {c_o}\nu = {c_u}")

