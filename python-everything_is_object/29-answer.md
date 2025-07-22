# Muttable/immutable

## 1 - Introduction

In python there are muttable or not muttable object.
Some variables in python are muttable and other not.

## 2 - id and type

The fonction 'type(X)' return the type of an object '<class 'list'>'
The function 'id(X)' return the id like '139659761671104'

## 3 - muttable object

Mutable objects are objects that can be modified after they are created. Examples of mutable objects in Python include lists, dictionaries, sets, and byte arrays. When we modify a mutable object, its memory address remains the same.

## 4 -immutable object 

Immutable objects, on the other hand, cannot be changed after creation. Python’s immutable types include integers, floats, strings, tuples, frozen sets, and bytes. Modifying an immutable object creates a new object, and the original object remains unchanged.


## 5 - why does it matter and how differently does Python treat mutable and immutable objects

Python treats them differently when it comes to memory management and object references. Immutable objects are cached, which can improve performance, especially for commonly used values like small integers and strings.

## 6 - how arguments are passed to functions and what does that imply for mutable and immutable objects

Arguments can be passed to Python functions either by reference or by value. Mutable objects passed by reference can be modified in place, while immutable objects passed by reference cannot. Examples include modifying a list in place, creating a new string with concatenation, and creating a new list with slicing

# Python function arguments example

def modify_list(some_list):
  some_list.append(4)

my_list = [1, 2, 3]

modify_list(my_list)

print(my_list) " prints [1, 2, 3, 4]

def modify_string(some_string):
    some_string += ' world'

my_string = 'hello'

modify_string(my_string)

print(my_string) " prints 'hello'