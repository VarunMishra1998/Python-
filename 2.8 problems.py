##STUDENT ENROLLMENTS
'''
GIVEN A LIST OF TUPLE WITH INFO(name,subject)

info=
[

("Alice","Maths")
("Bob","Science")
("Alice","Science")
("Charlie","Maths"
("Alice","English")
("Alice","English")
("Charlie","English")

]

1. list all unique course
2. list students enroll in english
3. create dictionary (student, set of courses)
'''
# solution
info=[
("Alice","Maths"),
("Bob","Science"),
("Alice","Science"),
("Charlie","Maths"),
("Bob","Maths"),
("Alice","English"),
("Charlie","English")
]

#for tup in info:
    #print(tup)
    

'''op:
    ('Alice', 'Maths')
('Bob', 'Science')
('Alice', 'Science')
('Charlie', 'Maths')
('Bob', 'Maths')
('Alice', 'English')
('Charlie', 'English')
'''    
    #print(tup[0])

'''op:
Alice
Bob
Alice
Charlie
Bob
Alice
Charlie
'''
#print(tup[1])
'''o/p:
Maths
Science
Science
Maths
Maths
English
English
'''
#print(tup[0]) 
#print(tup[1])

'''o/p:
Science .....name
Alice   .....cource
Science
Charlie
Maths
Bob
Maths
Alice
English
Charlie
English
'''

#find list of unique courses
'''courses_set = set()
for tup in info:
             courses_set.add(tup[1])

print(courses_set) # {'Maths', 'Science', 'English'}'''

'''
here cources_set is a name type not work as container
set() is container

set() → creates the container

courses_set → name that refers to the container

.add() → puts values into the container

The container stores unique values
  '''
for name,courses in info:
    
    #print(name,courses)
    
    '''o/p:
Alice Maths
Bob Science
Alice Science
Charlie Maths
Bob Maths
Alice English
Charlie English

'''
# list the student enroll in english

    if(courses=="English"):
        print(name) 
    '''o/p:
       Alice
       charlie'''

# create dictionary (student,set of corses)

'''
d={}
for name , courses in info:

  if(d.get(name) == none)
   d.update({name : set()})
     d.[name].add(cources)
     else:
     d.[name].add(cources)

     print(d)

     # second method

     if name is not in d:
      d[name]=[]  # Create empty list to store "value"
     d[name].append(courses)
     print(d)
'''


'''
  List with duplicate values → count frequency

  lst = ["a", "b", "a", "c", "b", "a"]

d = {}
for item in lst:
    d[item] = d.get(item, 0) + 1

print(d)
 O/P:
 {'a': 3, 'b': 2, 'c': 1}

 ##d[items] update only key or value ,or both

1.item → the key in the dictionary

2.value → the value for that key

3.When you do this:

4.If the key does not exist:
Python creates a new key-value pair

5.If the key already exists:
Python updates only the value for that key

The key itself does not change

#EXPLANATION

Step-by-step explanation

We start with an empty dictionary:

d = {}

Iteration 1: item = "a"
d.get("a", 0) → 0   # "a" not in dictionary yet
d["a"] = 0 + 1      # assign 1 to key "a"


Dictionary now:

{"a": 1}

Iteration 2: item = "b"
d.get("b", 0) → 0   # "b" not in dictionary yet
d["b"] = 0 + 1      # assign 1 to key "b"


Dictionary now:

{"a": 1, "b": 1}

Iteration 3: item = "a"
d.get("a", 0) → 1   # "a" already exists with value 1
d["a"] = 1 + 1      # update value of "a" to 2


Dictionary now:

{"a": 2, "b": 1}

Iteration 4: item = "c"
d.get("c", 0) → 0   # "c" not in dictionary
d["c"] = 0 + 1      # assign 1 to key "c"


Dictionary now:

{"a": 2, "b": 1, "c": 1}

Iteration 5: item = "b"
d.get("b", 0) → 1   # "b" already exists with value 1
d["b"] = 1 + 1      # update value of "b" to 2


Dictionary now:

{"a": 2, "b": 2, "c": 1}

Iteration 6: item = "a"
d.get("a", 0) → 2   # "a" already exists with value 2
d["a"] = 2 + 1      # update value of "a" to 3


Dictionary now:

{"a": 3, "b": 2, "c": 1}

Step 7: Print the dictionary
print(d)


Output:

{'a': 3, 'b': 2, 'c': 1}

✅ Key Concept

d[item] → the key in the dictionary

d.get(item, 0) → gets the current value of that key (0 if not exist)

+1 → increments the count

d[item] = ... → updates the value for that key

Dictionary always stores key → value pairs

 '''  
