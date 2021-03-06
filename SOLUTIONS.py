# -*- coding: utf-8 -*-
"""ITI1120TestReviewMaterial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HaaKYV9VRUuRq5K8TJxhRmYxpLEtc9gF

# Python Midterm Review
Fall, 29\10\2020

## Pedagogy
* Compressed time, so therefore the material we present may be compressed
* We want to teach what you want to know, so please ask questions.
* We're trying to keep the material as relevant to you as possible, so let us know if it's irrelevant or if there's more material you guys want to see
* Let us know if you just want to move to practice questions

## **Big O Notation**
* Big O notation is used to describe the time-efficiency of an algorithm
  * i.e Given a number of inputs $\textbf{n}$, how long will it take an algorithm to solve a problem in $\textbf{t}$ (milli)seconds\minutes\hours 

* Let $f$ and $g$ be real valued functions. $f(x),g(x) \in \mathbb{R} $ 
*$ f(x) = O(g(x))$ if there exists positive real numbers $c$ and $x_0$ such that $\mid f(x) \mid \leq c \cdot g(x)$  $\forall$ $ x \geq x_0$

![](https://drive.google.com/uc?export=view&id=1zhSaux1vJHjGmbVjjan9uJ9-pbMKrlhi)
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import os
from scipy.special import gamma
# %matplotlib inline

fig = plt.figure(figsize=(12,12),dpi = 75)
axes = fig.add_subplot(111)

x = np.linspace(1,5.5,1000)
y = np.linspace(1,5.5,1000)

plt.xticks(np.arange(min(x), max(x)+1, 1))

plt.plot(x,np.ones(1000), label = 'O(1)')
plt.plot(x,np.log2(x + 1), label = 'O(log(n))')
plt.plot(x,x, label = 'O(n)')
plt.plot(x,x*np.log2(x + 1), label = 'O(nlog(n))')
plt.plot(x,x**2, label = 'O(n²)')
plt.plot(x,2**x - 1,label = 'O(2ⁿ)')
plt.plot(x,gamma(x) * 3, label='O(n!)')

fig.legend()
# fig.plot()


fig.show()

"""### Cases
As with most things, algorithms behave differently or take a different amount of time based on the input and the content of the input
"""

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['Best', 'Average', 'Worst']
students = [10,20,30,]
ax.bar(langs,students)
plt.show()

#Example 1 - N runtime
x = [1,2,3,4,5,6,7,8,9,10,11]
n = len(x)
t = 0

print(x)

for i in range(n):
  t += 1
  x[i] += 2

print(x)
print(i)

#Example 2 - N^2 runtime
x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
n = len(x)
t = 0

print(x)

for i in range(n):
  for j in range
  t += 1
  x[i] += 2

print(x)
print(i)

"""### Practice Questions :"""

# Question 1 

n,m = 1000,1000
a,b = 0,0
for i in range(n):
  a += i

for i in range(m):
  b += i
  

# O(N * M) time, O(1) space
# O(N + M) time, O(N + M) space
# O(N + M) time, O(1) space -> Correct
# O(N * M) time, O(N + M) space

# Question 2

a = 0 
for i in range(n):
  for j in range(n,i,-1):
    a += i + j

# O(N)
# O(N*log(N))
# O(N * Sqrt(N))
# O(N*N) -> Correct

# Question 3

