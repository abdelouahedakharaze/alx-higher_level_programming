**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze



---

**_0. First constant, first print_**

---

<p>Write a script that prints “JavaScript is amazing”:</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_1. 3 languages_**

---

<p>Write a script that prints 3 lines:</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_2. Arguments_**

---

<p>Write a script that prints a message depending of the number of arguments passed:</p>

<p>Reference: <a href="/rltoken/5kTYi3rxb6KM1_pivm-tXg" target="_blank" title="process.argv">process.argv</a></p>

<pre><code>guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_3. Value of my argument_**

---

<p>Write a script that prints the first argument passed to it:</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_4. Create a sentence_**

---

<p>Write a script that prints two arguments passed to it, in the following format: “<first argument=""> is <second argument="">”</second></first></p>

<pre><code>guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_5. An Integer_**

---

<p>Write a script that prints <code>My number: &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer:</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_6. Loop to languages_**

---

<p>Write a script that prints 3 lines: (like <code>1-multi_languages.js</code>) but by using an array of string and a loop</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_7. I love C_**

---

<p>Write a script that prints <code>x</code> times “C is fun”</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_8. Square_**

---

<p>Write a script that prints a square</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_9. Add_**

---

<p>Write a script that prints the addition of 2 integers</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_10. Factorial_**

---

<p>Write a script that computes and prints a factorial</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_11. Second biggest!_**

---

<p>Write a script that searches the second biggest integer in the list of arguments.</p>

<pre><code>guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_12. Object_**

---

<p>Update this script to replace the value <code>12</code> with <code>89</code>:</p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_13. Add file_**

---

<p>Write a function that returns the addition of 2 integers.</p>

<p><a href="/rltoken/1k6VPdLchwtGubOfPyGL1Q" target="_blank" title="Tip">Tip</a> </p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_14. Const or not const_**

---

<p>Write a file that modifies the value of <code>myVar</code> to <code>333</code></p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
</code></pre>

<p><img alt="" loading="lazy" src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4ae30fb44f708dbb3abc211b784db614e615ca21.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240212T093852Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=5f4fdd034d5e2399ca3f491d1863a5775f64c54fe19a28d4eca3b6e71c6fb60f" style=""/></p>

<p>Do you get it? Tweet! Post! Talk about it!</p>

<p>Hint: Scope</p>

<p><strong>This exercise doesn’t pass <code>semistandard</code></strong> so don’t worry about it.</p>

---


---

**_15. Call me Moby_**

---

<p>Write a function that executes <code>x</code> times a function.</p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_16. Add me maybe_**

---

<p>Write a function that increments and calls a function.</p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$ 
</code></pre>

---


---

**_17. Increment object_**

---

<p>Update this script by adding a new function <code>incr</code> that increments the integer <code>value</code>.</p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$ 
</code></pre>

---
