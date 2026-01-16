# Conditional Statements - Example 1
age = int(input("enter age: "))

if age >= 18:           # if true/false, entire block of code is executed
    print("you can vote")
    print("you can drive")
else:
    print("you can't vote")
    print("you can't drive")

    # Example 2 - Traffic Lights
color = input("enter color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Look")
elif color == "green":
    print("Go")
else:
    print("wrong color")

   # Example 3
age = int(input("enter age: "))

if age < 13:
    print("child")
elif (age >= 13 and age < 18):
    print("teenager")
else:
    print("adult")

    # Example 4 - Login System
username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("login successful!")
elif username != "admin":
    print("wrong username, try again.")
else:
    print("wrong password, try again.")

    # Example 5 - num multiple of 5 or not
num = int(input("enter number: "))

if num % 5 == 0:
    print("multiple of 5")
else:
    print("NOT a multiple of 5")

    # Example 6 - Odd or Even
num = int(input("enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

    # Login system Same as Example 4

username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("login successful!")
else:
    if username != "admin":        # Nesting
        print("wrong username, try again.")
    else:
        print("wrong password, try again.")

 