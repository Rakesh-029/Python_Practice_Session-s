str1 = "All Silver tea cup."
for i in range(len(str1)):
    if str1[i]== " " and str1[i+1]!= " ":
        str1 =str1[ :i+1] + str1[i+1].upper()+str1[i+2:]
print(str1)        