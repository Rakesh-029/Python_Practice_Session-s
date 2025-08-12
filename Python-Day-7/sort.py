
#Two Sum Problem in Python
nums =[1,6,4,5,3]
target = 11
res = "-1"
flag = False

for i in range(len(nums)-1):
    nums[i]
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            res = nums[i], nums[j]
            flag = True
            break
    if flag:
        break

print(res)


# "Two Sum Problem using Hashing (Set) — Python"
nums = [1, 6, 4, 5, 3]
target = 11
unique = {1, 6, 7}

for i in nums:
    required = target - i
    if required in unique:
        print(i, required)
        break
    else:
        unique.add(i)





# "Two Sum Problem using Hashing (Set) — Python"
nums = [1, 6, 4, 5, 3]
target = 11
unique = set()

for i in nums:
    required = target -i
    if required in unique:
        print(i,required)
    unique.add(i) 
    

#"Finding Missing Elements in a Sequence"
nums =[1,2,3,4,5]

for i in range(len(nums)-1):
    if nums[i]+1 != nums[i+1]:
        print(nums[i]+1)
        break


#"Finding Missing Elements in a Sequence"
nums =[1,2,4,5]

for i in range(len(nums)-1):
    if nums[i]+1 != nums[i+1]:
        print(nums[i]+1)
        break    


#diven n-1 integers in the range 1 to n with n duplicates,"find the missing no."
#"Finding a Missing Number Using Sum Formula"
n=5
nums =[1,2,3,4,5]

sum1 =sum(range(1,n+1)) # (or) sum1 = n*(n+1)//2
sum2 =sum(nums)
print(sum1-sum2)


# #List Rotation in Python (using slicing)
l = [1, 2, 3, 4, 5]
k = int(input("Enter rotation value: "))
rotation = k % len(l)  # To handle rotations greater than list length
print(l[-rotation:] + l[:-rotation])

