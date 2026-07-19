'''
Docstring for OOPSpyCODE.05_OOPsPillars

1.Encpsulation
"wrapping data & funcion into single unit"
2.inheritance

3.polymorphism
4.abstraction


'''

#Ecapsulation:-
'''
Python Encapsulation
"wrapping data & funcion into single unit"
1.Encapsulation is about protecting data inside a class.
2.It means keeping data (properties) and methods together in a class, 
while controlling how the data can be accessed from outside the class.
3.This prevents accidental changes to your data and hides the 
internal details of how your class works.

'''
'''
class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public Attribute
        self.__balance=balance # private Attribute

    def get_info(self):
            print(f"name of employee is {self.name}")


emp1=BankAccount("varun",9000000) 
emp1.get_info() # name of employee is varun
print(emp1.__balance) #AttributeError: 'BankAccount' object has no attribute '__balance'
'''

'''
Explanation:

self.name = name: Public attribute, can be accessed directly.
self.__balance = balance: Private attribute, cannot be accessed directly.
emp1.get_info(): Prints "varun" because name is public.
print(emp.__balance): Raises an error because __salary is private and hidden.


'''

'''
Access Specifiers/access modifiers:-

Access specifiers define how class members (variables and methods) 
can be accessed from outside the class.
They help in implementing encapsulation by controlling the visibility of data.
There are three types of access specifiers:

1.public
2.protected
3.private

'''
#protected
'''
Protected members are variables or methods that are intended to be accessed only 
within the class and its subclasses. 
They are not strictly private but should be treated as internal. 
In Python, protected members are defined 
with a single underscore prefix (e.g., self._name).
'''
''''class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass'''

'''
Explanation:

self._age: Defined with a single underscore, marking it as protected.
SubEmployee: Inherits from Employee and can access _age directly.
Protected members should not be accessed outside the class hierarchy,
 but Python does not enforce this rule strictly
'''

#getter and setter
"it helps in get and update the "
"private atrributes values"


class BankAccount:
     def __init__(self,name,balance):
          
          self.name=name # public attribute
          self.__balance=balance #private attrivbute

     def get_balance(self):  # getter
               return self.__balance
          
     def set_balance(self,newBalance):  # setter
               self.__balance=newBalance

acc1=BankAccount("varun",50000)
acc1.set_balance(700000)
print(acc1.name,acc1.get_balance()) #varun 700000
print(acc1.name,acc1._BankAccount__balance) #varun 700000

'''
class Student:
    def __init__(self,name):
        self.name=name
        self.grade=0

    def set_grade(self,grade):
        if grade <= 100:
            self.grade=grade


    def get_grade(self):

            return self.grade

8uojilkm.
    def get_info(self):
        if self.grade>=50:
             return "passed"
        else:
             return "fail"
        

stu1=Student("varun")
stu1.set_grade(40)
print(stu1.get_grade(),stu1.get_info())


class Student:
    def __init__(self,name):
        self.name = name
        self.grade = 0

    def set_grade(self,grade):
        if grade <= 100:
            self.grade = grade

    def get_grade(self):
        return self.grade

    def get_info(self):
        if self.grade >= 50:
            return "passed"
        else:
            return "fail"


stu1 = Student("varun")

print(stu1.get_grade(), stu1.get_info())

#self.grade = 0 we initialise because
if we not pass or set grade then
it will return "0 fail" otherwise
we get error

'''

#inheritance

'''
#inheritance
"reusing attributes and method from parent(base) class"
Inheritance is a fundamental concept in object-oriented programming (OOP)
that allows a class (called a child or derived class) 
to inherit attributes and methodsfrom another class 
(called a parent or base class).

'''
#example of inheritence
class Employee:
        start_time= "5am"
        end_time= "6pm"

class Teacher(Employee):
        def __init__(self,subject):
                self.subject=subject

t1=Teacher("maths")
print(t1.subject,t1.start_time,t1.end_time)  # maths 5am 6pm   

