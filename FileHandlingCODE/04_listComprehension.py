'''List Comprehension in Python is a 
concise way to create lists 
using a single line of code.
It combines a for loop and optional conditions into 
one readable expression.

1. Basic Syntax
list=["expression" for "item" in "iterable"]
OR
["output" for "item" in "iterable" "if conditionig"]
    \-->this output in the form of variable(i)
    o/p:[0,1,4,9,6,25]
    i*i-->output
    ietrable-->for i in range(6)
    list=[output,iterable,condition]


expression → what you want to add to the list
item → each element from the iterable
iterable → sequence like list, tuple, string, range
'''
#example:
square=[]
for i in range(6):
    square.append(i*i)
print(square) #[0, 1, 4, 9, 16, 25]

#using list comprehension
list=[i*i for i in range(6)]
print(list) #[0, 1, 4, 9, 16, 25]

#with condition
list=[i*i for i in range(6) if i%2!=0]
print(list) #[1, 9, 25]

#overwrite -value with zero
num=[-2,-4,8,9,-9]
num=[0 if val<0 else val for val in num]
print(num) #[0, 0, 8, 9, 0]

#wthout USING list comprehension
words=["apple","mango","anar"]
print(words[0].upper()) #APPLE
#USING list comprehension
words=[val.upper() for val in words]
print(words) #['APPLE', 'MANGO', 'ANAR']



















