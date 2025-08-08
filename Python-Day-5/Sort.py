''''
m = int(input())
n = int(input())

# Define is_prime function
def is_prime(num):
    if num < 2:
        return
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return
    print(num, end=" ")  # print in same line with space

if m > n:
    print("enter valied range")
elif (m < 0 and n <= 1):
    print("enetr valied range")
else:
    for i in range(m, n + 1):
        is_prime(i)
    
'''

'''
def add(x,y):
    return(x+y)
a=int(input())
b=int(input())    #retuning a value
c=add(a,b)
print(c)       
'''

'''
#factorial program using recursion
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))        
'''

'''
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
print(fact(0)) 
'''

'''
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
n=int(input())    
print(fact(5)) 
'''

'''
#1st 10 natural num
def fact(n):
    if n<=1:
        return 1
    return n+fact(n-1)
n=int(input())    
print(fact(n)) 
'''


'''
#fibnoci program using recursion
def fibb(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1    
    return fibb(n-1) + fibb(n-2)  


n=int(input())
for i in range(n):
    print(fibb(i))
'''

'''
# list conversion of a range object in Python
c = list(range(1, 5))
print(c)

'''

'''
# membership operator concept in Python, combined with a loop and conditional statements
for i in range(1, 5):
    if i in [3, 4]:
        print(i)

'''

'''
#sets
a=2
set_a= {5,"six",a,8.2}
print(type(set_a))
print(set_a)
'''

'''
#Dictionaries
dict_a={"name": "Ram","age":15}
print(dict_a)
'''

'''

class iphone:
    def icloud(self):
        print("free 5gb space")
    def call(self,number):
        print("calling....",number)
iphone16pro = iphone()
no = int(input("Enter the num:"))
print(type(iphone16pro))
iphone16pro.call(no)            

'''

'''

class student:
    def add(self, name, rollno, branch):
        self.rollno = rollno
        self.name = name
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Branch:", self.branch)

s1 = student()
s1.add("ram", 1, "eee")
s1.display()

'''

'''

class student:
    def __init__(self, name, rollno, branch):
        self.rollno = rollno
        self.name = name
        self.branch = branch

    def call(self):
        print("method called")

s1 = student("ram", 1, "ece")
s1.call()  

'''

'''
# Inherantance
class student:
    def add(self, name, rollno, branch):
        self.rollno = rollno
        self.name = name
        self.branch = branch

def __del__(self):
    print("destructor called")
s1 = student()
s1.add("ram", 1, "eee")    
print(s1.name)

'''

'''
# Inherantance
class student:
    def __init__(self, name, rollno, branch):
        self.rollno = rollno
        self.name = name
        self.branch = branch

def __del__(self):
    print("destructor called")
s1 = student("ram", 1, "eee")
print(s1.name)

''' 


'''

class AmazonsService:
    def __init__(self, Agentname,agentId,custId):
        self.custId = custId
        self.Agentname = Agentname
        self.agentId = agentId

Agentname ="ram"
AgentId = 1

complaint =input('Enter  your Issue :')
customerId = int(input("enter cus Id :"))
while complaint:
    Agent1 = AmazonsService(Agentname,AgentId,customerId)
    complaint = False
print("Agent",Agent1.agentId,"is handling customer : ",Agent1.custId)    

'''







          