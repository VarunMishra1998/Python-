'''
OOPS:-Object-Oriented Programming is a way of writing programs using objects that bundle:

data → variables (called attributes)

behavior → functions (called methods)

Think of an object as a real-world thing.

it is mapping real word objects in code

1️⃣ Definition

Instance ek specific object hai jo class se bana ho.

Class = blueprint (jaise house ka design)

Instance = actual house (jo design ke hisaab se bana ho)

An instance method is a function defined inside a class 
that operates on the data of a particular object (instance) and
 can access instance variables using self.

 class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

Student → class (blueprint)

Ab objects create karte hain:

stu1 = Student("Rahul", 9.8)
stu2 = Student("Varun", 8.6)

stu1 → instance of Student/instances of the class
stu2 → another instance of Student/instances of the class

imp: for defing parameters (subject,cgpa,address) again and again
of each students of a college is a big problem
so we use class and objects

class--blueprint of an object
 define how my objects look like

 object:it is intance of class.
 this is the actual thing which take place in memory

Reasons Why We Use OOPS
1️⃣ Code Reusability

OOPS allows reuse of code using inheritance.
➡️ Less duplication, less effort.

2️⃣ Easy Maintenance

Programs are divided into small objects, so fixing or updating code is easier.

3️⃣ Better Organization

Code is organized into classes and objects, making it clean and structured.

4️⃣ Data Security

Encapsulation protects data by restricting direct access.

'''

'''
class Student:
    subject = "python"
    college= "ABC"
    year= "4rth  year"

stu1= Student()
stu2= Student()
print(stu1.subject,stu1.college,stu2.year) # python ABC 4rth  year
print(stu2.subject,stu2.college,stu2.year)  # python ABC 4rth  year

imp:if we want to check for large no. of student then
we use loop here 
'''

# create methods in class

'''
CONSTRUCTOR
1. __init__ method
this mehod is known as consructor

__init__method use to initialise our object
we call this every time when we create new objects.
 
# __init__this gets called automatically.
ex: class Student:
      sub="python"
    stu1=Student()
    print(stu1.sub) # python

   imp:--> Do parentheses () call __init__?

❌ No — not directly
✅ They call the class

Calling the class may result in __init__ being called, but only as part of the process.

constructor are that function which create  or construct  object in
 programming language 

if we want to write self then we write 
def __init__(self)
here "self" is by default parameter
place of self we write anything like abc,nbh bla bla .....
self parameter storing
current instances of the class 


'''
'''
class Student:
    def __init__(self):
        print("constructor was called...") 

stu1= Student()  # constructor was called...
stu2=Student() # constructor was called...
  
✅ 5-Line Exam Answer

1.When Student() is written, Python calls the class, not __init__ directly.

2.Python first uses __new__() to create a new object in memory.

3.After the object is created, Python automatically calls __init__() if it is defined.

4.If __init__() is not defined, object.__init__() is used, which does nothing.

5.__init__() is executed once for every object created.

## What does self mean?

self means: the current object (instance)

It represents which object is calling the method.



'''
'''
class Student:
    def __init__(self,name,cgpa):
        
        self.name=name
        self.cgpa=cgpa

stu1=Student("rahul",9.8)
stu2=Student("varun",8.6)
stu3=Student("mohan",9.5)

print(stu1.cgpa) # 9.8
print(stu2.name) # varun
print(stu3.name) # mohan

'''
class Student:
    def __init__(self,name,cgpa):
        
        self.name=name #self.name-->instace variable
        self.cgpa=cgpa #self.cgpa-->instace variable
        '''“An instance variable stores data specific to that object.”

It means:

Instance variable → a variable that belongs to one object.

Stores data → keeps information.

Specific to that object → only for that particular object, not shared with others.

Simple Example

Imagine a class called Car.

Each car has:

color

speed

If you create two cars:

car1 = Car("Red", 120)
car2 = Car("Blue", 150)


car1 has color Red

car2 has color Blue

The color of car1 does NOT affect car2.

So the color is specific to each object.'''

    def get_cgpa(self):   # instace method

        '''1️⃣ Instance method ka kaam

Instance method ka main kaam hota hai ek specific object (instance) ke andar
 store data (instance variables) ko access ya modify karna.'''
        
        return self.cgpa #gets the CGPA of that particular object.
 

stu1=Student("rahul",9.8)
stu2=Student("varun",8.6)
stu3=Student("mohan",9.5)

print(f'{stu1.name} has cgpa={stu1.get_cgpa()}') # rahul has cgpa=9.8



"our understanding"
'''
🔥 Case 1️⃣: Parameters Pass Karna (Dynamic Values)

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

c = Car("Red", 120)

print(c.color)
print(c.speed)

✔ Har object ki value alag ho sakti hai
✔ Flexible design
✔ Real-world projects me mostly ye use hota hai

🔥 Case 2️⃣: Direct Assign Karna (Fixed Values)

class Car:
    def __init__(self):
        self.color = "Red"
        self.speed = 120

c = Car()

print(c.color)
print(c.speed)

✔ Simple
✔ Har object same value lega
✔ Testing ya simple examples me useful

🔥 Case 3️⃣: Default Parameters (Best Combination)

class Car:
    def __init__(self, color="Red", speed=120):
        self.color = color
        self.speed = speed

c1 = Car()
c2 = Car("Blue", 150)

print(c1.color, c1.speed)
print(c2.color, c2.speed)

✔ Flexible
✔ Default bhi milta hai
✔ Professional approach
'''



