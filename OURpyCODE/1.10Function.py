# Functions

# Function Definition
def hello():
    print("hello from Prime")

hello() # Function Call

# Fnx to compute sum of 2 nums

def sum(a, b):         # a & b are parameters
    return a + b

print(sum(5, 10))      # 5 & 10 are arguments


# Fnx to computer average of 3 nums

def avg(a, b, c):           
    return (a + b + c) / 3

print(avg(1, 2, 3))


 #sum() fnx with default param 1

def sum(a, b = 1):         # default val of b is 1
    return a + b

print(sum(5))

# Factorial of N
n = int(input("enter n: "))

fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial = ", fact)

"or"
def factorial(n):
    varun=1

    for i in range(1,n+1):
       varun=varun*i
       return varun
    # user=int(input("enter the number:"))
    # print(factorial(user)) # enter the number:?
    print(factorial(5)) # 120

"or"
def factorial(n):
    varun=1
    while n>0:
        varun=varun*1
        n=n-1
    return varun
    print(factorial(5))

"or use recursion "  

def factorial(n):
    if n==0:
        return 0
    return n*factorial(n-1)
print(factorial(5))

'''
🔄 Complete Execution of factorial(5)

Function calls happen like this:

factorial(5)
= 5 × factorial(4) # first call n=5
= 5 × (4 × factorial(3)) # second call n=4
= 5 × (4 × (3 × factorial(2))) #third call n=3
= 5 × (4 × (3 × (2 × factorial(1)))) # fourth call n=2
= 5 × (4 × (3 × (2 × (1 × factorial(0))))) fifth call n=1

Now base case:

factorial(0) = 1

Then calculation happens in reverse:

factorial(1) = 1 × 1 = 1
factorial(2) = 2 × 1 = 2
factorial(3) = 3 × 2 = 6
factorial(4) = 4 × 6 = 24
factorial(5) = 5 × 24 = 120

Final Output:
120

IN recursion there is no need
to define variable to store 
return value because there
is temporary memory automatiaclly
created to store it
'''


# Largest of 3 nums - a, b, c

def get_largest(a, b, c):
    if (a > b and a > c):
        return a
    elif b > c:
        return b
    else:
        return c

print(get_largest(3, 10, 5))

'''# Multiple built-in fnx
print()
range()
input()
type()'''