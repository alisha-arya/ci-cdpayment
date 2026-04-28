from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Payment Application Running"})

@app.route('/payment')
def payment():
    return jsonify({"status": "Payment Successful"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