'''
🔹 How This Shows Reusability

Teacher inherits from Employee

So Teacher automatically gets:

start_time

end_time

You did not rewrite those variables inside Teacher

👉 This is code reuse — the child class reuses properties of the parent class.

🔹 What Is Happening Internally?

When you create:

t1 = Teacher("maths")


Python looks for:

subject → found in Teacher

start_time → not in Teacher, so it checks Employee

end_time → not in Teacher, so it checks Employee

This process is called method resolution order (MRO).

'''
#example of inheritence
class Employee:
        start_time= "5am"
        end_time= "6pm"

        def change_time(self,new_end_time): #method
                self.end_time=new_end_time
             

class Teacher(Employee):
        def __init__(self,subject):
                self.subject=subject

t1=Teacher("maths")
t1.change_time("7pm")

print(t1.subject,t1.start_time,t1.end_time) #maths 5am 7pm

#example of inheritence
class Employee:
        start_time= "5am"
        end_time= "6pm"

        def change_time(self,new_end_time): #method
                self.end_time=new_end_time
             

class Teacher(Employee):
        def __init__(self,subject):
                self.subject=subject

class Adminstaff(Employee):
        def __init__(self,role):
                self.role=role                

t1=Adminstaff("manager")
t1.change_time("7pm")


print(t1.role,t1.start_time,t1.end_time) #manager 5am 7pm

"types of inheriteance"
#singel level inheritance
#multilevel inheritance
#multiple inheritance

"SINGLE LEVEL INHERITANCE"

#example
class Employee:
        start_time= "5am"
        end_time= "6pm"

class Teacher(Employee):
        def __init__(self,subject):
                self.subject=subject

t1=Teacher("maths")
print(t1.subject,t1.start_time,t1.end_time)  # maths 5am 6pm   

'''
Explanation:
1.Parent class (Employee):
Has class attributes start_time and end_time.
These are shared with all instances of Employee and its subclasses.
2.Child class (Teacher):
Inherits from Employee.
Has its own instance attribute "subject" initialized via "__init__".
3.Object creation:
t1 = Teacher("maths")

t1 has:
subject → "maths" (from Teacher)
start_time → "5am" (inherited from Employee)
end_time → "6pm" (inherited from Employee)

4.Output:
maths 5am 6pm

'''

"use super()"

'''
'''


class Employee:
        def __init__(self,start_time= "5am",end_time= "6pm"):
         self.start_time=start_time 
         self.end_time= end_time
        

class Teacher(Employee):
        def __init__(self,subject,start_time="5am",end_time="6pm"):
                super().__init__(start_time,end_time)
                self.subject=subject

t1=Teacher("maths")
print(t1.subject,t1.start_time,t1.end_time)  # maths 5am 6pm   


"""OR we can pass paramer in object"""

class Employee:
        def __init__(self,start_time,end_time):
         self.start_time=start_time 
         self.end_time= end_time
        

class Teacher(Employee):
        def __init__(self,subject,start_time,end_time):
                super().__init__(start_time,end_time)
                self.subject=subject

t1=Teacher("maths","5am","6am")
print(t1.subject,t1.start_time,t1.end_time)  # maths 5am 6pm 

"MULTILEVEL INHERITANCE"

'''Employee
      ↑
  Adminstaff
      ↑
  Accountant

Adminstaff is child of Employee

Accountant is child of Adminstaff

Accountant indirectly inherits from Employee
'''

# 1️⃣ Base Class
class Employee:
    def __init__(self, start_time, end_time):
        # 2️⃣ Initialize common attributes for all employees
        self.start_time = start_time
        self.end_time = end_time


# 3️⃣ First Level Inheritance (Adminstaff inherits Employee)
class Adminstaff(Employee):
    def __init__(self, role, start_time, end_time):
        # 4️⃣ Call parent (Employee) constructor first
        super().__init__(start_time, end_time)
        
        # 5️⃣ Add new attribute specific to Adminstaff
        self.role = role


