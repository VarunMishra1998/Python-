#sting--> sequence of character
'''
string can be created in single(''),diuble("") and triple quotes(''' ''')
generally we wrte single characters variables in single quote like ch='a'
indexing is also occure in string
'''

word="pyhton" #length :6
word3="pyth on" #length:7,space also refers as astring
print(len(word))
print(len(word3))

#concatenate
word1="i love"
word2="python"
varun=word1+ " " +word2
print(varun)

#indexing--start from zero

word="python"
print(word[0]) #p
print(word[2]) #t

# string is immutable

'''word="python"
word[2]='x' #(x)item
print(word) #o/p:'str' does not support item assignment
#x will not come place of t'''

#for loop

word="python"
for ch in word:
    print(ch) #o/p:p,y,t,h,o,n

#slicing in string

word="i study from apanacollege"
print(word[14:25]) #o/p:apanacollege
print(word[13:]) #o/p:apanacollege
print(word[13:len(word)]) #o/p:apanacollege
print(word[:len(word)]) #o/p: i study from apanacollege 
print(word[:]) #o/p: i study from apanacollege 
print(word[13:])  #o/p:apanacollege

'''place of 25 we can write nothing then syntax of slicing can understand that we want to go 
end of the string then  by default it will print the apanacollege
......str[st idx:end idx]...........
......starting index default value=0.......
......ending index default value = len(str).....'''

#reverse slicing
''' in reverse slicing the index start from -1 not from zero'''

word="python"
print(word[-4:-2]) #o/p: th
'''here indexing start from n to p in a reverse  way like 
p...-6
y...-5
t...-4
h...-3
o...-2
n...-1 '''

#strings formatting
'''when we want to create dynamic string then we use sting formatting 
dynamic string means jisake andar ham different variables and different values ko use kar sake
'''
#1. formate function---->formate()

a=5
b=20

print("languge is {}".formate("python")) #op-language is python
'''we also use string instead of variable'''

print("sum is {}".formate(sum)) #o/p:sum is 25
'''here {}-->placeholder where sum variable value will come'''

print("sum of {} and {} is {} ".formate(a,b,sum)) #o/p:sum of 5 and 20 is 25

## here also we use index bsed fortmatting 

print("sum of {1} and {0} is {2}".formate(a,b,sum)) #o/p:sum of 20 and 5 is 25
'''here indexing in a such way
a...0
b...1
sum...2'''

## f-string
'''it introduese in python 3.6
we use in f-string "literal srting interpolation" means
 we embed any variable or expression in string 
 f"{ }" IF Use parenthesis in string then
 we direct write any variable ans use expression
 and these variable and expression value will be evaluate as part of the string'''

a=5
b=25
print(f"sum of {a} and {b} is {a+b}") #sum of 5 and 20 is 25
print("avg of {a} and {b} is {(a+b)/2}") #avg of 5 and 20 is 12.5

