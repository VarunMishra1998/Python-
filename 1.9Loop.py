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

while(i < 10):
    i += 1
    if(i % 3 == 0):
        continue;      # 1, 2, continue, 4, 5, continue, 7, 8, continue, 10
    print(i)

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

'''## **Step-by-Step Explanation**

1. **`word = "artificial intelligence"`**

   * Stores the sentence *artificial intelligence* in the variable `word`.

2. **`count = 0`**

   * Initializes a counter to 0 because **we haven’t counted any 'i' yet**.

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
