from flask import Flask,jsonify

app = Flask(__name__)

data=[{"id":"10015","name":"santhosh"},{"id":"10016","name":"sathish"}]
@app.route('/')
def user():
    return "welcome to python"

@app.route('/api/users',methods=['GET'])
def home():
    return jsonify(data)

@app.route('/',methods=['PUT'])
def create():
    

if __name__ == '__main__':
    app.run(debug=True)
