'''
methods are functions that are defined inside a class 
and 
are used to operate on " objects of that class".

There are three main types of methods in Python:
1.instace method
2.class method
3.static method
'''
#instance method

#Original method with return

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self): #instance method
        return f"Laptop has {self.RAM} RAM and {self.storage} {self.storage_type}"

l1 = Laptop("16gb", "512gb")
l1.get_info()      # ❌ nothing is printed
print(l1.get_info())  # ✅ this prints the info
#o/p:-Laptop has 16gb RAM and 512gb ssd

#Method with print instead of return

class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage} {self.storage_type}")   

l1=Laptop("16gb","512gb")
l2=Laptop("8gb","256gb")

l1.get_info()   #✅ this prints the info automatically
#Laptop has 16gb RAM and 512gb ssd

#HERE INSTANCE METHOD ACSESS BOTH
# CLASS AND INSTACE ATTRIBUTES 


#class method

class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    @classmethod
    def get_storage_type(cls): #cls:-parameter 
        print(f"Laptop has {cls.storage_type} type storge")   

l1=Laptop("16gb","512gb")
l2=Laptop("8gb","256gb")

Laptop.get_storage_type() # Laptop has ssd type storge
l1.get_storage_type() # Laptop has ssd type storge

'''
cls is a conventional name used in a class method to refer to the class itself,
 just like self refers to the instance in regular methods.
 🔹 Why Use cls?

Because it gives access to class-level data and methods.
 '''

#Static methods

class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    @classmethod
    def get_storage_type(cls):
          print(f" Laptop has storage type {cls.get_storage_type}")

        #instance methods
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM ,{self.storage} and {self.storage_type} type")

    @staticmethod
    def cacl_discount(price,discount):
          final_price=price-(price*discount/100)
          print(f"discount price={final_price}")

#create objects OUTSIDE the class
l1=Laptop("16gb","512gb")
l2=Laptop("8gb","256gb")   

l1.cacl_discount(40_000,10) # 36000.0


'''
Question:-
design and create an online store for products(name,price)
Track total products being creted.
create astatic method to calculate discount on each products based on a % parameter
'''
"#design and create an online store for products(name,price)"
class Products():
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.count +=1

        Products.count +=1

        
    def get_info(self):
        print(f"{self.name}  price is {self.price}")

 # create object outside the class

p1=Products("phone",100000)
p2=Products("laptop",400000)
p1.get_info() # phone  price is 100000


"#Track total products being creted"

class Products():
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.count +=1

        Products.count +=1

        '''if we take self.count istead of product.count
then the count will unchanges and it creates new instaces
"p1.count" and stores in object'''
    def get_info(self):
        print(f"{self.name}  price is {self.price}")

    @classmethod

    def get_count(cls):
                  
        print(f"product in store {cls.count}")

 # create object outside the class

p1=Products("phone",100000)
p2=Products("laptop",400000)
p1.get_info()     #phone  price is 100000
Products.get_count() #Products in store 2

"create astatic method to calculate discount on each products based on a % parameter"

#Static methods

class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    @classmethod
    def get_storage_type(cls):
          print(f" Laptop has storage type {cls.get_storage_type}")

        #instance methods
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM ,{self.storage} and {self.storage_type} type")

    @staticmethod
    def cacl_discount(price,discount):
          final_price=price-(price*discount/100)
          print(f"discount price={final_price}")

#create objects OUTSIDE the class
l1=Laptop("16gb","512gb")
l2=Laptop("8gb","256gb")   

l1.cacl_discount(40_000,12) # 36000.0



'''
Exlanation of code:-

1️⃣ When Python Reads the Class
class Products():


Python:

Creates a class object in memory.

Stores everything inside the class block.

Does NOT create any products yet.

When Python sees:
count = 0


It creates a class variable.

Stored inside the class.

Shared by all future objects.

Memory idea:

Products
 ├── count = 0
 ├── __init__
 ├── get_info
 └── get_count

🏭 2️⃣ When You Create an Object
p1 = Products("phone", 100000)


Here is what really happens internally:

Step 1: Python creates empty object
help of __new__() method
p1 → (empty Products object)

Step 2: Python automatically calls:
__init__(self, "phone", 100000)


Now:

self = p1

name = "phone"

price = 100000

Step 3: These lines run
self.name = name


Now p1 has:

p1.name = "phone"

self.price = price


Now:

p1.price = 100000

Products.count += 1


This means:

Products.count = 0 + 1
Products.count = 1


Notice:

count is NOT stored in p1.

It stays in the class.

All objects share it.

same process will occure for second objectcs(p2)
'''


