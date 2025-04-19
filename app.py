from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET', 'POST'])

def predict():
    try:
        x1 = float(request.args.get('x1', 0))
        x2 = float(request.args.get('x2', 0))
    except ValueError:
        return jsonify({"error": "Invalid input, must be numeric"}), 400

    total = x1 + x2
    prediction = 1 if total > 5.8 else 0

    return jsonify({
        "features": {"x1": x1, "x2": x2},
        "prediction": prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
