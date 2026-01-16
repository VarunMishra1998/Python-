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