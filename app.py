from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return ''' <html> <h1>Ulcer prevention smart mattress</h1> <p>This is final year project conducted by </p><ul><li>Adrian Perera</li><li>Buddhini Edirisinghe</li><li>Helik Tribuwan</li><li>Thamalu Piyadigama</li></ul> </html>  '''
    return jsonify({"message":"This is our first test", "additional":"this is really cool"})

@app.route('/get',methods=['GET'])
def get():
    json = request.args
    result = ""
    for i in json:
        result += f"{i} is {json[i]}. \n"
    return result

@app.route('/post',methods=['POST'])
def post():
    json = request.json
    result = ""
    for i in json:
        result += f"{i} is {json[i]}. \n"
    result += "Good work Buddhini!!"
    return result

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)