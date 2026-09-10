from flask import Flask, request, jsonify

app = Flask(__name__)

VERSION = "1.0.0"


@app.route("/health", methods=["GET"])
def health():
   return jsonify({
    "status": "healthy",
    "application": "student-ml-api",
    "application_version": "1.1.0",
    "model_version": "model-1"
})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "value" not in data:
        return jsonify({"error": "value is required"}), 400

    value = data["value"]

    if not isinstance(value, (int, float)):
        return jsonify({"error": "value must be numeric"}), 400

    return jsonify({
        "input": value,
        "prediction": value * 2
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)