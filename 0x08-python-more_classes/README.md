**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze

**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze



---

**_0. Simple rectangle_**

---

<p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
&lt;class '0-rectangle.Rectangle'&gt;
{}
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_1. Real definition of a rectangle_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>0-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_2. Area and Perimeter_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>1-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_3. String representation_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>2-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
--
##########
##########
##########
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>Object address can be different</strong></p>

<p><strong>No test cases needed</strong></p>

---


---

**_4. Eval is magic_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>3-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_5. Detect instance deletion_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>4-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_6. How many instances_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>5-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_7. Change representation_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>6-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&amp;"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_8. Compare rectangles_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>7-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_9. A square is a rectangle_**

---

<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>8-rectangle.py</code>)</p>

<pre><code>guillaume@ubuntu:~/0x08$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_10. N queens_**

---

<p><img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/><br>
<small>Chess grandmaster <a href="/rltoken/bsRwbt64OvYjWaClriv0jg" target="_blank" title="Judit Polgár">Judit Polgár</a>, the strongest female chess player of all time</small><br>
<br/></br></br></p>

<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>

<p>Read: <a href="/rltoken/dAQmi8RxMnLH-iHBzkz-lw" target="_blank" title="Queen">Queen</a>, <a href="/rltoken/TGXZXdY2Awg8m4mSjlrjjA" target="_blank" title="Backtracking">Backtracking</a></p>

<pre><code>julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code></pre>

---
