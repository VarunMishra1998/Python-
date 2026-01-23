#DICTIONARY
'''A dictionary is a built-in data type 
used to store data in key–value pairs.
key always unique ,duplicate value is not allwes
it is unodered because there is not use indexing'''

info={
    "name":"varun",
    "cgpa":8,
    "subject":["maths","science"],
    3.4:"pi"
}
print(info)
print(info[3.4]) #pi

#dictionary is a mutable and unodered
info["cgpa"]=9.8
print(info["cgpa"]) #9.8

#methods in dictionary

'''d.keys()  return all keys'''

print(info.keys())  
# dict_keys(['name', 'cgpa', 'subject', 3.4])

dic_keys=info.keys() 
print(dic_keys) # dict_keys(['name', 'cgpa', 'subject', 3.4])



'''d.values() return all values'''

dic_vals=info.values()
print(dic_vals) # dict_values(['varun', 8, ['maths', 'science'], 'pi'])

#we can convert it into list and return op will be in list
dic_keys=list(info.keys())
print(dic_keys) # ['name', 'cgpa', 'subject', 3.4]


'''d.items() return(key,val) pairs'''

print(info.items())
# dict_items([('name', 'varun'), ('cgpa', 9.8), ('subject', ['maths', 'science']), (3.4, 'pi')])



### d.get(val) return val acc. to key

'''importnt points:--> if we use dic[key] return vlue if exist in dictionary
if key not exist in dictionay it will give error and running of program stop
if we use dic.get() return value if exist in dictionay
if key not exist it will give "none" value and next line of code 
will execute'''
print(info.cgpa2()) #we use wrong key cgpa1
print("hello varun")

'''o/p:
print(info.cgpa2()) #we use wrong key cgpa1
          ^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'cgpa1'''

print(info.get("cgpa2"))
print("hello varun")

'''o/p:
none
hllo varun'''



#d.update(new_item) adds new item to dictionary
info.update({"city":"delhi"})
print(info)
# o/p:{'name': 'varun', 'cgpa': 9.8, 'subject': ['maths', 'science'], 3.4: 'pi', 'city': 'delhi'}
