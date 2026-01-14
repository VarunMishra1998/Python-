## operators-->>arithmatic, relational/comparison,assignment,logical
##ARITHMATIC
a=10
b=6

print(a+b)
print(a-b)
print(a*b)
print(a**b) #power
print(a/b) #division
print(a%b) #modulo

##RELATIONAL
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

##assignment variable
a=5 # 5 assign into 'a'
a+=10 #a=a+5 same as it is we can write for *,-,/
a**=2
print(a)

##LOGICAL
## 1.not(true covert into false vice versa)
var=False
print(not var)

##2.AND(only true-true = true )
a=5
b=10
print((b>a) and (a<b))
print((b>a)and (a>b))

## OR (only false-false =false)
print((a<b)or(a>b))


##operator precedence 
'''1.()
2.**
3.*,/,%   '''if same precedence occure then solve left to right 
example:-20/2*5--->>5*5=25
4.+,-
5.==,!=,>,>=,<,<=
6.not 
7.and
8.or'''
example:-2*(3+5) ##16
