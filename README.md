Redis basic query using python


Redis ->

Redis Basic Commands 

Connecting to a redis cli

>  redis-server 
> redis-cli

Accessing remote server
  
> redis-cli  -h 127.0.0.1 -p 6379

> redis-cli  -h 127.0.0.1 -p 6379 -p passwordhere


Repeat a cmd n of times

> redis-cli  -h 127.0.0.1 -p 6379  -r  ntimes ping


View statics 

>redis-cli –stat

Check latency\

> redis-cli --latency


Select database (only 16 data base are there in redis available)

> redis-cli 

127.0.0.1:6379> Select 1

Op -> 127.0.0.1:6379[1]>


Delete data from db

127.0.0.1:6379[1]> flushdb

Monitor cmd

>redis-cli monitor



Redis Data Type (5 type of datatype)

Strings
Lists
Hashes
Sets
Sorted Sets


Strings

Simplest kind of data type
You can store any kind of string including binary data.
The size  of the string should not go beyond 512 MB

	Cmd

 127.0.0.1:6379> SET name "satish"

127.0.0.1:6379> GET name
"Satish"


127.0.0.1:6379> append name mishra
(integer) 12
127.0.0.1:6379> GET name
"satishmishra"
127.0.0.1:6379>

Get part of strings cmd

127.0.0.1:6379> getrange name 0 4
"satis"
127.0.0.1:6379> getrange name 0 5
"satish"

To get hole string 

127.0.0.1:6379> getrange name 0 -1
"Satishmishra"

Calculate length of string
127.0.0.1:6379> strlen name
(integer) 12
127.0.0.1:6379>



Lists

 They maps b/w string fields and string values so they are the perfect data type to represent objects.
A Hash with few fields can store

Insert data at Head of list 

127.0.0.1:6379> LPUSH name "satish"


Insert data at Tail of list 

127.0.0.1:6379> RPUSH name "satish"

127.0.0.1:6379> LRANGE name 0 -1


Find length of key 

>LLEN name

Print value using index

>LINDEX name index(3)

Delete top data from list
>LPOP name


Delete last data from list
>RPOP name


 
 



HASHES
 
                Create hash
             >hmset details first_name “satish”  last_name “mishra”
 
	Display all data 

	>hgetall details(key)
  
Display using key name

>hget details first_name


Get length of hash
 
>hlen details(keyname)

Delete from hash

>hdel details(keyname)  first_name(field_name)



Insert field and value that does not exists

>hsetnx details age 24


Set

Create a set 

>sadd key_name “satish” “mishra”

Display all value 

>smembers names(key_name)

Check value is member of sets or not

>sismember names “satish”


Find intersection b/w two sets

>sinter set1 set2

Store the created sets 

>sinterstore food3 food1 food2

Detele from set 

>srem food1 “dosa”


Move member form one set to another


>smove food1 food3 “vada”


SORTED SETS

>ZADD food 1 “dosa”

>ZADD food 1 “dosa” 2 “samosa” 3 “vada”  4 “idli” 5 “paneer chelly”


>zrange food 0 -1

Get length 

>zcard food


>zrank  food “idli”


>zrem food “idli”
