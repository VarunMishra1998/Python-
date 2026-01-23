#TUPLES
'''Immutable sequence of value
here we use parenthesis"()" to create tuple
in tuple we can store value in string and float form same as list 
'''
tup=(1,2,3,4,5)

print(tup)   #(1, 2, 3, 4, 5)
print(type(tup)) # <class 'tuple'>
print(len(tup)) # 5
print(tup[2]) # 3

#tuple is immutable
tup(2)=20
print(tup) # 'tuple' object does not support item assignment

# create single value tup 

tup=(1) # tuple-->❌
print(type(tup)) #<class,'int'>

tup=("abc")# tuple-->❌
print(type(tup)) #<class,'str'>


'''this is not tuple
because python interprete it as a expression'''

tup=(1,) #tuple-->✅
print(type(tup)) #<class,'tuple'>

tup=("abc",) #tuple-->✅
print(type(tup)) #<class,'tuple'>


#slicing in list
tup=(1,2,3,4,5)
print(tup[0:3]) # 1,2,3
print(tup[:3]) # 1,2,3
print(tup[:]) # 1,2,3,,4,5

# loop in tuple
tup=(1,2,3,4,5)
for val in tup:
    print(val) 
    '''
    o/p: 
1
2
3
4
5
    '''

#sum of the tuple
tup = (10, 20, 30)
total = 0
for val in tup:
    total += val

print(f"sum of vals is {total}")

## tuples method
# t.index(val)  return first occurence index
# t.count(val)   counts total occuttence

tup=[1,2,2,3,2,4]
print(tup.index(2)) # 1
''' here value 2 is exist at three different indexes 1,2,4
but during indexing from left to right fist occurrence 
of 2 index will come '''
print(tup.count(2)) # 3

