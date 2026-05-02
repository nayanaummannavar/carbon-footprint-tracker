from flask import Flask, request, jsonify
from flask_cors import CORS
from services.groq_client import GroqClient

app = Flask(__name__)
CORS(app)

client = GroqClient()

# -------------------------
# HEALTH CHECK
# -------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Service is running"
    })


# -------------------------
# TASK 5: DESCRIBE
# -------------------------
@app.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Input required"}), 400

    prompt = f"Explain the carbon footprint of: {data['input']}"

    result = client.generate_response(prompt)

    return jsonify({
        "status": "success",
        "data": result
    })


# -------------------------
# TASK 6: RECOMMEND
# -------------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Input required"}), 400

    prompt = f"Give ways to reduce carbon footprint for: {data['input']}"

    result = client.generate_response(prompt)

    return jsonify({
        "status": "success",
        "data": result
    })


# -------------------------
# TASK 6: GENERATE REPORT
# -------------------------
@app.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()

    if not data or "activities" not in data:
        return jsonify({"error": "Activities required"}), 400

    prompt = f"""
    Create a carbon footprint report for:
    {data['activities']}

    Include:
    - Impact
    - Suggestions
    """

    result = client.generate_response(prompt)

    return jsonify({
        "status": "success",
        "report": result
    })


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)