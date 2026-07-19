'''type conversion:-(iplicit type conversion where python interpreter automatically convert it)
convert one type data into another type'''

'''example:-->
int--->float
float--->int
int=--->bool'''
ans2=5+10.0 ##automatic conversion
print(ans2,type(ans2))

'''type casting :-(explicit type conversion where developers change the type)
in type casting we use function like int(),float(),bool() '''
ans1=int(5+10.0) ##type castind
print(ans1,type(ans1))

'''FOR boolean value-->> (true or false) true means value 1 and false means value 0'''
val1=bool(0) 
val2=bool(10)
val3=bool(-10)
print(val1) #false
print(val2) #true
print(val3) #true
