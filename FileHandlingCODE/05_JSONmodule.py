'''
✔ In simple words:
JSON Object = Key + Value pairs inside { }
JSON Object = Data stored as key and value pairs inside { }.

✔ In very simple words

JSON Object → { "key":"value" }
JSON String → '{"key":"value"}' (JSON written as text)

| Feature | JSON Object                   | Python Dictionary                    |
| ------- | ----------------------------- | ------------------------------------ |
| Format  | Text format for data exchange | Python data structure                |
| Quotes  | Uses **double quotes " "**    | Can use **single ' ' or double " "** |
| Example | `{ "name": "Rahul" }`         | `{'name': 'Rahul'}`                  |
| Usage   | Used in **APIs, web data**    | Used in **Python programs**          |

Simple Meaning

Text format → Data written as readable characters (text).

Data exchange → Sending data from one program/system to another.

So,

'''

'''
3️⃣ Convert JSON → Python (Deserialization)
Use json.loads():- to convert 
a JSON string into a Python object.
2️⃣ Convert Python → JSON (Serialization)

Use json.dumps():- to convert
a Python object into a JSON string.


'''

import json

json_str='{"name":"varun","isTeacher":true}'

py_obj=json.loads(json_str)
print(py_obj)

'''o/p:-
{'name': 'varun', 'isTeacher': True}
'''
import json

data={
    "name":"varun",
    "isTeacher":True,
    "address":{
        "city":"delhi",
        "country":"India"
    },
    "subject":["python","AI/ML"]

}

json_object=json.dumps(data)
print(json_object)

'''o/p:-
{"name": "varun", "isTeacher": true, 
"address": {"city": "delhi", "country": "India"}, 
"subject": ["python", "AI/ML"]}

o.u-
"isTeacher":True, if we write true place of
True it will give error but in sring not
because it present in single quotes
like:
json_str='{"name":"varun","isTeacher":true}'
'''
#deal with file
'''
when we deal with file then we will
use json.load() ans json.dump()
for string:
json.loads()
json.dumps()
'''

import json
with open("FileHandlingCODE/data.json","r") as f:
    py_object=json.load(f)
    print(py_object)
    '''
    {'name': 'varun', 'isTeacher': 'true',
      'address': {'city': 'delhi', 'country': 'India'}, 
      'subject': ['python', 'AI/ML']}
    '''
#overwrite
import json
data={
"name":"varun",
"age":"27",
"isTeacher":True

}
with open("FileHandlingCODE/data.json","w") as f:
    py_obj=json.dump(data,f,indent=4,sort_keys=True)

    '''
    information in data.json looks like
    {"name": "varun", "age": "27", "isTeacher": true}
    after usin indent=4 looks like
    {
    "name": "varun",
    "age": "27",
    "isTeacher": true
}
when using short_keys=True 
information then looks like

{
    "age": "27",
    "isTeacher": true,
    "name": "varun"
}
    
    '''
    

