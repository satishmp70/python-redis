from flask import Flask
from flask import redirect 
from flask import jsonify
from flask import request
import redis
import uuid
import datetime

app = Flask(__name__)

cur = redis.Redis(host='127.0.0.1',port=6379,db=0)

@app.route('/write',methods=['POST'])

def write():
    name = request.get_json()["name"]
    email = request.get_json()["email"]
    id = uuid.uuid1()
    date = datetime.datetime.now()
    score = cur.zcount("data","-inf","+inf") + 1

    data = str({'id':score,'uuid':id,'name':name,'email':email,'created_date':date})

    cur.zadd('data',{data:score})

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True,port=5000)

