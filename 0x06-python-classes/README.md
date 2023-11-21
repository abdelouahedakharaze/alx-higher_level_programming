**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze



---

**_0. My first square_**

---

*_Write an empty class Square that defines a square:_*

---
- You are not allowed to import any module
=====



---

**_1. Square with size_**

---

*_Write a class Square that defines a square by: (based on 0-square.py)_*

---
- Private instance attribute: size
- Instantiation with size (no type/value verification)
- You are not allowed to import any module
=====



---

**_2. Size validation_**

---

*_Write a class Square that defines a square by: (based on 1-square.py)_*

---
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):

size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- You are not allowed to import any module
=====



---

**_3. Area of a square_**

---

*_Write a class Square that defines a square by: (based on 2-square.py)_*

---
- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):

size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module
=====



---

**_4. Access and update private attribute_**

---

*_Write a class Square that defines a square by: (based on 3-square.py)_*

---
- Private instance attribute: size:


property def size(self): to retrieve it
property setter def size(self, value): to set it:


size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0


- property def size(self): to retrieve it
- property setter def size(self, value): to set it:


size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module
=====



---

**_5. Printing a square_**

---

*_Write a class Square that defines a square by: (based on 4-square.py)_*

---
- Private instance attribute: size:


property def size(self): to retrieve it
property setter def size(self, value): to set it:


size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0


- property def size(self): to retrieve it
- property setter def size(self, value): to set it:


size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:


if size is equal to 0, print an empty line

- if size is equal to 0, print an empty line
- You are not allowed to import any module
=====



---

**_6. Coordinates of a square_**

---

*_Write a class Square that defines a square by: (based on 5-square.py)_*

---
- Private instance attribute: size:


property def size(self): to retrieve it
property setter def size(self, value): to set it:


size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0


- property def size(self): to retrieve it
- property setter def size(self, value): to set it:


size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Private instance attribute: position:


property def position(self): to retrieve it
property setter def position(self, value): to set it:


position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers


- property def position(self): to retrieve it
- property setter def position(self, value): to set it:


position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers

- position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
- Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:


if size is equal to 0, print an empty line
position should be use by using space - Don’t fill lines by spaces when position[1] > 0

- if size is equal to 0, print an empty line
- position should be use by using space - Don’t fill lines by spaces when position[1] > 0
- You are not allowed to import any module
=====



---

**_7. Singly linked list_**

---

*_Write a class Node that defines a node of a singly linked list by:_*

---
- Private instance attribute: data:


property def data(self): to retrieve it
property setter def data(self, value): to set it:


data must be an integer, otherwise raise a TypeError exception with the message data must be an integer


- property def data(self): to retrieve it
- property setter def data(self, value): to set it:


data must be an integer, otherwise raise a TypeError exception with the message data must be an integer

- data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
- Private instance attribute: next_node:


property def next_node(self): to retrieve it
property setter def next_node(self, value): to set it:


next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object


- property def next_node(self): to retrieve it
- property setter def next_node(self, value): to set it:


next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object

- next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
- Instantiation with data and next_node: def __init__(self, data, next_node=None):
=====



---

**_8. Print Square instance_**

---

*_Write a class Square that defines a square by: (based on 6-square.py)_*

---
- Private instance attribute: size:


property def size(self): to retrieve it
property setter def size(self, value): to set it:


size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0


- property def size(self): to retrieve it
- property setter def size(self, value): to set it:


size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Private instance attribute: position:


property def position(self): to retrieve it
property setter def position(self, value): to set it:


position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integer


- property def position(self): to retrieve it
- property setter def position(self, value): to set it:


position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integer

- position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integer
- Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:


if size is equal to 0, print an empty line
position should be use by using space

- if size is equal to 0, print an empty line
- position should be use by using space
- Printing a Square instance should have the same behavior as my_print()
- You are not allowed to import any module
=====



---

**_9. Compare 2 squares_**

---

*_Write a class Square that defines a square by: (based on 4-square.py)_*

---
- Private instance attribute: size:


property def size(self): to retrieve it
property setter def size(self, value): to set it:


size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number
if size is less than 0, raise a ValueError exception with the message size must be >= 0


- property def size(self): to retrieve it
- property setter def size(self, value): to set it:


size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number
if size is less than 0, raise a ValueError exception with the message size must be >= 0

- size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number
- if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area
- You are not allowed to import any module
=====



---

**_10. ByteCode -> Python #5_**

---

*_Write the Python class MagicClass that does exactly the same as the following Python bytecode:_*

---
- Tip: Python bytecode
=====

