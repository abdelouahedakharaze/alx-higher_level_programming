**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze

**Name:** Abdelouahed Akharaze

**GitHub:** https://github.com/abdelouahedakharaze



---

**_0. List databases_**

---

<p>Write a script that lists all databases of your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_1. Create a database_**

---

<p>Write a script that creates the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_2. Delete a database_**

---

<p>Write a script that deletes the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_3. List tables_**

---

<p>Write a script that lists all the tables of a database in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_4. First table_**

---

<p>Write a script that creates a table called <code>first_table</code> in the current database in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_5. Full description_**

---

<p>Write a script that prints the full description of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_6. List all in table_**

---

<p>Write a script that lists all rows of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_7. First add_**

---

<p>Write a script that inserts a new row in the table <code>first_table</code> (database <code>hbtn_0c_0</code>) in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_8. Count 89_**

---

<p>Write a script that displays the number of records with <code>id = 89</code> in the table <code>first_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_9. Full creation_**

---

<p>Write a script that creates a table <code>second_table</code> in the database <code>hbtn_0c_0</code> in your MySQL server and add multiples rows.</p>

<pre><code>guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_10. List by best_**

---

<p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_11. Select the best_**

---

<p>Write a script that lists all records with a <code>score &gt;= 10</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_12. Cheating is bad_**

---

<p>Write a script that updates the score of Bob to <code>10</code> in the table <code>second_table</code>.</p>

<pre><code>guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_13. Score too low_**

---

<p>Write a script that removes all records with a <code>score &lt;= 5</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_14. Average_**

---

<p>Write a script that computes the score average of all records in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_15. Number by score_**

---

<p>Write a script that lists the number of records with the same score in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_16. Say my name_**

---

<p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<p>In this example, new data have been added to the table <code>second_table</code>.</p>

<pre><code>guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_17. Go to UTF8_**

---

<p>Write a script that converts <code>hbtn_0c_0</code> database to UTF8 (<code>utf8mb4</code>, collate <code>utf8mb4_unicode_ci</code>) in your MySQL server.</p>

<p>You need to convert all of the following to <code>UTF8</code>:</p>

<pre><code>guillaume@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_18. Temperatures #0_**

---

<p>Import in <code>hbtn_0c_0</code> database this table dump: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" target="_blank" title="download">download</a></p>

<p>Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).</p>

<pre><code>guillaume@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_19. Temperatures #1_**

---

<p>Import in <code>hbtn_0c_0</code> database this table dump: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" target="_blank" title="download">download</a> (same as <code>Temperatures #0</code>)</p>

<p>Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)</p>

<pre><code>guillaume@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
guillaume@ubuntu:~/$ 
</code></pre>

---


---

**_20. Temperatures #2_**

---

<p>Import in <code>hbtn_0c_0</code> database this table dump: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" target="_blank" title="download">download</a> (same as <code>Temperatures #0</code>)</p>

<p>Write a script that displays the max temperature of each state (ordered by State name).</p>

<pre><code>guillaume@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$ 
</code></pre>

---
