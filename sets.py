#https://www.programiz.com/python-programming/set/

==============================================================================================
#A set is an unordered collection of items. 
"""Every set element is unique (no duplicates) and must be immutable (cannot be changed).
However, a set itself is mutable. We can add or remove items from it.
Sets can also be used to perform mathematical set operations like
 union, intersection, symmetric difference, etc."""
===============================================================================================

#Creating Python Sets
"""A set is created by placing all the items (elements) inside curly braces {}, separated by comma, 
or by using the built-in set() function.
It can have any number of items and they may be of different types (integer, float, tuple, string etc.).
 But a set cannot have mutable elements like lists, sets or dictionaries as its elements."""

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# initialize my_set
my_set = {1, 3}
print(my_set)
=====================================================================================
'''Try the following examples as well.'''

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

my_set = {1, 2, [3, 4]}


======================================================================================
"""Creating an empty set is a bit tricky.

Empty curly braces {} will make an empty dictionary in Python. 
To make a set without any elements, we use the set() function without any argument."""

# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))

=====================================================================================
#Modifying a set in Python
"""Sets are mutable. However, since they are unordered, indexing has no meaning.
We cannot access or change an element of a set using indexing or slicing. 
Set data type does not support it.
We can add a single element using the add() method, and multiple elements using the update() method. 
The update() method can take tuples, lists, strings or other sets as its argument. 
In all cases, duplicates are avoided."""

# initialize my_set
my_set = {1, 3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

# my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)


===========================================================================
#Removing elements from a set
"""A particular item can be removed from a set using the methods discard() and remove().
The only difference between the two is that the discard() function leaves a set unchanged if the element 
is not present in the set. On the other hand, the remove() function will raise an error in such a 
condition (if element is not present  in the set)."""

#The following example will illustrate this.

# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

my_set.remove(2)
====================================================================================================

#Similarly, we can remove and return an item using the pop() method.

"""Since set is an unordered data type, there is no way of determining which item will be popped. 
It is completely arbitrary."""

#We can also remove all the items from a set using the clear() method.

# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)

print(my_set)






====================================================
x={1,2,3}
y={1,"two",(1,2,3),True,10.234}
print(type (y))
