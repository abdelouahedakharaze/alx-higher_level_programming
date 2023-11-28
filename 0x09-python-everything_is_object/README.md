**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze

**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze



---

**_0. Who am I?_**

---

<p>What function would you use to get the type of an object?</p>

<p>Write the name of the function in the file, without <code>()</code>.</p>

---


---

**_1. Where are you?_**

---

<p>How do you get the variable identifier (which is the memory address in the CPython implementation)?</p>

<p>Write the name of the function in the file, without <code>()</code>.</p>

---


---

**_2. Right count_**

---

<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 100
</code></pre>

---


---

**_3. Right count =_**

---

<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 89
</code></pre>

---


---

**_4. Right count =_**

---

<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a
</code></pre>

---


---

**_5. Right count =+_**

---

<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a + 1
</code></pre>

---


---

**_6. Is equal_**

---

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = "Best School"
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

---


---

**_7. Is the same_**

---

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = "Best"
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

---


---

**_8. Is really equal_**

---

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = "Best School"
&gt;&gt;&gt; s2 = "Best School"
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

---


---

**_9. Is really the same_**

---

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = "Best School"
&gt;&gt;&gt; s2 = "Best School"
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

---


---

**_10. And with a list, is it equal_**

---

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3] 
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

---


---

**_11. And with a list, is it the same_**

---

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3] 
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

---


---

**_12. And with a list, is it really equal_**

---

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

---


---

**_13. And with a list, is it really the same_**

---

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

---


---

**_14. List append_**

---

<p>What does this script print?</p>

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
</code></pre>

---


---

**_15. List add_**

---

<p>What does this script print?</p>

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
</code></pre>

---


---

**_16. Integer incrementation_**

---

<p>What does this script print?</p>

<pre><code>def increment(n):
    n += 1

a = 1
increment(a)
print(a)
</code></pre>

---


---

**_17. List incrementation_**

---

<p>What does this script print?</p>

<pre><code>def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
</code></pre>

---


---

**_18. List assignation_**

---

<p>What does this script print?</p>

<pre><code>def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
</code></pre>

---


---

**_19. Copy a list object_**

---

<p>Write a function <code>def copy_list(l):</code> that returns a <strong>copy</strong> of a list.</p>

<pre><code>guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

---


---

**_20. Tuple or not?_**

---

<pre><code>a = ()
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

---


---

**_21. Tuple or not?_**

---

<pre><code>a = (1, 2)
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

---


---

**_22. Tuple or not?_**

---

<pre><code>a = (1)
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

---


---

**_23. Tuple or not?_**

---

<pre><code>a = (1, )
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

---


---

**_24. Who I am?_**

---

<p>What does this script print?</p>

<pre><code>a = (1)
b = (1)
a is b
</code></pre>

---


---

**_25. Tuple or not_**

---

<p>What does this script print?</p>

<pre><code>a = (1, 2)
b = (1, 2)
a is b
</code></pre>

---


---

**_26. Empty is not empty_**

---

<p>What does this script print?</p>

<pre><code>a = ()
b = ()
a is b
</code></pre>

---


---

**_27. Still the same?_**

---

<pre><code>&gt;&gt;&gt; id(a)
139926795932424
&gt;&gt;&gt; a
[1, 2, 3, 4]
&gt;&gt;&gt; a = a + [5]
&gt;&gt;&gt; id(a)
</code></pre>

<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>

---


---

**_28. Same or not?_**

---

<pre><code>&gt;&gt;&gt; a
[1, 2, 3]
&gt;&gt;&gt; id (a)
139926795932424
&gt;&gt;&gt; a += [4]
&gt;&gt;&gt; id(a)
</code></pre>

<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>

---
