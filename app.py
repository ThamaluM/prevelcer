from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message":"This is our first test", "additional":"this is really cool"})

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)