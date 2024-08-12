str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if len(str1) != len(str2):
    print(f'"{str1}" and "{str2}" are not anagrams.')
else:
    char_count1 = 0
    char_count2 = 0
    
    for char in str1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1
    
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    
    if char_count1 == char_count2:
        print(f'"{str1}" and "{str2}" are anagrams.')
    else:
        print(f'"{str1}" and "{str2}" are not anagrams.')
