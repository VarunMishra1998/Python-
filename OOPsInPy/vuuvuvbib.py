# # Simple Calculator in Python

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error! Division by zero"

# # Menu
# # print("Select operation:")
# # print("1. Add")
# # print("2. Subtract")
# # print("3. Multiply")
# # print("4. Divide")

# # Take input from the user
# # choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # if choice == '1':
# print(f"{num1} + {num2} = {add(num1, num2)}")
# # elif choice == '2':
# print(f"{num1} - {num2} = {subtract(num1, num2)}")
# #elif choice == '3':
# print(f"{num1} * {num2} = {multiply(num1, num2)}")
# #elif choice == '4':
# print(f"{num1} / {num2} = {divide(num1, num2)}")
# #else:
# print("Invalid input")
# class Employee:
#         start_time= "5am"
#         end_time= "6pm"

#         def change_time(self,new_end_time): #method
#                 self.end_time=new_end_time
             

# class Teacher(Employee):
#         def __init__(self,subject):
#                 self.subject=subject

# class Adminstaff(Employee):
#         def __init__(self,role):
#                 self.role=role                

# t1=Adminstaff("manager")
# t1.change_time("7pm")

# print(t1.role,t1.start_time,t1.end_time) #manager 5am 7pm

# class Animal:
#      def make_sound(self):
#            print("some sound")

# class Dog(Animal):
#       def make_sound(self):
#             print("dog barks")

# d1=Dog()
# d1.make_sound()
# class Cat: 
#     def make_sound(self):   
#         print("mew mew")

# class Dog: 
#     def make_sound(self):
#         print("dog barks like bho,bho")

# # # Duck-typing function
# # def animal_sound(a):
# #     a.make_sound()  # we don’t care what type `a` is

# # Objects
# a1 = Cat()
# d1 = Dog()

# # Works with both
# a1.make_sound  # prints: some sound
# d1.make_sound  # prints: dog barks like bho,bho  


# class Teacher:
#       def get_designation(self):
#             print("dedignation=Teacher")

# class Accountant:
#       def get_designation(self):
#             print("designation=Accountant")


# t1=Teacher()
# t1.get_designation()

# acc1=Accountant()
# acc1.get_designation()

# Python program to demonstrate
# duck typing


# class Bird:
#     def fly(self):
#         print("fly with wings")

# class Airplane:
#     def fly(self):
#         print("fly with fuel")

# class Fish:
#     def swim(self):
#         print("fish swim in sea")
      

# # Attributes having same name are
# # considered as duck typing
# for obj in Bird(), Airplane():
#      obj.fly()

# class Student:
#     def study(self):
#         print("he is studing")

# def Myfunction(obj):
#     obj.study()

# stu1=Student()
# Myfunction(stu1)


# class Specialstring:
#     def __len__(self):
#         return 21

# list = Specialstring()
# print(len(list))
 
# class Student:

#     def study(self):
#         print("he is studying")

#     def myfunction(a):
#         a.study()

# stu1=Student()

# stu1.myfunction()         
    
# def factorial(n)
# def factorial(n):
#     varun=1
#     for i in range(1,n+1):
#        varun=varun*i
#     return varun

# user=int(input("enter the number"))
# print(factorial(user))
# def factorial(n):
#     varun=1
#     while n>0:
#         varun=varun*n
#     return varun
#     n=n-1
        
#     print(factorial(5))

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))

# for i in range(5):
#     if i==3:
#         continue
#     print(i)
# count=5
# while count >0:
#     if count==3:

#        pass

#     else:

#       print(count)
#     count-=1

# count=5
# while count>0:
#     if count==3:
#         pass
#     else:
        
#        print(count)
# count=count-1

# str=input("enter the string:")
# vowel=["a","e","i","o","u","A","E","I","O","U"]
# i=0
# last_char=""
# while i<len(str):
#     last_char=str[i] #overwrite
#     i=i+1
#     if last_char in vowel:
#         print("last character is vowel")
#     else:
#         print("last character is not vowel")    
    

# s = input("Enter a string: ")
# vowels = ["a","e","i","o","u","A","E","I","O","U"]

# i = 0
# last_char = ""
# while i < len(s):
#     last_char = s[i]  # overwrite each time, ends up with last char
#     i += 1

# if last_char in vowels:
#     print("The last character is a vowel")
# else:
#     print("The last character is not a vowel")
# def get_largest(a, b, c):
#     if (a > b and a > c):
#         return a
#     elif b > c:
#         return b
#     else:
#         return c

# print(get_largest(3, 10, 5))
# str=input("enter the string:")
# vowel=["a","e","i","o","u","A","E","I","O","U"]
# i=0
# last_char=""
# while i<len(str):
#     last_char=str[i] #overwrite
#     i=i+1
#     if last_char in vowel:
#         print("last character is vowel")
#     else:
#         print("last character is not vowel")
          
# square = [[], [], []] 

# square[0].append(5)
# square[1].append(5)
# square[2].append(5)

# print(square)
# marks=[10,20,30,40,50]
# num=30
# index=0
# for val in marks:
#     if(val==num):
#      print(index)
#      break
#     index+=1
# square = []
# for i in range(6):
#     square.append(i*i)
# print(square)



# square = [0]*6
# for i in range(6):
#     square[i] = i*i   # overwriting the index value
# # print(square)
# import json

# # data={"name":"varun",
# # "isTeacher":"true"}

# # json_string=json.dumps(data)
# # print(json_string)
# import json

# json_string = '{"name": "Alice", "age": 25, "is_student": false}'

# data = json.loads(json_string)
# print(data)
# print(type(data))

# class Student:
#     def __init__(self,name):
#         self.name=name
        
        

#     def set_grade(self,grade):
#         if grade <= 100:
#             self.grade=grade


#     def get_grade(self):

#             return self.grade


#     def get_info(self):
#         if self.grade>=50:
#              return "passed"
#         else:
#              return "fail"
        

# stu1=Student("varun")
# stu1.set_grade(40)
# print(stu1.get_grade(),stu1.get_info()) 


# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.grade=0
        

#     def set_grade(self,grade):
#         if grade <= 100:
#             self.grade = grade

#     def get_grade(self):
#         return self.grade

#     def get_info(self):
#         if self.grade >= 50:
#             return "passed"
#         else:
#             return "fail"


# stu1 = Student("varun")


# print(stu1.get_grade(), stu1.get_info())


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()    
        







