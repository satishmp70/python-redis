import redis

cur = redis.Redis(host='127.0.0.1',port=6379,db=0,password='')

#lits inseert from head

def insert_from_head(key,data):
    cur.lpush(key,data)
    print('data inserted')

# insert_from_head('food','dosa')
# insert_from_head('food','samosha')
# insert_from_head('food','vada')
# insert_from_head('food','idli')
# insert_from_head('food','paneer')

def display_all(key):
    print(cur.lrange(key,0,-1))

display_all('food')

def length_of_key(key):
    print(cur.llen(key))

length_of_key('food')
