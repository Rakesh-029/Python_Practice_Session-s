#convert str1 to pascal
str1 = 'All silver Tea Cup'
pascal = ''.join(word.capitalize() for word in str1.split())
print(pascal)
