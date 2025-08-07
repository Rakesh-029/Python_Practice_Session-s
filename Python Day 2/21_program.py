l1=input()
l2=sorted(l1)
print(l2)

#-------------------------------------------

l1=input()
l2=sorted(l1)
print(l2[len(l2)-1])

#-------------------------------------------

l1=input().split()
print(l1)

#-------------------------------------------

l1=input().split()
l2=list(map(int,l1))
print(l2)

#-------------------------------------------


l2=list(map(int, input().split()))
l2.sort()
print(l2)


#----------------------------------------------


l2 = list(map(int, input().split()))
l2.sort()
print("Sorted list:", l2)
i = len(l2) - 1     
highest = l2[i]
print("Highest number:", highest)

#----------------------------------------------



l2 = list(map(int, input("Enter numbers separated by space: ").split()))
l2.sort()
print("Sorted list:", l2)
i = len(l2) - 1 
lowest = l2[0] 
print("Lowest number:", lowest)

#-----------------------------------------------



l2 = list(map(int, input("Enter numbers separated by space: ").split()))
l2.sort()
print("Sorted list:", l2)
i = len(l2) - 1       
highest = l2[i]
lowest = l2[0]        
print("Highest number:", highest)
print("Lowest number:", lowest)

#------------------------------------------------------
