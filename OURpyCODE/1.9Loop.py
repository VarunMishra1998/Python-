# While Loop - Example 1

while True:        # DO NOT RUN - an infinite loop
    print("Prime")

# Example 2 - print 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 3 - print 5 to 1
i = 5
while i > 0:
    print(i)    
    i -= 1

# Multiplication table of N
n = int(input("enter n: "))
i = 1

while i <= 10:
    print(i * n)     
    i += 1


# Break & Continue

# Break for multiple of 6
i = 1

while i <= 10:
    if(i % 6 == 0):
        break
    print(i)           # 1, 2, 3, 4, 5, break
    i += 1

# Skip multiples of 3
i = 0
'''
| Iteration | i | i % 6 == 0 | Action            |
| --------- | - | ---------- | ----------------- |
| 1         | 1 | False      | print 1           |
| 2         | 2 | False      | print 2           |
| 3         | 3 | False      | print 3           |
| 4         | 4 | False      | print 4           |
| 5         | 5 | False      | print 5           |
| 6         | 6 | True       | break (stop loop) |
'''

# continue
i=0
while(i < 10):
    i += 1
    if(i % 3 == 0):
        continue;      # 1, 2, continue, 4, 5, continue, 7, 8, continue, 10
    print(i)
    '''
| Loop check  | i after `i += 1` | i % 3 == 0 | Result                |
| ----------- | ---------------- | ---------- | --------------------- |
| i=0 < 10 ✅  | 1                | No         | print 1               |
| i=1 < 10 ✅  | 2                | No         | print 2               |
| i=2 < 10 ✅  | 3                | Yes        | continue (skip print) |
| i=3 < 10 ✅  | 4                | No         | print 4               |
| i=4 < 10 ✅  | 5                | No         | print 5               |
| i=5 < 10 ✅  | 6                | Yes        | continue              |
| i=6 < 10 ✅  | 7                | No         | print 7               |
| i=7 < 10 ✅  | 8                | No         | print 8               |
| i=8 < 10 ✅  | 9                | Yes        | continue              |
| i=9 < 10 ✅  | 10               | No         | print 10              |
| i=10 < 10 ❌ | —                | —          | loop ends             |

    '''



# Print odd nums from 1 to 10 using continue
i = 0
while(i < 10):
    i += 1
    if(i % 2 == 0):
        continue;      # 1, 3, 5, 7, 9
    print(i)

    

    # for Loop - Example 1

for i in range(5):     # 0, 1, 2, 3, 4
    print(i)

    # Membership Operator("in")

# Chars of a string
word = "Prime"

for ch in word:
    print(ch)

# Check if char 'i' exists in word
if 'i' in word:
    print("letter exists")

    # Example 2 - count number of i's in word

word = "artificial intelligence"

count = 0

for ch in word:
    if ch == 'i':
        count += 1

print(f"i occurs {count} times.")

'''dry run:

| Step | ch      | ch=='i'? | count (after step) |
| ---- | ------- | -------- | ------------------ |
| 1    | a       | No       | 0                  |
| 2    | r       | No       | 0                  |
| 3    | t       | No       | 0                  |
| 4    | i       | Yes      | 0 → 1              |
| 5    | f       | No       | 1                  |
| 6    | i       | Yes      | 1 → 2              |
| 7    | c       | No       | 2                  |
| 8    | i       | Yes      | 2 → 3              |
| 9    | a       | No       | 3                  |
| 10   | l       | No       | 3                  |
| 11   | (space) | No       | 3                  |
| 12   | i       | Yes      | 3 → 4              |
| 13   | n       | No       | 4                  |
| 14   | t       | No       | 4                  |
| 15   | e       | No       | 4                  |
| 16   | l       | No       | 4                  |
| 17   | l       | No       | 4                  |
| 18   | i       | Yes      | 4 → 5              |
| 19   | g       | No       | 5                  |
| 20   | e       | No       | 5                  |
| 21   | n       | No       | 5                  |
| 22   | c       | No       | 5                  |
| 23   | e       | No       | 5                  |

'''

'''## **Step-by-Step Explanation**

1. **`word = "artificial intelligence"`**

   * Stores the sentence *artificial intelligence* in the variable `word`.

2. **`count = 0`**

   * Initializes a counter to 0 because **we haven't counted any 'i' yet**.

3. **`for ch in word:`**

   * Loops through **each character** in the string `word`.
   * Each character is temporarily stored in the variable `ch`.

4. **`if ch == 'i':`**

   * Checks if the current character is `'i'`.

5. **`count += 1`**

   * If the character is `'i'`, increase `count` by 1.

6. **`print(f"i occurs {count} times.")`**

   * Prints the total number of times `'i'` appears.
   * `f"{count}"` is an **f-string**, which lets you put the value of `count` directly into the string.

---'''

# Example 3 - count vowels in word
for ch in word:
    if (ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a'):
        count += 1

print(f"vowel count = {count}")


 #range()

# 0, 1, 2, 3, 4 
for i in range(5):
    print(i)

# 1, 2, 3, 4 , 5
for i in range(1, 6): #range(start, stop)

    print(i)
    '''start → the first number in the sequence (included)

stop → the number up to which to go, but not included

So, Python counts from start up to stop - 1.'''

# 1, 3, 5, 7, 9
for i in range(1, 10, 2): #range(start, stop, step)
    print(i)
    '''start → where to start counting (included)

stop → where to stop counting (excluded)

step → how much to increase the number each time'''

# Sum of first n natural nums

n = int(input("enter n: "))
sum = 0
for i in range(1, n+1):
    sum += i

print("sum = ", sum)
'''If we wrote range(1, n), the last number n would not be included.

That’s why we write n+1 to make Python include n.'''

#write a program to print last ch is vowel or not

str=input("enter the string:")
vowel=["a","e","i","o","u","A","E","I","O","U"]
i=0
last_char=""
while i<len(str):
    last_char=str[i] #overwrite
    i=i+1
if last_char in vowel:
        print("last character is vowel")
else:
        print("last character is not vowel")    
'''o/p:
enter the string:apple
last character is vowel
    
    '''
"what happend if we weite if,else iside the while loop"

str=input("enter the string:")
vowel=["a","e","i","o","u","A","E","I","O","U"]
i=0
last_char=""
while i<len(str):
    last_char=str[i] #overwrite
    i=i+1
    if last_char in vowel:
        print("last character is vowel")
    else:
        print("last character is not vowel")    
'''o/p:
enter the string:apple
last character is vowel
last character is not vowel
last character is not vowel
last character is not vowel
last character is vowel

here iside the loop 
it will give five iteration
value.

'''
#check last third ch is vowel or not

# Input from user
str= input("Enter a string: ")

# List of vowels (both lowercase and uppercase)
vowels = ["a","e","i","o","u","A","E","I","O","U"]

# Calculate index of 3rd last character
target_index = len(str) - 3  # 3rd last character
# Make sure string has at least 3 characters
if target_index < 0:
    print("String is too short")
else:
    # Find 3rd last character using a loop
    i = 0
    char = ""
    while i <= target_index:
        char = str[i]
        i += 1

    # Check if it's a vowel
    if char in vowels:
        print("The 3rd last character is a vowel")
    else:
        print("The 3rd last character is not a vowel")
