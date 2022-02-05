from flask import Flask
from flask import jsonify
from flask import request
import redis



app = Flask(__name__)

cur = redis.Redis(host='127.0.0.1',port=6379,db=0)

@app.route('/read',methods=['GET'])

def read():
    all_data = cur.zrange("data",0,-1,withscores=True)
    return jsonify(all_data)

@app.route('/delete/<int:score>',methods=['DELETE'])

def delete(score):
    if cur.zremrangebyscore("data",score,score) == 0:
        return jsonify({"error":"data not found in the key"})
    else:
        cur.zremrangebyscore("data",score,score)
        return read()

if __name__ == '__main__':
    app.run(debug=True,port=5000)