# 6️⃣ Second Level Inheritance (Accountant inherits Adminstaff)
class Accountant(Adminstaff):
    def __init__(self, role, salary, start_time, end_time):
        # 7️⃣ Call parent (Adminstaff) constructor first
        super().__init__(role, start_time, end_time)
        
        # 8️⃣ Add new attribute specific to Accountant
        self.salary = salary


# 9️⃣ Creating an object of Accountant
a1 = Accountant("manager", 900000, "6am", "8pm")

# 🔟 Accessing attributes of the object
print(a1.role, a1.salary, a1.start_time, a1.end_time) # manager 900000 6am 8pm


"MULTIPLE INHERITANCE"

'''
A single class inherits from more than one parent class.
              "OR"
Multiple inheritance =
One child class inheriting from two or more parent classes.              

Parent1     Parent2
     \       /
        Child

The child gets features from both parents.

'''
#parent(1 RED)
class Employee:
       def __init__(self,name):
              self.name=name

       def work(self):
              return "pyment working in google company"    



#parent(2)
class Salary:
       def __init__(self,salary):
              self.salary=salary

       def years(self):
              return "for 25 years"     


#child class inheriting from two parent 

class Manager(Employee,Salary):
       def __init__(self,name,salary):
              
            ''' Employee .__init__(self,name)
             Salary.__init__(self,salary)'''
            
            "or use super()"

            super().__init__(name)
            Salary.__init__(self,salary)
            
                       
              
        
m1=Manager("varun",90_00000)               
print(m1.name,m1.salary,m1.work(),m1.years())


'''op-varun 9000000 pyment working in google company for 25 years'''


"Abstrhiaction"
'''
hiding internal details and showing only
essential features

'''


from abc import ABC, abstractmethod

# 🔹 Animal → ABSTRACT CLASS
class Animal(ABC):

    # 🔹 make_sound → ABSTRACT METHOD
    @abstractmethod
    def make_sound(self): 
        print("some sounds") # Parent class method
        pass


# 🔹 Lion → NORMAL (Concrete) CLASS
class Lion(Animal):

    # 🔹 make_sound → NORMAL METHOD (Implementation)
    def make_sound(self):
        print("Roar")  


# 🔹 Cow → NORMAL (Concrete) CLASS
class Cow(Animal):

    # 🔹 make_sound → NORMAL METHOD (Implementation)
    def make_sound(self):
        print("Maa")  # Child class method overrides parent


# 🔹 Object creation of normal classes
l1 = Lion()
l1.make_sound()

c1 = Cow()
c1.make_sound()

'''
🔹 Analogy

Parent = Teacher’s rule: “Do homework”

Child = Student writes actual homework

Child’s action overrides parent’s instruction

like here..
some sound-->parent rule
roar-->child actual action
'''

#with or without abstract method

# without abstractmethod code

from abc import ABC

class Animal(ABC):
    def make_sound(self):
        pass  # normal method, does nothing

# Subclass does not implement make_sound
class Lion(Animal):
    pass

l1 = Lion()
l1.make_sound()  # ✅ Works, but prints nothing


#with abstractmethod

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # normal method, does nothing

# Subclass does not implement make_sound
class Lion(Animal):
    pass
l1 = Lion()
l1.make_sound()  # give error

'''
main purpose of an abstract method is to enforce that 
every child class must implement it(the abstract method).
means:
1.Python says: “Every subclass must implement make_sound().”
example-->class Lion(Animal):
    def make_sound(self):   # ✅ Implementation
        print("Roar") # Actual code

l1 = Lion()
l1.make_sound()  # Prints "Roar"

2.If the subclass does not implement "make_sound()" → object creation will give an error
 example--> class Lion(Animal):
                 pass
            l1 = Lion()
            l1.make_sound()  # give error

"pass"
“pass is a placeholder that does nothing, used when no code is written yet.”

example-->
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # do nothing here
        
 make_sound() exists, but has no code

pass tells Python: “Syntax is okay, but there’s nothing to execute here”

The child class will provide the real code

without pass-->

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
  # nothing here ❌

Python gives SyntaxError

So we write pass to make it valid
'''