n = 20
ind = 0
k = 0
for i in range(n//2):
  for j in range(2,n,j*2):
    k += n/2

# O(n)
# O(nLogn) -> Correct
# O(n^2)
# O(n^2Logn)

# Question 4 

a,i = 0,1000
while(i > 0):
  a += i
  i/=2

# O(N)
# O(Sqrt(N))
# O(N / 2)
# O(log N) -> Correct

# Question 5 (Linear Search)

l = [1,2,3,6,4,9,10,12]
k = 12

for i in range(0, len(l)):
  if l[i] == k:
    print("Yes")
    break

"""---
## **Lists, Methods and Iteration**

---

  * Lists can be thought of as containers for objects. They hold one or more objects (they can be different types)
  * They can contain almost any object, including other lists (nested)
"""

#Simple Lists
a = [1,2,3,4,5,6]

#Lists can also contain objects of different types
person = [22, 160.24, 5, 0, 'Malik', 'Taylor'] #Age,Weight,Feet,Inches,First,Last

#Lists can also contain other lists among their types (more on that later)
A = [
     [1,2,3],
     [4,5,6],
     [7,8,9],
]

"""### Indexing and Slicing
* Unlike tuples, lists are mutable, meaning that they can be changed and modified, and that they can be expanded
* Usually, most of these operations are handled by Python
* **Indexing** allows us to access a particular position in a list
  * In regular indexing, lists start at **0** and end at **n-1**
  * In negative indexing, lists start at **-n** and end at **-1**
* **Slicing** allows us to take a section of the list and return it as a list
* Let's look at some examples :
"""

#Indexing
a = [1,2,3,4,5,6,7,8]

#List indices start at 0 and end at n-1
print(len(a))
print(a[0])
print(a[len(a)-1])

#Lists can also be negative indexed (Starts at -1)
print(a[-1])
print(a[-len(a)])

#Lists can be sliced. This returns a list subsection
print(a[0:2])
print(a[:]) # Not specifying a beginning or end takes the whole rest of the list
print(a[3:])
print(a[::2]) #You can also specify the steps taken in the slce

#Lists can also be negative sliced
print(a[-5:-1])
print(a[-1:-len(a)-1:-1]) ## [Start:End:StepCount]
print()

b = a[3:7]
a[5] = 12
print(b)

"""### List Methods
* There are methods that we can make use of to modify lists in python
* Remember, when doing these operations (save for copy,sorted, and reversed) we are modifying the list itself, not creating a new copy
* Pay attention to when you do and don't need a copy
"""

#Append -> Add an element to the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#Clear -> Remove all elements in a list
fruits.clear()
print(fruits)

#Copy -> Creates a copy of a list (Slicing automatically creates a copy)
a = [1,2,3,4,5,6]
b = a #Non Copied List
c = a.copy() #Copied List

a[1] = 12
print(b)
print(c)

#Count -> Returns how many instances of an object happened in an array
fruits = ['apple','cherry', 'banana', 'cherry','orange']
print(fruits.count("cherry"))
print(fruits.count("orange"))

#Extend -> Add the elements of one list to the end of another
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#Index -> Returns the first index at which a certain element occurs
fruits = ['apple', 'banana', 'cherry', 'orange', 'pineapple', 'cherry']
x = fruits.index("cherry")

#Insert -> Insert element at specific location (negative indexing works too)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(len(fruits), "orange")
print(fruits)

#Pop -> Removes the specified element of a list (negatice indexing works too)
a = [1,2,3,4,5,6,7,8]
a.pop(-2)
print(a)

#Remove -> Removes a specific element from the list
a = [1,2,3,4,5,6,7,8]
fruits = ['apple','orange','pineapple','banana','peach','tomato']
a.remove(3)
fruits.remove("tomato")
print(a)
print(fruits)

#Reverse -> Reverse the array 
a = [1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)
a.reverse


#ALTERNATE : Reversed -> Does the same thing, however it returns a copy of the array
b = reversed(a)

#Sort
words = ['zebras', 'xavier', 'wyoming', 'apples', 'cars', 'bees']
words.sort()

#ALTERNATE : Sorted -> Does the same thing, however it returns a copy of the array
words = ['zebras', 'xavier', 'wyoming', 'apples', 'cars', 'bees']
holder = sorted(words)

"""### Iteration
* Because they are sequential holders that can be indexed, it would be easier to loop over lists rather than type out individual commands repeatedly
* Loop types : 
  * For : deal with ranges and integers
  * While : deals with booleans, conditions and actions
"""

#For loops : 
a = ['ahmad','apples','oranges','bottles','orangutan']

A = [
     [1,2,3],
     [4,5,6],
     [7,8,9]
]

#Object approach
for i in a:
  print(i)

for i in A:
  for j in i:
    print(j)

#Index Approach
for i in range(len(a)):
  print(a[i])

for i in range(len(A)):
  for j in range(len(A[i])):
    print(A[i][j])

for i in range(20):
  print(i)

"""While loops will continue to loop over the child commands until it's condition is no longer satisfactory



```
while CONDITION:
  print('running command')
```
"""

#example 1
while True:
        print('THIS WILL PRINT FOREVER')

#example 2:
  user_input = input("Please put in your input: ")
  while user_input != 'exit':
        print(f'Last input: {user_input}')
        user_input = input("Please put in your input: ")
  print('while loop exited')

#example 3:
a = 5
while a > 0:
  print(f"a -> {a}")
  a = a -1

print('while loop ended')

"""the break operator can be used to terminate a while loop before it's condition has been met"""

#example 4
a = 5
while a > 0:
  print(f"a -> {a}")
  if(a ==3):
    print('terminating while loop')
    break;
    #note that I put break after the print statement (break functions like return)
  a = a -1

print('while loop ended')

"""The continue operator reverts back to the top of the loop but doesn't completely break it"""

#example 5
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

"""---
## Strings and Text Based Methods 

---

*   Strings are simply arrays of bytes representing unicode characters

*   List item
"""

a = "Hello there."
length = len(a)

#Indexing (Uncomment Code)
# print(a[6])

#Slicing (Uncomment Code)
# print(a[0:5])

#Negative indexing (Uncomment Code)
# print(a[-1])
# print(a[-12])

#Negative Slicing
# print(a[-5:-1])
# print(a[3:-2])

#Resources for Anagram Finder
from google.colab import files
uploaded = files.upload()

file_name = "english_wordbook.txt"
data = uploaded[file_name].decode("utf-8").split('\r\n')

x = input("Enter your palindrome : ")

if x in data:
  holder = x[::-1]
  if holder in data:
    print("Success! It's a Palindrome")
  else:
    print("Not a Palindrome")
else:
  print("Not a Palindrome")

if x in data

print(data)

#exmample 1 -> looping over a string
a = 'iTi1120'
for item in a:
  print(a)

#example 2 -> looping over an array
a  = ['item1', 'item2', 'item3', 'item4']
for item in a:
    print(item)

#exmaple 3 -> double for loops
a  = ['item1', 'item2', 'item3', 'item4']
for item in a:
    print(item)
    for char in item:
        print(char)

def squarefree(s):
    # We store a length to make sure that we pick the longest square free pair
    stored_length = 0
    # To increase speed (big O), the length of one of the pairs can only be up to half the length of the string
    #range -> iterates of the length of the string / 2
    #this actualy keeps track of the length
    for length in range((len(s)//2)):
        #now we actually want to go through the entire string
        for position in range(len(s)):
            # we slice the string so that we get it's current position to the length of the string
            value =s[position:position+length+1]
            # now we check if the sliced string is found twice throughout the entire string
            if s.count(value) == 2:
                #this is uncessarary 
                # if(length+1>stored_length):
                # now we check if the value we found is behind or in front of the value (next to it)
                if(value == s[position+length+1: position+length+1+length+1] or value == s[position-length-1: position]):
                    return False
    return True

user_input = input("Please type in a string ")
print(squarefree(user_input))

"""### Up Monotone
* A sequence of numbers $\{x_1,x_2,x_3...\}$ is up-monotone when $\{x_1 < x_2 < x_3 < ... < x_n\} $
* Split an integer X (such as 12345678) into sections of size d
  * For example : $(X = 12345678, d = 2 ) \rightarrow ([12],[34],[56],[78] )$
"""

#Example 3 - Up Monotone
x = input("Wass gud, enter your your first number (X) : ")
d = int(input("Aight cool, enter your second number (d) : "))

up_monotone = True
num_sections = len(x) // d

if(len(x) % d == 0):
  for i in range(0,len(x),d):
    if (i < len(x)-2) & (x[i:i+d] >= x[i+d:i+d+d]):
      up_monotone = False
else:
  up_monotone = False

print(up_monotone)

!ls

"""## Recursion
* I know it seems 'meta' and excessive for a function to call itself, but sometimes recursion offers elegant solutions, like in the case of Pell Numbers
$P = \begin{Bmatrix}0 & \text{if } n=0 \\
                    1 & \text{if } n=0 \\
                    2P_{n-1} + P_{n-1} & \text{if } n=0 \end{Bmatrix}$
* The point of emphasis is on the **base case(s)** (1 and 0 in this case)
  * These are the points at which your function will return
"""

#Pell Number

def pell_number(n = 0):
  #Base Case
  if(n == 0):
      return 0
  #Base Case
  elif(n ==1):
      return 1
  return 2*pell_number(n-1) + pell_number(n-2)

print(pell_number(6))

"""# IF AND ELSE



1.   Every if branch has to have 1 if statement
2.   Can have 0 -> infinite amount of elif statements
3.   0 - 1 else statements


*   Each if branch can only have 1 statement that prints out. After the first 
true condition is met. It will skip the remaining if statements
*   Else will only be reached if all other statements above return false
"""

def main():
    if True:
        print('if is here')
    elif True:
        print('elif is here')
    else:
        print('if all else failse this will print')
    # IT WILL ONLY HIT ONE STATEMENT

    print('NEXT IF BRANCH')

    if False:
        # as this statement is false, it will not print
        print('if is here')
    elif True:
        # this is the next statement, thus this will run, but the one under it will not 
        print('elif is here')
    else:
        print('if all else failse this will print')


    print('NEXT IF BRANCH')

    if False:
        # as this statement is false, it will not print
        print('if is here')
    elif False:
        # this is the next statement, thus this will run, but the one under it will not 
        print('elif is here')
    else:
        #as all else failed, this is the final part of the if branch and this will print, there is no check for a true statement
        print('if all else failse this will print')
    
    print('NEXT IF BRANCH')
    if True:
        print('this if branch')
    print('NEXT IF BRANCH')
    if True:
        print('and this if branch are seperate')
    else:
        print('this is branch will not print')
    print('NEXT IF BRANCH')
    if False:
        print('and this if branch are seperate')
    else:
        print('this is branch will not print')

main()