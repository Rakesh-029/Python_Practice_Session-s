str1 = "all silver tea cup."
str1=str1[0].upper()+str1[1:]
for i in range(len(str1)):
    if str1[i]== " " and str1[i+1]!= " ":
        str1 =str1[ :i+1] + str1[i+1].upper()+str1[i+2:]
print(str1)