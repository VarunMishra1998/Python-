'''
Attributes are variables that belong to a class or an object.
They are used to store information about the object or class.

imp:-attibutes are not belong to class and object at 
same time 

Types of Attributes

There are two main types:

1️⃣ Instance Attributes (Object-specific)

Belong to individual objects.

(self refers to the current
 object being created.

self.name and self.cgpa create 
separate attributes for each object.)

Each object can have different values.

Usually defined inside the constructor __init__() using self.

Example:
 class Student:
    def __init__(self, name, cgpa):
        self.name = name   # instance attribute
        self.cgpa = cgpa   # instance attribute

s1 = Student("Rahul", 9.0)
s2 = Student("Alice", 9.5)

print(s1.name, s1.cgpa)  # Rahul 9.0
print(s2.name, s2.cgpa)  # Alice 9.5

✅ Here:

self.name and self.cgpa are instance attributes.

Each object (s1, s2) has its own separate copy.

2️⃣ Class Attributes (Shared by all objects)

Belong to the class itself.

Shared by all objects of the class.

Usually defined directly inside the class, outside any method.

Example:

class Student:
    school = "ABC School"  # class attribute

s1 = Student("Rahul", 9.0)
s2 = Student("Alice", 9.5)

print(s1.school)  # ABC School
print(s2.school)  # ABC School
✅ Here:

school is a class attribute.

All objects share the same value.

'''
class Student:
    college_name="ABC college"
    pi=3.4

    def __init__(self,name,cgpa):
     self.name=name 
     self.cgpa=cgpa
     self.pi=3.5

s1=Student("varun",9.2)

print(s1.name)        #  varun
print(s1.college_name) # ABC college

''' HERE Object can access both:

Instance attributes

Class attributes'''

print(Student.college_name) # ABC college

'''HERE class can access 
only class atributes'''

print(s1.pi) # 3.5
'''when two attributes are same
(pi)then instance attribute will be print'''
print(Student.pi) # 3.4




