import redis

cur = redis.Redis(host='127.0.0.1',port=6379,db=0,password='')

# data = {'first_name':'satish','last_name':'M','place':'Mumbai'}
data = {'first_name':'amit','last_name':'K','place':'Mumbai'}


def insert_data(table,data):
    data = str(data)
    score = cur.zcount(table,'-inf','+inf') + 1
    cur.zadd(table,{data:score})
    print('data inserted')


def delete_data(table,score):
    if cur.zremrangebyscore(table,score,score) == 0:
        print('data not exists')
    else:
        cur.zrem(table,score)
        print('data deleted successfully')

delete_data('details',2)
# insert_data('details',data)