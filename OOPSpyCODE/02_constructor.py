'''A constructor is a special method in a class 
that is automatically called when you create an object.

__init__()

It is used to initialize (set up) the object’s data, usually instance variables.

class Person:
    def __init__(self, name, age):   # constructor
        self.name = name
        self.age = age

p1 = Person("Alice", 25)   # constructor runs automatically



# constructor runs automatically

example:-
class Student:
    def __init__(self):
        print("Constructor is running")

s1 = Student()   # Constructor is running

# Manually called

class Student:
    def __init__(self):
        print("Constructor is running")

s1.__init__()      # Constructor is running

output will be same but we dont need to write

s1.__init__() to access the object data

'''

#types of constructor

'''1️⃣ Default Constructor

A constructor that does not take any parameters (except self).

example:-
class Student:
   def __init__(self)
     print("default constuctor")
s1=Student()

here only one parameter "self"

✔ It does not receive values from the user.
✔ It may just print something or set default values.

2️⃣ Parameterized Constructor

A constructor that takes parameters (arguments).

example:-
class Student:
  def __init__(self,name,age)
     self.name=name
     self.age=age

s1=("varun",29)     

here more parameters are available 
along with self parameter

✔ It accepts values when the object is created.
✔ Used to initialize different data for different objects.

'''

'''
In python multiple constructor  not 
allowed in a single class
exmple:-

class Student:
 def __init__(self):
 print("object is being constructed")

 def __init__(self,name,cgpa)
       self.name
       self.cgpa

 def get_cgpa(self):
   return self.cgpa

s1=Student("rahul",9.0)
s2=Student("varun",9.1)   
s3=Student("mnglm",9.2)

print(f"{s1.name}has cgpa={s1.cgpa}")

output:-
rahul has cgpa=9.0

imp:-here if we use multiple __init__() constructor 
the last one is overwrite the previous ones


class Student:

def __init__(self,name,cgpa): # will be ignored
       self.name
       self.cgpa

def __init__(self):
 print("object is being constructed")      

def get_cgpa(self):
   return self.cgpa


s1=Student("rahul",9.0)
s2=Student("varun",9.1)   
s3=Student("mnglm",9.2)

print(f"{s1.name}has cgpa={s1.cgpa}")

here it will give syntax error 
because we pass two properties
during create the object and we have 
passed name and cgpa but there is only self
so it will give error

'''
'''

2️⃣ How to “simulate” multiple constructors in Python

Since Python allows only one __init__(), we can use default arguments or conditions inside it:

class Student:
    def __init__(self, name=None, cgpa=None):
        if name is None and cgpa is None:
            print("No info provided")
        elif cgpa is None:
            print("Name is:", name)
        else:
            print("Name:", name, "CGPA:", cgpa)

s1 = Student()              # No info provided
s2 = Student("Alice")       # Name is: Alice
s3 = Student("Bob", 9.2)    # Name: Bob CGPA: 9.2


Here, only one constructor exists, but it behaves like multiple constructors depending on arguments.

Python calls the same __init__() constructor, and the if-elif-else decides what happens.
The idea:

__init__() is always a single constructor in Python.

Inside __init__(), you can write if-elif-else conditions to handle different cases depending on the arguments.

Each condition can “act” differently when an object is created.

Because of this, __init__() behaves like multiple constructors, even though technically there is only one constructor.

Analogy:

Think of __init__() as a universal remote.

Pressing different buttons (conditions) makes it control TV, AC, or music system.

The remote itself is one device, but it behaves differently depending on what you press.



'''
class Student:

 def __init__(self,name,cgpa):
       #three positional argument sel,name,cgpa
       self.name
       self.cgpa
       
 def __init__(self):
  print("object is being constructed")      

 def get_cgpa(self):
   return self.cgpa


s1=Student("rahul",9.0)
# s2=Student("varun",9.1)   
# s3=Student("mnglm",9.2)

print(f"{s1.name}has cgpa={s1.cgpa}") # give syntax error