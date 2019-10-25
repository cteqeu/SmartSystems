# Developed by Vincent Claes
# vincent@cteq.eu
# 14/11/2018

from flask import Flask, json, Response, render_template

app = Flask(__name__)

# test with curl -i https://xxxxx.pythonanywhere.com/hi
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
# test with curl -i https://xxxxx.pythonanywhere.com/hello/name
# test with curl -i https://xxxxx.pythonanywhere.com/hello/

@app.route('/hello/')

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)