#####POLYMORPHISM

"POLYMORPHISM"

'''
poly-->many
morphism--> forms

Polymorphism in Python

Polymorphism means:

One name, many forms.

example-->
1.operator overloading-->
print(1+2,"hello"+"world")
same operator--> "+" ,work-->multiple(add,concatenation)
                /   \
             add     concatenation
        this is the ex. of polymophism 

In Python, polymorphism allows the 
same method name 
to behave differently 
depending on the object.

🔹 Types of Polymorphism in Python

1.Duck Typing
2.Method Overriding
3.Operator Overloading
4.Function Polymorphism (same function works for different types)


'''
"2️⃣ Method/function Overriding (Runtime Polymorphism)"
"overriding occures where inheritance involved"
'''if any function is in parent class
if we redefing same function in child class
then it is called as overriding'''
#example
class Animal:
     def make_sound(self):   
           print("some sound")

class Dog(Animal):
      def make_sound(self):
            print("dog barks like bho,bho")

d1=Dog()
d1.make_sound()  #dog barks 
'''
Which overrides what?

👉 Dog.make_sound() overrides Animal.make_sound().

Why?

Dog inherits from Animal

Both classes have a method with the same name: make_sound

The child class (Dog) provides its own implementation

our understanding--->
| Syntax            | Inheritance                  | Notes                            |
| ----------------- | ---------------------------- | -------------------------------- |
| `class Animal():` | inherits `object` by default | Parentheses optional in Python 3 |
| `class Animal:`   | inherits `object` by default | Shorter and more common style    |

our uderstanding--->
code-->
    class Student:
    def study(self):
        print("he is studing")

def Myfunction(a): #outside the class
    a.study()

stu1=Student()
Myfunction(stu1)

Explanation-->

tep 1: Class definition
class Student:
    def study(self):
        print("he is studying")

    def  Myfuction(a):
         a.study()  



Here you define a class called Student.

It has one method study() that prints "he is studing".

Nothing executes yet, this is just a definition.

Step 2: Function definition
def Myfunction(a): 
    a.study() 

You define a function Myfunction that takes one parameter a.

Inside, it calls a.study().

Still nothing executes yet, just defining the function.

Step 3: Create an instance of Student
stu1 = Student()

Here you create an object stu1 of the class Student.

Python automatically calls the constructor __init__() (default one) to create the object.

Now stu1 is an instance of Student.

Step 4: Call Myfunction
Myfunction(stu1)

This is the first actual execution in the program.

Python calls Myfunction and passes stu1 as the argument a.

Inside Myfunction, the line a.study() is executed.

Here a refers to stu1.

So Python calls the study() method of stu1.

Inside study(), Python executes:

print("he is studing")

Output:-he is studing


'''

"DUCK TYPING"

class Teacher:
      def geta_degignation(self):
            print("dedignation=Teacher")

class Accountant:
      def geta_degignation(self):
            print("designation=Accountant")


t1=Teacher()
t1.get_designation()

acc1=Accountant()
acc1.get_designation()

#example 2

class Specialstring:
      def __len__(self):
            return 21
      
      
sp=Specialstring()
print(len()) # 21


'''It's duck typing because len() works on any object(string,list,tuple) that has a __len__() method,
regardless of its actual type.'''

#example 3
# Python program to demonstrate
# duck typing


class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swim in sea")

# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    obj.fly()


'''
explanation--->
What happens:

Bird → has fly() ✅ → works

Airplane → has fly() ✅ → works

Fish → does not have fly() ❌ → Python raises AttributeError

AttributeError: 'Fish' object has no attribute 'fly'
Why this is duck typing (when correct):

Duck typing means “if it behaves like a duck, treat it as a duck”.

Here, Python only cares that an object has a fly() method.

The type of object doesn’t matter (Bird or Airplane).

'''            
