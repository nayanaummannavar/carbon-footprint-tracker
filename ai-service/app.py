from flask import Flask, request, jsonify
from flask_cors import CORS
from services.groq_client import generate_response
from dotenv import load_dotenv
import os


# Load environment variables

load_dotenv(dotenv_path=".env")

app = Flask(__name__)
CORS(app)


# ------------------ HOME ------------------
@app.route("/")
def home():
    return "AI Service Running 🚀"


# ------------------ HEALTH ------------------
@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "Service is running"
    })


# ------------------ DESCRIBE ------------------
@app.route("/describe", methods=["POST"])
def describe():
    try:
        data = request.get_json()

        if not data or "input" not in data:
            return jsonify({"error": "Input required"}), 400

        user_input = data.get("input")

        prompt = f"Explain carbon footprint of: {user_input}"

        result = generate_response(prompt)

        print("AI RESULT:", result)  # 👈 ADD THIS

        if "Error:" in result:
            return jsonify({"status": "error", "data": result}), 500

        return jsonify({"status": "success", "data": result})

    except Exception as e:
        print("ERROR:", e)  # 👈 ADD THIS
        return jsonify({"error": str(e)}), 500


# ------------------ RECOMMEND ------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()

        if not data or "input" not in data:
            return jsonify({"error": "Input required"}), 400

        user_input = data.get("input")

        prompt = f"""
        Suggest practical and eco-friendly alternatives for:
        {user_input}

        Give 3-5 actionable suggestions.
        """

        result = generate_response(prompt)

        if "Error:" in result:
            return jsonify({
                "status": "error",
                "data": result
            }), 500

        return jsonify({
            "status": "success",
            "data": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------ GENERATE REPORT ------------------
@app.route("/generate-report", methods=["POST"])
def generate_report():
    try:
        data = request.get_json()

        if not data or "input" not in data:
            return jsonify({"error": "Input required"}), 400

        user_input = data.get("input")

        prompt = f"""
        Create a structured carbon footprint report for:
        {user_input}

        Include:
        1. Estimated emissions
        2. Environmental impact
        3. Reduction tips
        4. Conclusion

        Format in bullet points.
        """

        result = generate_response(prompt)

        if "Error:" in result:
            return jsonify({
                "status": "error",
                "data": result
            }), 500

        return jsonify({
            "status": "success",
            "data": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------ RUN SERVER ------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)