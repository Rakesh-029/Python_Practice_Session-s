list_1=[5,6,4,7,8,9]
print(list_1)

#--------------------------

list_1=[5,6,4,7,8,9]
list_2=set(list_1)
print(list_2)

#------------------------------


list_1=[5,6,4,7,8,9]
list_2=sum(set(list_1))
print(list_2)

#------------------------------


list_1=[5,6,4,7,8,9]
list_2=sum(set(list_1))*2
print(list_2)

#--------------------------------

n = 5
fact = 1
for i in range(n, 1, -1):
    fact *= i
print(fact) 

#----------------------------------

n=int(input("enter a number:"))
s=0
for i in range(1,11):
    s+=n*1
print(s)    

#-------------------------------------

n=int(input("enter the num:"))
print(n*55)


#------------------------------------


list_1 =[1,7,9,4,6,2]
target=7
for i in range(len(list_1)):
    if target==list_1[i]:
       print(i)
       break

list_1 =[1,2,3,4,5,6,7,8,9,10]
target=7
for i in range(len(list_1)):
    if target==list_1[i]:
       print(i)
       break   

#-----------------------------------

list_1 =[1,7,9,4,6,2]
target=7
start=0
end=len(list_1)-1
for i in range(len(list_1)):
    if target==list_1[i]:
       print(i)
       break     


#--------------------------------------

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11
start = 0
end = len(list_1) - 1
index = -1

while start <= end:
    middle = (start + end) // 2
    if list_1[middle] == target:
        index = middle
        
        start = end + 1  # makes while condition false
    elif list_1[middle] > target:
        end = middle - 1
    else:
        start = middle + 1

print("middle =", middle)
print("index =", index)
       

#-----------------------------------------------


n=int(input())
for i in range(1,n+1): #right angle triangle
    print("* "* i)

#------------------------------------------------

n = int(input())
for i in range(n, 0, -1): #inverted triangle
    print("* " * i)
   

#--------------------------------

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):    # number right angle triangle
        print(j, end=" ")
    print()



#------------------------------------


n = int(input())
for i in range(n, 0, -1):
    for j in range(1, i + 1):   # inverted right angle triangle
        print(j, end=" ")
    print()


#-------------------------------------

n = int(input())
for i in range(1, n + 1):
    str1 = ""                          #number triangle
    for j in range(1, i + 1):
        str1 = str1 + str(j) + " "
    print(str1)
       

#------------------------------------------


n=int(input())
for i in range(1,n+1):          #triangle
    print(" "*(n-i)+"+ "*i)


#-----------------------------------------


n=int(input())
for i in range(1,n+1):        
    if i==1 or i==n:           #hollow right angle triangle
        print(" *"*i)
    else:      
      print("*"+" "*(2*i-3)+" *")

#-----------------------------------



