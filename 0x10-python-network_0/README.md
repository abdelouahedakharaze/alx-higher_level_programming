**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze




---

**_0. cURL body size_**

---

<p>Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response</p>

<p>Please test your script in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_1. cURL to the end_**

---

<p>Write a Bash script that takes in a URL, sends a <code>GET</code> request to the URL, and displays the body of the response</p>

<p>Please test your script in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_2. cURL Method_**

---

<p>Write a Bash script that sends a <code>DELETE</code> request to the URL passed as the first argument and displays the body of the response</p>

<p>Please test your script in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_3. cURL only methods_**

---

<p>Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.</p>

<p>Please test your script in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_4. cURL headers_**

---

<p>Write a Bash script that takes in a URL as an argument, sends a <code>GET</code> request to the URL, and displays the body of the response</p>

<p>Please test your script in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_5. cURL POST parameters_**

---

<p>Write a Bash script that takes in a URL, sends a <code>POST</code> request to the passed URL, and displays the body of the response</p>

<p>Please test your script in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_6. Find a peak_**

---

<p><strong>Technical interview preparation</strong>: </p>

<p>Write a function that finds <strong>a peak</strong> in a list of unsorted integers.</p>

<pre><code>guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_7. Only status code_**

---

<p>Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.</p>

<p>Please test your script in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_8. cURL a JSON file_**

---

<p>Write a Bash script that sends a JSON <code>POST</code> request to a URL passed as the first argument, and displays the body of the response.</p>

<p>Please test your scripts in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ cat my_json_0
{
    "name": "John Doe",
    "age": 33
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_1
I'm a JSON! really!
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
</code></pre>

---


---

**_9. Catch me if you can!_**

---

<p>Write a Bash script that makes a request to <code>0.0.0.0:5000/catch_me</code> that causes the server to respond with a message containing <code>You got me!</code>, in the body of the response.</p>

<p>Please test your script in the sandbox provided, using the web server running on port 5000</p>

<pre><code>guillaume@ubuntu:~/0x10$ ./102-catch_me.sh ; echo ""
You got me!
guillaume@ubuntu:~/0x10$ 
</code></pre>

---
