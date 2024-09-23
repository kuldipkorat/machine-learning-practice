from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(fname="kuldip", lname="korat")

@app.route('/test')
def test():
    data = {
   "fname":"korat"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
