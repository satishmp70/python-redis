import redis

cur = redis.Redis(host='127.0.0.1',port=6379,db=0,password='')

def insert_data(table,data):
    for data in data:
        cur.sadd(table,data)
        print(cur.smembers(table))


def update_data(table,old,new):
    if cur.sismember(table,old):
        cur.srem(table,old)
        cur.sadd(table,new)
        print('data inserted')
    else:
        print('no data exist')

update_data('cities','kolkata','kanpur')

data = ['noida','mumbai','pune','delhi','bangalore','kolkata']

# insert_data('cities',data)