#SETS
'''a set is a built-in data type 
used to store unique, unordered elements.
SETS can be mutable but each element of sets 
can't be mutable i.e immutable
list and dictionary can't use here becsuse it is
mutable built in function
duplicate value cant be store in sets'''

s={1,2,2,2,2,3}
print(s) # {1,2,3}
print(len(s)) # 3
print(type(s)) # <class 'set'>

#it is mutable
s.add(5)
print(s) #{1,2,3,5}

# creating empty set
empty_set = set()
print(empty_set)
print(type(empty_set)) #<class 'set'>

empty_set={}
print(type(empty_set)) #<class 'dictinary'>

#sets method
'''
s.add() add value
s.remove() remove value
s.clear() empty the set
s.pop() removes a randome value
s.union(set2) return new union (print uniqe elements)
s.intersection(set2) reurn new intersection (print common elements)
'''

# s={1,2,2,2,3}

print(s) #{1,2,3}

s.add(5)
print(s) # {1, 2, 3, 5}

s.remove(5)

print(s) # {1, 2, 3}

s.pop()
print(s) #{2, 3}

s.clear()
print(s) # ()


## union and intersection
'''
UNION

A = {1, 2, 3}
B = {3, 4, 5}

union_set = A | B
print(union_set)  ## o/p: {1, 2, 3, 4, 5}

print(A.union(B))  ## o/p:  {1, 2, 3, 4, 5}

'''



'''
INTERSECTION

A= {1, 2, 3}
B = {3, 4, 5}

print(A.intersection(B))  ## o/p: {3}

intersection_set = A & B
print(intersection_set)   ## o/p: {3}

'''
