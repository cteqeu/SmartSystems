from flask import Flask, url_for, request, json, Response, jsonify
from functools import wraps

app = Flask(__name__)

# test with curl -i https://xxxxx.herokuapps.com/hi
@app.route('/hi', methods = ['GET'])
def api_hi():
    data = {
        'hello': 'world',
        'number': 456
    }
    js = json.dumps(data)
    
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link']= 'http://www.cteq.eu'
    return resp




if __name__ == '__main__':
    app.run()
   