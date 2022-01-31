import redis
import uuid
import datetime

cur = redis.Redis(host='127.0.0.1',port=6379,db=0,password='')

def insert_data(table,data):
    for key, value in data.items():
        cur.hmset(table,{key:value})
    print(cur.hgetall(table))

def update_data(table,key,value):
    if cur.hexists(table,'first_name'):
        cur.hset(table,key,value)
        print('updated')
    else:
        print('data not found')

update_data('details','first_name','amit')

# data ={'id':str(uuid.uuid1()),'first_name':'satish','last_name':'mishra','place':'mumbai','age':24,'timstamp':str(datetime.datetime.now())}

# insert_data('details',data)
