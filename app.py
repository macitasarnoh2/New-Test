from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/add/<int:a>/<int:b>')
def add_numbers(a, b):
    return jsonify({"result": a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)