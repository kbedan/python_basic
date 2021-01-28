
#What is String in Python?
"""A string is a sequence of characters.

A character is simply a symbol. For example, the English language has 26 characters.

Computers do not deal with characters, they deal with numbers (binary). 
Even though you may see characters on your screen,internally it is stored and manipulated as a combination 
of 0s and 1s.

This conversion of character to a number is called encoding, and the reverse process is decoding. 
ASCII and Unicode are some of the popular encodings used.

In Python, a string is a sequence of Unicode characters. 
Unicode was introduced to include every character in all languages and bring uniformity in encoding. 
You can learn about Unicode from Python Unicode."""

#How to create a string in Python?
"""Strings can be created by enclosing characters inside a single quote or double-quotes. 
Even triple quotes can be used in Python but generally used to represent multiline strings & docstrings.
"""
# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
=========================================================================================================

#How to access characters in a string?
"""We can access individual characters using indexing and a range of characters using slicing. 
Index starts from 0. Trying to access a character out of index range will raise an IndexError.
 The index must be an integer. We can't use floats or other types, this will result into TypeError.

Python allows negative indexing for its sequences.

The index of -1 refers to the last item, -2 to the second last item and so on. 
We can access a range of items in a string by using the slicing operator :(colon)."""

#Accessing string characters in Python
str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])




=======================================================================================================
#If we try to access an index out of the range or use numbers other than an integer, we will get errors.

# index must be in range
my_string[15]  
...
IndexError: string index out of range

# index must be an integer
my_string[1.5] 
...
TypeError: string indices must be integers




========================================================================================
#How to change or delete a string?
"""Strings are immutable. This means that elements of a string cannot be changed once they have been assigned. 
We can simply reassign different strings to the same name."""

my_string = 'programiz'
my_string[5] = 'a'
...
TypeError: 'str' object does not support item assignment
 my_string = 'Python'
my_string
'Python'

=========================================================================================

"""We cannot delete or remove characters from a string.
 But deleting the string entirely is possible using the del keyword."""

del my_string[1]
...
TypeError: 'str' object doesn't support item deletion
 del my_string
 my_string
...
NameError: name 'my_string' is not defined
=========================================================================================

#Python String Operations
"""There are many operations that can be performed with strings which makes
 it one of the most used data types in Python."""

#Concatenation of Two or More Strings
"""Joining of two or more strings into a single one is called concatenation.

The + operator does this in Python. Simply writing two string literals together also concatenates them.

The * operator can be used to repeat the string for a given number of times."""

# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

============================================================================================




===========================================================================================
age=10              #int
weight=100.5        #float
is_married=True     #Boolean
completed=False     #Boolean
name='Techcamp'
model="Toyota"


#check the data of a variable using type()
print(type=(age))
print(type=(weight))
print(type=(is_married))
print(type=(completed))


name="Tech"

