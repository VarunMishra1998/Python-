# # f = open("FileHandlingCODE/sample.txt","r")
# # data = f.read()
# # print(data) 
# # f.close()
# # '''o/p:-
# # hii i am varun
# # from prayagraj
# # uttar pradesh
# # india
# # '''
# # '''
# # "reads mode is a default mode"
# # if we not wrete "r" then
# # it will be assuming that we try to
# # read data into sample.txt
# # then it give data whatever will be in
# # file
# # example-->
# # f = open("FileHandlingCODE/sample.txt")
# # data = f.read()
# # print(data) 
# # f.close()

# # o/p:-
# # hii i am varun
# # from prayagraj
# # uttar pradesh
# # india

# # '''
# # f = open("FileHandlingCODE/sample.txt","r")

# # data = f.readline()
# # print(data)

# # f.close()
# # '''o/p:-
# # hii i am varun
# # '''

# # f = open("FileHandlingCODE/sample.txt","r")

# # data = f.readline()
# # print(data)

# # data = f.readline()
# # print(data)
 
# # f.close()
# # '''
# # What readline() Does

# # readline() reads only one line at a time from the file.

# # Every time you call:

# # data = f.readline()
# #       print(data)

# # 👉 The file pointer moves to the next line.
# # first call-->data = f.readline()
# # give o/p-hii i am varun

# # then file pointer moves to the next line
# # second call--data = f.readline()
# #                   print(data)
# # give o/p-from prayagraj              
# # '''

# # '''o/p:-
# # hii i am varun
# # from prayagraj
# # '''

# # "write data"

# # f = open("FileHandlingCODE/sample.txt","r")

# # data = f.readline()
# # print(data)

# # data = f.readline()
# # print(data)
 
# # f.close()

# # "w-overwrite"

# # '''if i use "w"
# # i write "hii i am manglam"
# # in smple.text alredy data given
# # "hii i am varun
# # from prayagraj
# # uttar pradesh
# # india"
# # then because of "w"
# # into sample.text given data 
# # get to clean and new data added
# # "hii im am mangalam
# # from prauagraj"
# # this is called overriding '''

# # #example-->
# # f=open("FileHandlingCODE/sample.txt","w")
# # data=f.write("hii im manglam \n from prayagraj")
# # print(data)
# # f.close()

# # '''o/p:-
# # hii im am mangalam
# # from prauagraj
# # '''

# # #append()
# # f=open("FileHandlingCODE/sample.txt","a")
# # data=f.write("\nwhat about you varun")
# # print(data)
# # f.close()
# # '''o/p:-
# # hii im manglam 
# #  from prayagraj.what about you varun
# #  append me jaha se hamara line khatm hoga
# #  usi ke aage se new line append hoga
# # '''
# # f=open("FileHandlingCODE/sample.txt","a")
# # data=f.write("\nwhat about you varun")
# # print(data)
# # f.close()
# # '''o/p:-
# # hii im manglam 
# #  from prayagraj.
# # what about you varun
# # '''

# # f=open("FileHandlingCODE/sample.txt2","x")
# # data=f.write("\nwhat about you varun")
# # print(data)
# # f.close()
# # "a new file create"
# # "name sample.txt2"
# # "in file new data added"
# # "o/p- what about you varun"

# # f=open("FileHandlingCODE/sample.txt2","r+")

# # data=f.write("123")
# # print(data.read()) ❌
# # '''
# # ❌ What is Wrong?

# # f.write("123") returns number of characters(3) written (an integer).

# # So data becomes an integer, not a file object(f).

# # You cannot use .read() on an integer.

# #like print(3.read()) it is wrong

# # Also, in "r+" mode, the file pointer moves to the end after writing.

# # f=open("FileHandlingCODE/sample.txt2","r+")
# # f.write("123")
# # print(f.read())

# # '''o/p:-
# # lo varun what about you
# # her 123 replce the "Hel"
# # '''
# # '''
# # for our understanding
# # | Mode | Read | Write      | Delete Old Data | Pointer Start |
# # | ---- | ---- | ---------- | --------------- | ------------- |
# # | `r`  | ✔    | ❌          | No              | Beginning     |
# # | `r+` | ✔    | ✔          | No              | Beginning     |
# # | `w`  | ❌    | ✔          | ✔               | Beginning     |
# # | `w+` | ✔    | ✔          | ✔               | Beginning     |
# # | `a`  | ❌    | ✔ (append) | No              | End           |
# # | `a+` | ✔    | ✔ (append) | No              | End           |
# # | `x`  | ❌    | ✔          | Error if exists | Beginning     |

# # '''
# # #'with' keywords
# # #ex: open("data.txt","r") as f:
# # # print(f.read())

# # with open("FileHandlingCODE/sample.txt2","r") as f:
# #  data=f.read()
# # print(len(data))
# # '''o/p:
# # lo varun what about you
# # 26
# # '''

# # #delete files
# # '''to delete files we use "os module"
# # which is built in module in python
# # it stands for operting system
# # the os module provides the remove()
# #  function to delete files in Python.
# # '''
# # import os

# # os.remove("FileHandlingCODE/sample.txt2")

# #word searching


# # with open("FileHandlingCODE/sample.txt","r") as f:
 
# #  data=f.readline()
# #  print(data)

# #  data=f.readline()
# #  print(data)

# #  data=f.readline()
# #  print(data)

# # '''o/p:
# #  hii i am manglam 

# # from prayagraj

# # what about you varun
# #  '''

# # #use loop
# # data=True
# # with open("FileHandlingCODE/sample.txt","r") as f:
 
# #  while data:
# #   data=f.readline()
# #   print(data)
# '''o/p:
#  hii i am manglam 

# from prayagraj

# what about you varun
#  '''
# "check 'varaun' is found or not"
# # data=True

# # with open("FileHandlingCODE/sample.txt","r") as f:
 
# #  while data:
# #   data=f.readline()
  
# #   if "varun" in data:
# #    print("word found")
# #    break
   
# #   print(data)
# '''o/p:
#  hii i am manglam 

# from prayagraj

# word found
#  '''
data=True
i=1

with open("FileHandlingCODE/sample.txt","r") as f:
 
 while data:
    data=f.readline()

    if "varun" in data:
      print(f"word found at line {i}")
      break
    else:
      print(f"word not found at line {i}")  

    print(data)
    i=i+1
'''o/p:-
word found at line 3
'''
    
    



  
 









