'''
🔎 What is Exception Handling?

Exception handling is a method used to handle runtime errors 
so that the program does not crash 
and continues to execute smoothly.

An exception is an error that occurs during program execution.
example 
a=10
b=0
print(a/b)
o/p:
ZeroDivisionError

🔹 Basic Syntax
try:
    # Code that may cause error
except:
    # Code that runs if error occurs

    🔹 Example 1: Simple Exception Handling
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except:
    print("Error occurred")

If user enters 0 → Program will not crash.
'''
# # without try and except
# x=int(input("enter the x:"))
# ans=10/x
# print(f"ans is {ans}")


#with try and except
try:
    x=int(input("enter the x:"))
    ans=10/x
except ZeroDivisionError:
     print("divide by zero is not allowed")
except ValueError:
     print("invalid input")     
else:
     print(f"ans={ans}")
finally:
     print("end of the program")
'''
finally will execute always
if error is being throw or not
'''  
#list comprehension   


