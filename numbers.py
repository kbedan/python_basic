# https://www.programiz.com/python-programming/numbers

                    #Number Data Type in Python
"""
Python supports integers, floating-point numbers and complex numbers. 
They are defined as int, float, and complex classes in Python.

Integers and floating points are separated by the presence or absence of a decimal point.
 For instance, 5 is an integer whereas 5.0 is a floating-point number.

Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

We can use the type() function to know which class a variable or 
a value belongs to and isinstance() function to check if it belongs to a particular class."""

#Let's look at an example:

a = 5

print(type(a))

print(type(5.0))

c = 5 + 3j
print(c + 3)

print(isinstance(c, complex))
==================================================================================================
"""
While integers can be of any length, a floating-point number is accurate only up to 15 decimal places
 (the 16th place is inaccurate).

The numbers we deal with every day are of the decimal (base 10) number system. 
But computer programmers (generally embedded programmers) need to work with binary (base 2),
 hexadecimal (base 16) and octal (base 8) number systems.

In Python, we can represent these numbers by appropriately placing a prefix before that number.
 The following table lists these prefixes.""""

""""
Number System	                       Prefix 
Binary	                            '0b' or '0B'
Octal	                            '0o' or '0O'
Hexadecimal	                        '0x' or '0X'
"""

#Here are some examples

# Output: 107
print(0b1101011)

# Output: 253 (251 + 2)
print(0xFB + 0b10)

# Output: 13
print(0o15)

=====================================================================================
#Type Conversion
"""
We can convert one type of number into another. This is also known as coercion.

Operations like addition, subtraction coerce integer to float implicitly (automatically), 
if one of the operands is float."""

 1 + 2.0
3.0

"""
We can see above that 1 (integer) is coerced into 1.0 (float) for addition and 
the result is also a floating point number.


We can also use built-in functions like int(), float() and complex() to convert between types explicitly. 
These functions can even convert from strings."""

int(2.3)
2

int(-2.8)
-2

 float(5)
5.0

complex('3+5j')
(3+5j)
#When converting from float to integer, the number gets truncated (decimal parts are removed).
===================================================================================











                # Number Data Type in Python
# Python supports integers, floating-point numbers and complex numbers.
#  They are defined as int, float, and complex classes in Python.

# Integers and floating points are separated by the presence or absence of a decimal point. 
# For instance, 5 is an integer whereas 5.0 is a floating-point number.

# Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

# We can use the type() function to know which class a variable or a value belongs to and
# isinstance() function to check if it belongs to a particular class.

a = 5

print(type(a))

print(type(5.0))

c = 5 + 3j
print(c + 3)

print(isinstance(c, complex))