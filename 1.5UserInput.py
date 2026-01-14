## input()
a=input("enter the value:25")
print(a) ## take i/p=25 then o/p:25

username=input("enter your name:")
print("welcome",username) ## let take i/p:varun then o/p:welcome varun

##type casting in input() function
a=input("enter value a:") ## before type casting
b=input("enter value b:")
sum=a+b
print(sum)

'''let take a=10 and b=5 then o/p=105 istead of 15 because
whatever we write in input function that will be string so there is requre type casting'''
a=int(input("enter value a:")) ##after type casting
b=int(input("enter value b:"))
sum=a+b
print(sum) 

## avg of two numbers
a=int(input("enter a 1st number:"))
b=int(input("enter a 2nd number:"))
avg=(a+b)/2
print("avg of two nubers:",avg)