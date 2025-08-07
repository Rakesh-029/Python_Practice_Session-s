# membership check
n=input().lower()
c=0
for i in n:
    if i in "aeiou":
        c+=1
print(c)  


# membership check
n=input().lower()
c=0
for i in n:
    if i not in "aeiou":
        c+=1
print(c)