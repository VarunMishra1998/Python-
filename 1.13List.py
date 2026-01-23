## list
'''mutable sequence of value
here square bracket id used
supose we have marks1=50,marks=60,marks=70,marks=80
rather than this we use list like 
mark=[50,60,70,80]'''

marks=[50,60,70,80]
print(marks) #o/p:[50,60,70,80]
print(marks[1])# o/p:60
print(len(marks))# o/p:4

# it is mutable 

marks[2]=90
print(marks) #o/p:[50,60,90,80]

#in list we can store different types of value also

mark=[20,330,40,50,"abc",100.10]
print(type(mark))# <class,list>

# slicing is also occure in list  same as string
marks=[20,30,50,60,"abc,70,80"]
print(marks[0:4]) #o/p:[20,30,50,60]'''

# l.append(val)  add one element at the end
# l.indert(inx,val) insert element at idx
# l.sort() arranges in incresing order
#  l.reverse() revers order

marks=[1,2,3]

marks.append(4)
print(marks)    #o/p:[1,2,3,4]

marks.insert(2,10)
print(marks) #o/p:[1,2,10,3,4]

marks.sort()
print(marks) #o/p:[1,2,3,4,10]

marks.reverse()
print(marks) #o/p[10,4,3,2,1]
'''
o/p:
[1, 2, 3, 4]
[1, 2, 10, 3, 4]
[1, 2, 3, 4, 10]
[10, 4, 3, 2, 1]
'''
# loops in list
#it is also called as linear search

marks=[10,20,30,40,50]
varun=30
index=0
for val in marks:
    if(val==varun):
     print(f"{varun} found at index={index}")
    break
    index=index+1 

    '''
| val | index | val == varun? | Action         |
| --- | ----- | ------------- | -------------- |
| 10  | 0     | No            | index → 1      |
| 20  | 1     | No            | index → 2      |
| 30  | 2     | Yes           | print 2, break |

    '''

