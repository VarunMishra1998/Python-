#question no.1
a=input("enter a age:")
print("hello varun, you are",a,"years old!")

#question no.2
a=int(input("enter a first number:"))
b=int(input("enter the second number:"))
sum=a+b
difference=a-b
product=a*b
quotient=a/b
print(sum,difference,product,quotient)

#question no.3
a=int(input("enter the first numberf:"))
b=int(input("enter the second number"))
c=float(input("enter the third number"))
print(float(a+b+c))
avg=(a+b+c)/3
print(avg)

#question no.4
number=input("enter the number:")
number1=int(number)
number2=float(number)
number3=str(number)
print(number1,type(number1))
print(number2,type(number2))
print(number3,type(number3))

# Q.5 expression 
x=10+3*2**2
print(x) #22

# Q.6swapping of two numbers
a=5
b=6
a=b
b=a
print(a)
print(b) #output:6,6 here value of a is lost so we will use third variable like "temp"

a=5
b=6
temp=a
a=b
b=temp
print(a)
print(b)

#another way to swapping of two value
a=5
b=6
a,b=b,a
print(a)
print(b)

#without using third variable swap two values
a=5  #101--> 3 bit
b=6  #110--> 3 bit
a=a+b #11--> 1011 --> 4 bit so it is taking 1 bit extra so we will use here XOR (^)
b=a-b #5
a=a-b #6
print(a)
print(b)

# USE XOR
a=5
b=6
a=a^b
b=a^b
a=a^b
print(a)
print(b)

#another way to swapping of two numbers 
a=5
b=6
a,b=b,a
print(a)
print(b)
'''here we will find from right side b,a when value of b,a will 
go into the stak then it get to reverse the value of b comes in a and the value of a in b
then both is assign in left side(a,b)'''

# Q.7 
a=input("enter the value in celsius:")
CelsiusTemperature=float(a)
print(CelsiusTemperature,type(CelsiusTemperature))
fahrenheitTemp=(CelsiusTemperature*(9/5))+32
print(fahrenheitTemp)

# Q8: Area of a circle
r = float(input("Enter the radius: "))
pi = 3.14

area = pi * r * r
print("Area of the circle:", area)

# Q9: Simple Interest

P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate (R): "))
T = float(input("Enter Time (T): "))

SI = (P * R * T) / 100
print("Simple Interest:", SI)

# Q10: Integer and fractional part (another way)

num = float(input("Enter a decimal number: "))

integer_part = int(num)
fractional_part = float(num - integer_part)

print("Integer part:", integer_part)
print("Fractional part:", (fractional_part))

