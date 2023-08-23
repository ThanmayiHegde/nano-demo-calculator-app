from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    f_no = data['first']
    s_no = data['second']
    result = f_no + s_no
    res = {'result':result}
    return jsonify(res),200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    f_no = data['first']
    s_no = data['second']
    result = f_no - s_no
    res = {'result':result}
    return jsonify(res),200
   

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
